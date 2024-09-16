# (Convert feet into meters) Write a program that reads a number in feet, converts it
#  to meters, and displays the result. One foot is 0.305 meters.
feet= float(input("enter a value for feet"))

meters = feet * 0.305

print(f"{feet} feet is {meters:4f} meters")