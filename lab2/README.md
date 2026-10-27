# Lab 2

This folder contains the Lab 2 PEAS report, a simple stateful thermostat example, input cases, and output trace.

## Run
Use Python 3.9 or newer. No third-party packages are needed.

```bash
python lab2_check.py
```

The script prints the trace and writes `outputs/mode_trace.csv` and `outputs/check_output.txt`.

## Assumptions
The original temperature-control code was not in the repository when this task was prepared. This example uses HEAT below 18°C, COOL above 26°C, IDLE from 18°C through 26°C, and OFF when the room is empty. The empty-room rule has priority. Replace these assumptions if your instructor's original code uses different thresholds or modes.
