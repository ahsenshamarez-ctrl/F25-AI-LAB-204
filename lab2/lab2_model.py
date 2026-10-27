"""Simple temperature-mode controller with previous-mode memory."""

LOW_TEMP = 18
HIGH_TEMP = 26


def reflex_target(temperature, occupied):
    """Choose a mode using the current percept only."""
    if not occupied:
        return "OFF"
    if temperature < LOW_TEMP:
        return "HEAT"
    if temperature > HIGH_TEMP:
        return "COOL"
    return "IDLE"


class StatefulController:
    """Return target mode and whether a command should be sent."""
    def __init__(self):
        self.previous_mode = None

    def step(self, temperature, occupied):
        target = reflex_target(temperature, occupied)
        should_send = target != self.previous_mode
        if should_send:
            self.previous_mode = target
        return target, should_send
