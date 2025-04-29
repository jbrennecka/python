'''
Name: Jesse Brennecka
Calender Module 
'''
import calendar as c
import datetime as d

def main():
    
    
    try:
        # Get the user's birthmonth in order for calendar module
        userinm = input("Please enter a birth month (Jan::1, Feb::2, etc):\n")
        try:
            userinm = int(userinm)
        except Exception as g:
            print(f"\nInput (\'{userinm}\') was not an interger.\nError:\n{g}\n")
            
        # Get the current year
        thisYear = d.datetime.now().year

        # Check if input is within 1 and 12:
        if userinm > 12 or userinm < 0:
            print("Input was not between 1 and 12")
            main()
        else:
            pass
        print(c.month(thisYear, userinm))
    except Exception:
        print(f'we dun goofed...\n')
        main()
main()