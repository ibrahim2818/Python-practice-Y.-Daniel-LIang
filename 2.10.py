# Runway Length Calculation
speed = float(input("Enter speed in meters/second (m/s): "))
acceleration = float(input("Enter acceleration in meters/second squared (m/s²): "))

runway_length = (speed ** 2) / (2 * acceleration)
print(f"The minimum runway length for this airplane is {runway_length:.3f} meters")
