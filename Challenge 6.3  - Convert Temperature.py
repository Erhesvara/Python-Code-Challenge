# Chapter 6.3 Python Basics by The Real Python Team
# Write a program called temperature.py that defines two functions:
# 1. convert_cel_to_far(), which takes one float parameter representing degrees celsius and returns a float representing
#    the same temperature in degrees Fahrenheit using the following formula:
#    F = C * 9/5 + 32
# 2. convert_far_to_cel(), which takes one float parameter representing degrees Fahrenheit and returns a float
#    representing the same temperature in degrees Celsius using the following formula:
#    C = (F - 32) * 5/9

# 1.
def convert_cel_to_far(c):
    """ converts celsius to Fahrenheit """
    f = c * 9/5 + 32
    return f


# 2.
def convert_far_to_cel(f):
    """ converts fahrenheit to celsius """
    c = (f - 32) * 5/9
    return c


user_cel = float(input("Enter a temperature in degrees F: "))
print(f"{user_cel} degrees F = {convert_far_to_cel(user_cel):.2f} degrees C")

user_far = float(input("Enter a temperature in degrees C: "))
print(f"{user_far} degrees C = {convert_cel_to_far(user_far):.2f} degrees F")
