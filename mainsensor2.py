from room_sensor import RoomSensor

# Part 3: Create and Store Multiple Objects
# We create three instances with values that test different logic branches
sensors = [
    RoomSensor("Kitchen", 31, 72, 180),   # Expected: Warning, Dark
    RoomSensor("Bedroom", 23, 50, 450),   # Expected: Comfortable, Bright
    RoomSensor("Balcony", 18, 30, 600)    # Expected: Normal, Bright
]

# Part 4: Loop Through the List
for sensor in sensors:
    # 1. Print sensor information (Name, Temp, Humidity, Light)
    sensor.show_info()
    
    # 2. Print the calculated comfort level
    print(f"Comfort Level: {sensor.comfort_level()}")
    
    # 3. Print the light status
    print(f"Light Status: {sensor.light_status()}")
    
    # Separator for readability between sensors
    print("-" * 20)
