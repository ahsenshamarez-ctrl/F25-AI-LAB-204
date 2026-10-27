# Lab 2 Report: PEAS, Environment Types, and Stateful Control

**Name:** ____________________  **Course:** ____________________  **Date:** ____________________

## 1. Problem and assumptions
This lab describes two AI systems using PEAS, classifies their environments, and tests a controller that remembers its previous mode to avoid repeating identical commands.

The delivery robot operates in a real delivery area with people and moving obstacles. The LLM student-support agent can read approved course FAQs/handbook material, search course pages, and provide links. It cannot access private grades, change student records, or submit forms. A human handles sensitive cases. The original thermostat code was not found in the repository, so this example assumes HEAT below 18°C, COOL above 26°C, IDLE at 18°C and 26°C and between them, and OFF when the room is empty. Replace these if the original class code differs.

## 2. PEAS specifications

### Delivery robot
- **Performance:** deliver the correct parcel; avoid collisions; arrive on time; preserve battery; protect parcel condition.
- **Environment:** corridors and pavements; people and pets; doors and lifts; temporary obstacles; delivery locations.
- **Actuators:** drive wheels/steering; brakes; parcel compartment or gripper; status lights/speaker.
- **Sensors:** camera/depth camera; lidar or ultrasonic sensor; wheel encoders; GPS outdoors; IMU; battery sensor.
- **Trade-off:** faster driving may improve delivery time but increases stopping distance and collision risk. Safety should take priority when sensor confidence is low.

### LLM-based student-support agent
- **Performance:** accurate answers based on approved sources; clear explanations; quick replies; privacy; escalation when uncertain.
- **Environment:** student questions; course FAQs and handbook; course pages; changing deadlines; ambiguous wording; language/accessibility needs.
- **Actuators:** display an answer; ask a clarifying question; cite/link an approved source; suggest contacting staff; draft a ticket only if that tool is explicitly enabled.
- **Sensors:** incoming message and conversation context; retrieved document snippets; tool status/errors; user-provided course/week identifier.
- **Tool assumptions and trade-off:** it can search approved course documents and give links, but cannot read grades or change records. Checking sources can improve accuracy but take longer; a quick unsupported answer may be wrong.

## 3. Environment classifications

| System | Observability | Determinism | Example and justification |
|---|---|---|---|
| Delivery robot, real world | Partially observable | Stochastic | A camera may not show a person behind a door. The same drive command may have different outcomes because people move, wheels slip, or sensors are noisy. |
| Student-support LLM, real world | Partially observable | Stochastic | It may not know a deadline changed unless the approved source is updated. Model generation and retrieval/tool errors can make answers vary. |

A simplified robot simulator with a complete map, exact sensor values, and fixed physics can be fully observable and deterministic. A fixed student-support test harness with fixed documents and fixed model outputs can also look deterministic. These are simulator assumptions, not guaranteed properties of real systems. Adding random obstacles, model sampling, or tool errors makes a simulator stochastic.

## 4. Stateful controller and results
The reflex function chooses a target from the current percept. The stateful class remembers the previous target and returns `(target, should_send)`. It sends a command only if the target changes. Empty-room status takes priority and selects OFF.

| Case | Previous mode | Percept | Target | Command |
|---|---|---|---|---|
| cold room | NONE | 17°C, occupied | HEAT | SEND |
| same cold percept repeated | HEAT | 17°C, occupied | HEAT | NO COMMAND |
| lower exact boundary | HEAT | 18°C, occupied | IDLE | SEND |
| same boundary repeated | IDLE | 18°C, occupied | IDLE | NO COMMAND |
| upper exact boundary | IDLE | 26°C, occupied | IDLE | NO COMMAND |
| hot room | IDLE | 27°C, occupied | COOL | SEND |
| same hot percept repeated | COOL | 27°C, occupied | COOL | NO COMMAND |
| empty room despite cold temperature | COOL | 17°C, empty | OFF | SEND |
| empty room repeated | OFF | 17°C, empty | OFF | NO COMMAND |

The trace includes repeated percepts, both exact boundaries, mode transitions, and an empty-room case. The stateful and reflex controllers should choose the same target, but the reflex controller may send duplicate commands each time it runs.

## 5. Edge case, limitations, and improvement
An invalid sensor value such as -100°C would be treated as a very cold room and select HEAT. The likely cause is missing input validation. A better version should validate the sensor range and use a safe fallback or alert when readings are invalid. This example also omits hysteresis, manual override, and actuator-failure handling; a real thermostat may need hysteresis to avoid rapid switching near a threshold.

## 6. Reflection and responsible practice
This small controller is easy to read and shows why remembering state can reduce repeated commands. The test trace checks boundaries and transitions, but does not prove safety in every case. A delivery robot should prioritize bystander safety over speed. A student-support agent should use current approved sources, protect student information, admit uncertainty, and refer sensitive issues to a human. Tool permissions should be limited to what the agent needs.

## 7. Reproduction
Use Python 3.9 or newer. From the `lab2` folder run `python lab2_check.py`. It writes `outputs/mode_trace.csv` and `outputs/check_output.txt`.

## References
1. S. Russell and P. Norvig, *Artificial Intelligence: A Modern Approach*, 4th ed., Pearson, 2021.
2. A. M. Turing, “Computing Machinery and Intelligence,” *Mind*, 1950. https://doi.org/10.1093/mind/LIX.236.433
3. NIST, *AI Risk Management Framework (AI RMF 1.0)*, 2023. https://www.nist.gov/itl/ai-risk-management-framework

The controller thresholds in this report are stated assumptions because the original source code was not present in the repository. Reconcile them with the instructor's original code before submitting.
