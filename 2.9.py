# (Science: wind-chill temperature) How cold is it outside? The temperature alone is
#  not enough to provide the answer. Other factors including wind speed, relative
#  humidity, and sunshine play important roles in determining coldness outside. In
#  2001, the National Weather Service (NWS) implemented the new wind-chill tem
# perature to measure the coldness using temperature and wind speed. The formula
#  is given as follows:
#  twc = 35.74 + 0.6215ta- 35.75v0.16 + 0.4275tav0.16
#  where 
# ta
#  is the outside temperature measured in degrees Fahrenheit and v is the
#  speed measured in miles per hour. 
# twc
#  is the wind-chill temperature. The formula
#  cannot be used for wind speeds below 2 mph or for temperatures below 
# above 41°F. 
# Write a program that prompts the user to enter a temperature between -58F
#  or
#  and
#  41°F and a wind speed greater than or equal to 2 and displays the wind-chill tem
# perature. 
# Wind-Chill Temperature Calculation
temperature = float(input("Enter the temperature in Fahrenheit between -58 and 41: "))
wind_speed = float(input("Enter the wind speed in miles per hour (>= 2): "))

if -58 <= temperature <= 41 and wind_speed >= 2:
    wind_chill = (35.74 + 0.6215 * temperature 
                  - 35.75 * wind_speed ** 0.16 
                  + 0.4275 * temperature * wind_speed ** 0.16)
    print(f"The wind chill index is {wind_chill}")
else:
    print("Invalid input. Temperature or wind speed is out of range.")
