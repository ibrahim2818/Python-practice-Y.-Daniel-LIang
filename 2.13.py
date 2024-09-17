# (Split digits) Write a program that prompts the user to enter a four-digit integer
#  and displays the number in reverse order.
number = int(input("Enter a four-digit integer: "))
reversed_number = str(number)[::-1]

print(f"The number in reverse order is {reversed_number}")
