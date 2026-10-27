# Week 2 — PEAS and Stateful Control

This week's work covers PEAS specifications for a delivery robot and an LLM-based student-support agent, environment classifications, and a temperature-mode controller that avoids sending the same command repeatedly.

## Files
- [Lab 2 report in Markdown](lab2/Lab2_Report.md)
- [README and run instructions](lab2/README.md)
- [Controller implementation](lab2/lab2_model.py)
- [Percept cases](lab2/lab2_percepts.py)
- [Test runner](lab2/lab2_check.py)
- [Input data](lab2/data/percepts.csv)
- [Recorded CSV trace](lab2/outputs/mode_trace.csv)
- [Captured console output](lab2/outputs/check_output.txt)

A Word-format report is available as a download in the ChatGPT conversation. The committed Markdown report contains the same main sections; upload the downloaded `.docx` to `lab2/Lab2_Report.docx` before final course submission if the instructor requires the Word file to be in GitHub.

## Important assumption
The earlier temperature-control source was not present in the repository. This example therefore uses HEAT below 18°C, COOL above 26°C, IDLE at 18–26°C inclusive, and OFF whenever the room is empty. If the original class code uses different thresholds, update the controller and trace before submitting.

## Run
Open a terminal in the `lab2` folder and run:

    python lab2_check.py

Before submitting, add your details to the report and check the assumptions against the original class code.