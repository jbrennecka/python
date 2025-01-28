'''
Homework1
Name: Jesse Brennecka
github link:
'''
def add(num1, num2):
    ans1 = num1 + num2
    print(ans1)
def subtract(num1, num2):
    ans2 = num1 - num2
    print(ans2)
def multiply(num1, num2):
    ans3 = num1 * num2
    print(ans3)
def division(num1, num2):
    ans4 = num1 / num2
    print(ans4)
def int_div(num1, num2):
    ans5 = num1 // num2
    print(ans5)
def modulus(num1, num2):
    ans6 = num1 % num2
    print(ans6)
def exp(num1, num2):
    ans7 = num1 ** num2
    print(ans7)
def area(length, width):
    ans8 = length * width
    print("'The area of the rectangle with a length of 3 and a width of 4 is", ans8, end="'")
if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest1.py'))