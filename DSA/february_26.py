class Counter:
    """Counter class"""

    def __init__(self, integer) -> None:
        """Initialization"""
        self.integer = integer

    def get_count():
        """Return current count"""
        return self.integer

    def increment():
        """Increments the couny by 1"""
        self.integer += 1

    def reset():
        """Reset count to zero"""
        self.integer = 0


class LimitCounter(Counter):
    """LimitCounter class"""

    def __init__(self, integer, threshold = 100) -> None:
        """Initialization"""
        if integer <= threshold: self.integer = integer
        else: 
            raise ValueError("Error, count exceeds max threshold.")


class Thermostat:
    """Thermostat class"""

    def __init__(self, temperature = 75) -> None:
        """Initialization"""
        self.temperature = temperature

    def get_temperature():
        """Return current temperature"""
        return self.temperature
    
    def set_temperature(new_temp):
        """Update current temperature"""
        if 50 <= new_temp <= 90:
            self.temperature = new_temp
        else:
            raise ValueError("Error.")

    def __str__(self) -> str:
        """Print the current temperature"""
        return "Thermostat set to {self.temperature}°F"

class SmartThermostat(Thermostat):
    """SmartThermostat class"""

    def __init__(self, temperature=75, eco_mode = False) -> None:
        """Initialization"""
        super().__init__(temperature)
        self.eco_mode = eco_mode

    def set_temperature(new_temp):
        """Update the current temperature"""
        if self.eco_mode and 60 <= new_temp <= 78:
            self.temperature = new_temp
        else:
            return "Error."

    def toggle_eco_mode():
        self.eco_mode = not self.eco_mode

    def __str__(self) -> str:
        status = "ON" if self.eco_mode else "OFF"
        return "Thermostat set to {self.temperature}°F with eco_mode {status}."


