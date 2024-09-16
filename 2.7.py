# (Find the number of years and days) Write a program that prompts the user to
#  enter the minutes (e.g., 1 billion), and displays the number of years and days for
#  the minutes. For simplicity, assume a year has 365 days.

minutes = int(input("enter the number of minutes: "))

years = minutes // 525600

days = (minutes % 525600) // 1440

print(f"{minutes} minutes is approximately {years} years and {days} days")