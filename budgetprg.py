'''
Interacting with User Input
Name: Jesse Brennecka
github: 

This program is to budget one's income, one will give approx weekly income, the program
will take this number and will output an annual amount, then one would put in their monthly expences
with the appropriate prompt, the program will take this and will give the annual amount, with the
difference between the income and expenses presented in a weekly amount
'''

#Collecting data
weeklyIncome = input("What is your weekly income? ")

rent = input("How much do you pay per month for housing? ")
utilities = input("How much do you pay per month for utilities? ")
groceries = input("How much do you pay per month for groceries? ")
transportation = input("How much do you pay per month for transportation? ")
healthCare = input("How much do you pay per month for healthcare? ")
personalCare = input("How much do you pay per month for personal affects? As in manicures, haircuts, that sort of thing. ")
clothing = input("How much do you pay for clothing? ")
debt = input("How much per month do you have to pay your debts, if any? ")


#take income and make annual amount, print for user
annualIncome = round(float(weeklyIncome) * 52, 2)
print("Annual income: $ {:.2f}".format(annualIncome))

#take individual expences and make annual amount, print for user
rent = round(float(rent) * 12)
utilities = round(float(utilities) * 12)
groceries = round(float(groceries) * 12)
transportation = round(float(transportation) * 12)
healthCare = round(float(healthCare) * 12)
personalCare = round(float(personalCare) * 12)
clothing = round(float(clothing) * 12)
debt = round(float(debt) * 12)
print("Yearly amount spent on...")
print("Rent: $ {:.2f}".format(rent))
print("Utilities: $ {:.2f}".format(utilities))
print("Groceries: $ {:.2f}".format(groceries))
print("Transportation: $ {:.2f}".format(transportation))
print("Healthcare: $ {:.2f}".format(healthCare))
print("Personal care: $ {:.2f}".format(personalCare))
print("Clothing: $ {:.2f}".format(clothing))
print("Debts: $ {:.2f}".format(debt))

#take expenses and combine annual amounts, print for user
expenses = round(float(rent) * 12, )
print("Collected yearly expenses: $" + str(expenses))

#Present the difference
difference = annualIncome - expenses
print("This is the difference in income and yearly expenses: ${:.2f}".format(difference))

#Based off of difference, will represent the amount available per week, or the amount that must be saved in order to fit within given income
difference = difference / 52
if difference >= 0:
    print("You have about $ {:.2f}".format(difference), " per week to spend")
else:
    print("You are $ {:.2f}".format(difference), " per week in the hole")