class RoomSensor:
    def __init__(self, name, temperature, humidity, light):
        """
        Initializes the RoomSensor with specific environment data.
        
        :param name: String representing the sensor's location or ID
        :param temperature: Float/Int for the current temperature
        :param humidity: Float/Int for the humidity percentage
        :param light: Float/Int for the light level (e.g., in lux)
        """
        self.name = name
        self.temperature = temperature
        self.humidity = humidity
        self.light = light

