import json,csv,time
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from task2_chunks import DOCS,fixed_chunks,sentence_chunks
ROOT=Path(__file__).parent
QS=json.loads((ROOT/"data/queries.json").read_text(encoding="utf-8"))
def make_chunks(strategy):
    result=[]
    for d in DOCS:
        if strategy=="fixed0": result+=fixed_chunks(d,40,0)
        elif strategy=="fixed10": result+=fixed_chunks(d,40,10)
        else: result+=sentence_chunks(d,40)
    return result
def run(strategy):
    chunks=make_chunks(strategy); t=time.perf_counter()
    vec=TfidfVectorizer(ngram_range=(1,2)); matrix=vec.fit_transform([c["text"] for c in chunks])
    enc=time.perf_counter()-t; rows=[]; search=0; metrics={}
    for split in ("dev","test"):
        hit=[]; rr=[]
        for q in [x for x in QS if x["split"]==split]:
            t=time.perf_counter(); scores=cosine_similarity(vec.transform([q["query"]]),matrix).ravel(); order=scores.argsort()[::-1][:3]; search+=time.perf_counter()-t
            rank=None
            for r,i in enumerate(order,1):
                c=chunks[i]
                rows.append({"strategy":strategy,"query_id":q["id"],"split":split,"query":q["query"],"rank":r,"chunk_id":c["chunk_id"],"source_id":c["source_id"],"score":round(float(scores[i]),6),"start_char":c["start_char"],"end_char":c["end_char"],"text":c["text"],"relevant_doc":q["relevant_doc"],"answerable":q["answerable"]})
                if q["answerable"] and c["source_id"]==q["relevant_doc"] and rank is None: rank=r
            if q["answerable"]:
                hit.append(int(rank is not None)); rr.append(1/rank if rank else 0)
        metrics[split]={"Hit@3":round(sum(hit)/len(hit),3),"MRR@3":round(sum(rr)/len(rr),3)}
    return rows,{"strategy":strategy,"chunks":len(chunks),"metrics":metrics,"vectorize_seconds":round(enc,6),"search_seconds_total":round(search,6)}
if __name__=="__main__":
    allrows=[]; summaries=[]
    for s in ("fixed0","fixed10","sentence"):
        rows,summary=run(s); allrows+=rows; summaries.append(summary); print(summary)
    (ROOT/"outputs").mkdir(exist_ok=True)
    with (ROOT/"outputs/retrieval_log.csv").open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=list(allrows[0])); w.writeheader(); w.writerows(allrows)
    (ROOT/"outputs/metrics.json").write_text(json.dumps(summaries,indent=2),encoding="utf-8")
    print("Saved retrieval_log.csv and metrics.json. Select on dev; report test separately.")
    print("Unanswerable questions still receive nearest chunks; similarity is not proof of an answer.")
