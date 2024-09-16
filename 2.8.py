# (Science: calculate energy) Write a program that calculates the energy needed to
#  heat water from an initial temperature to a final temperature. Your program should
#  prompt the user to enter the amount of water in kilograms and the initial and final
#  temperatures of the water. The formula to compute the energy is 
# Q = M * (finalTemperature – initialTemperature) * 4184
#  where M is the weight of water in kilograms, temperatures are in degrees Celsius,
#  and energy Q is measured in joules.


weight = float(input("enter the weight of water in kilograms: "))

initial_temp = float(input("enter the initial temperature: "))

final_temp = float(input("enter the final temperature: "))

Q = weight * (final_temp - initial_temp) * 4184

print(f"The energy needed is {Q}") 