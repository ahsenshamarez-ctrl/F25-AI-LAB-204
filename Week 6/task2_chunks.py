import json, re
from pathlib import Path
ROOT=Path(__file__).parent
DOCS=json.loads((ROOT/"data/corpus.json").read_text(encoding="utf-8"))
def spans(text):
    return [(m.group(),m.start(),m.end()) for m in re.finditer(r"\\S+",text)]
def fixed_chunks(doc,size=40,overlap=0):
    if size<=0: raise ValueError("size must be positive")
    if overlap<0 or overlap>=size: raise ValueError("overlap must be from 0 to size-1")
    w=spans(doc["text"]); out=[]; step=size-overlap
    for start in range(0,len(w),step):
        part=w[start:start+size]
        if not part: break
        a,b=part[0][1],part[-1][2]
        out.append({"chunk_id":f'{doc["id"]}-fixed-{overlap}-{len(out)+1}',"source_id":doc["id"],"start_char":a,"end_char":b,"text":doc["text"][a:b],"word_count":len(part)})
    return out
def sentence_chunks(doc,budget=40):
    if budget<=0: raise ValueError("budget must be positive")
    text=doc["text"]
    sents=[(m.group().strip(),m.start(),m.end()) for m in re.finditer(r"[^.!?]+[.!?]?",text) if m.group().strip()]
    groups=[]; cur=[]; count=0
    for s,a,b in sents:
        n=len(s.split())
        if cur and count+n>budget: groups.append(cur); cur=[]; count=0
        cur.append((s,a,b)); count+=n
    if cur: groups.append(cur)
    out=[]
    for i,g in enumerate(groups,1):
        a,b=g[0][1],g[-1][2]
        out.append({"chunk_id":f'{doc["id"]}-sentence-{i}',"source_id":doc["id"],"start_char":a,"end_char":b,"text":text[a:b].strip(),"word_count":len(text[a:b].split())})
    return out
if __name__=="__main__":
    allc=[]
    for d in DOCS:
        a,b,c=fixed_chunks(d,40,0),fixed_chunks(d,40,10),sentence_chunks(d,40)
        allc+=a+b+c
        print(d["id"],"fixed/0:",len(a),"fixed/10:",len(b),"sentence:",len(c))
    (ROOT/"outputs/chunks.json").write_text(json.dumps(allc,indent=2),encoding="utf-8")
    print("Saved",len(allc),"chunks.")
    for test in [{"id":"EMPTY","text":""},{"id":"SHORT","text":"Only three words."}]:
        print("Edge case:",fixed_chunks(test))
    try: fixed_chunks(DOCS[0],40,40)
    except ValueError as e: print("Invalid overlap handled:",e)
