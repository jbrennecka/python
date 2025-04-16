'''
Name: Jesse Brennecka
Object Oriented Programming, Exception creation
'''

class NotNumericError(Exception):
    def __init__(self, mssg):
        self.mssg = mssg
ExceptCount = []
def LinearRegression():
    try:
        x = int(input("Please enter a number for X:\n"))
        y = int(input("Please enter a number for Y:\n"))
        b = int(input("Please enter the Y intercept:\n"))
    except Exception:
        print(f"::::::::::ERROR::::::::::\n\nPlease enter a number\n")
        ExceptCount.append(1)
        LinearRegression()
    else:
        print("Computing.....\n....\n...\n..\n.\n\n\n")
        ans = (y-b)/x
        print("The answer for variable 'm' is: ", ans)
    finally:
        errcount = 0
        if len(ExceptCount) >= 1 and errcount == 0:
            print("The program had an error and has finished.")
            errcount +=1
        elif errcount >= 1 and len(ExceptCount) >= 1:
            print("The program had "+str(len(ExceptCount))+" error/s and has finished.")
        else:
            print("\n\nThe program has finished.")

LinearRegression()