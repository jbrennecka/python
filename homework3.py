'''
Homework3
Name: Jesse Brennecka
github link: https://github.com/jbrennecka/python/blob/main/homework3.py
'''

def positive_or_negative(num):
    if num % 2 == 0:
        print("True")
    else:
        print("False")
    return 

def is_able_to_drive(num):
    if num >= 18:
        print("True")
    else:
        print("False")
    return

def is_able_to_vote(num):
    if num >= 18:
        print("True")
    else:
        print("False")
    return

def can_buy_alcohol(num):
    if num >= 18:
        print("True")
    else:
        print("False")
    return 

def senior_discount(num):
    if num >= 55:
        print("True")
    else:
        print("False")
    return 

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest3.py'))
