'''
Homework7
Name: Jesse Brennecka
github link: https://github.com/jbrennecka/python/blob/main/homework7.py
'''


def fizzbuzz(num):
    for x in range(1, num + 1):
        if x % 3 == 0 and x % 5 == 0:
            print("FizzBuzz")
        elif x % 5 == 0:
            print("Buzz")
        elif x % 3 == 0:
            print("Fizz")
        else:
            print(x)
    return 

def scholarship_eligibility(gpa,credits):
    # I figured since the doctest was going to test whether if the code output
    # was true or false rather than printing "true" or "false", I didn't use
    # the print() function
    if gpa >= 3.5 and credits >= 60:
        return True
    else:
        return False

def max_of_three_numbers(num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
        print(num1)
    elif num2 >= num1 and num2 >= num3:
        print(num2)
    elif num3 >= num1 and num3 >= num1:
        print(num3)
    return

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest7.py'))
