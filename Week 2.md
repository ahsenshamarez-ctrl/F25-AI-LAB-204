# Week 2 — PEAS and Stateful Control

This week's work covers PEAS specifications for a delivery robot and an LLM-based student-support agent, environment classifications, and a temperature-mode controller that avoids sending the same command repeatedly.

The detailed report is `lab2/Lab2_Report.docx`. Source code, sample inputs, and captured output are in `lab2/`.

**Important assumption:** The earlier temperature-control code was not present in this repository. The example currently uses HEAT below 18°C, COOL above 26°C, IDLE at both boundaries and between them, and OFF when the room is empty. Replace these values if the original lab code uses different rules.
