'''
Name: Jesse Brennecka
Datetime module: Age Calculator
'''
import datetime

def main():
    # This is a program that will take the input of the user
    # and will output how old said person is, measured by
    # years, months, weeks, and days.
    print("\n")

    # Each variable takes the input from the user
    useriny = int(input("Please enter the year of birth:\n"))
    userinm = int(input("Please enter the numerical birth month (Jan::1, Feb::2, etc):\n"))
    userind = int(input("Please enter the birthday:\n"))

    # Now will take the variables and compare them to datetime info
    try:
        today = datetime.datetime.today()
        bday = datetime.datetime(useriny, userinm, userind)

        # This will take the difference of today and the birthday
        # and divide it between year, month, weeks, and days
        bday_out = bday.strftime("%Y : %m : %d")
        print("This is the inputted birthdate:\n", bday_out)
        delta = today - bday
        years = delta.days // 365.2425
        print("This is the difference from today in years: ", int(years))
        months = delta.days // (365.3435 / 12)
        print("This is the difference from today in months: ", int(months))
        weeks = delta.days // (356.2425 / 52)
        print("This is the difference from today in weeks: ", int(weeks))
        days = delta.days
        print("This is the difference from today in days: ", int(days))
    except Exception as e:
        print(f'we dun goofed........{e}')

main()