"""Run repeated percepts and save the stateful controller trace."""
import csv
from pathlib import Path
from lab2_model import StatefulController
from lab2_percepts import PERCEPTS

ROOT = Path(__file__).resolve().parent
OUTPUTS = ROOT / "outputs"
OUTPUTS.mkdir(exist_ok=True)


def run():
    controller = StatefulController()
    rows = []
    lines = []
    for label, temperature, occupied in PERCEPTS:
        previous = controller.previous_mode or "NONE"
        target, should_send = controller.step(temperature, occupied)
        command = "SEND" if should_send else "NO COMMAND"
        rows.append({"case": label, "previous_mode": previous,
                     "temperature_c": temperature, "occupied": occupied,
                     "target_mode": target, "command": command})
        lines.append(f"{label}: previous={previous}; percept=({temperature} C, occupied={occupied}); target={target}; command={command}")

    with (OUTPUTS / "mode_trace.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    output = "\n".join(lines) + f"\n\nCases run: {len(rows)}\n"
    (OUTPUTS / "check_output.txt").write_text(output, encoding="utf-8")
    print(output)

if __name__ == "__main__":
    run()
