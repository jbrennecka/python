'''
Homework13
Name: Jesse Brennecka
github link:
'''
def calculate_interest(principal, rateInt, time):
    simpInt = int((principal * rateInt * time))
    print(simpInt)
def compound_interest(principal, rateInt, n, time):
    compInt = round((principal * (1 + ( rateInt / n)) ** (n * time)), 2)
    print(compInt)

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest13.py'))