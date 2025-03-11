'''
Homework1
Name: Jesse Brennecka
github link: https://github.com/jbrennecka/python/blob/main/homework1p2.py
'''

import random

def check(guess, actual_number):

    while guess != actual_number:
        x = abs(actual_number - guess)
        if x < 5:
            print('Very Hot')
        elif x > 5 and x < 15:
            print('Hot')
        elif x > 15 and x < 25:
            print('Cool')
        elif x > 25:
            print('Cold')
        guess = random.randint(1, 100)
    print('You Got It!')

def main(actual_number):
    guess = random.randint(1, 100)
    check(guess, actual_number)


if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest1.py'))
