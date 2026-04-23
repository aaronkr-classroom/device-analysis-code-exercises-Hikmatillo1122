class RoomSensor:
    def __init__(self, name, temperature, humidity, light):
        self.name = name
        self.temperature = temperature
        self.humidity = humidity
        self.light = light

    def show_info(self):
        """Prints all sensor data in a readable format."""
        print(f"Sensor: {self.name}")
        print(f"Temperature: {self.temperature}")
        print(f"Humidity: {self.humidity}")
        print(f"Light: {self.light}")

    def comfort_level(self):
        """
        Evaluates if the room is comfortable based on 
        standard temperature and humidity ranges.
        """
        # Define comfortable ranges
        temp_ok = 20 <= self.temperature <= 26
        hum_ok = 30 <= self.humidity <= 60

        if temp_ok and hum_ok:
            return "Comfortable"
        elif not temp_ok and not hum_ok:
            return "Uncomfortable: Check Temp & Humidity"
        elif not temp_ok:
            return "Uncomfortable: Temperature outside range"
        else:
            return "Uncomfortable: Humidity outside range"

# --- Testing the methods ---
if __name__ == "__main__":
    my_sensor = RoomSensor("Living Room", 26, 55, 420)
    my_sensor.show_info()
    print(f"Status: {my_sensor.comfort_level()}")
