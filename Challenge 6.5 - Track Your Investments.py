# Chapter 6.5 Python Basics by The Real Python Team
# In this Challenge, You'll write a program called invest.py that tracks the growing amount of an investment overtime.
# The initial deposit for an investment is called the principal amount. Each year, the amount increases by a fixed
# percentage, called the annual rate of return.
# For example, a principal amount of $100.00 with an annual rate of return of 5 percent increases the first year by $5
# for a new amount of $105.00. The second year, the increase is 5% of $105.00, or $5.25, bringing the total to $110.25.

# Write a function called invest with three parameters: the principal amount, the annual rate of return, and the number
# of years to calculate. The function signature might look something like this:
# def invest(amount, rate, years):
# The function should then print out the amount of the investment, rounded to two decimal places, at the end of each
# year for the specified number of years.
# For example, calling investment(100, .05, 4) should print the following:
# Year 1: $105.00
# Year 2: $110.25
# Year 3: $115.76
# Year 4: $121.55

# To finish the program, prompt the user to enter an initial amount, an annual percentage rate, and a number of years.
# then call invest() to display the calculation for the values entered by the user.

def invest(amount, rate, years):
    """ to calculate the investment """
    for investment in range(1, years+1):
        amount = (amount * rate) + amount
        print(f"Year {investment}: ${amount:.2f}")


users_amount = float(input("Enter the amount: "))
users_rate = float(input("Enter the rate: "))
users_years = int(input("Enter the year: "))

print("The results of your investment is: ")
invest(users_amount, users_rate, users_years)
