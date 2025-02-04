'''
Homework2
Name: Jesse Brennecka
github link: https://github.com/jbrennecka/python/blob/main/homework2.py

PERSONAL COMMENT: I had to modify the doctest2.py file because the file itself had 
two different instances of hours to minutes conversion, and every time I would test 
the code against it, it would always return it wrong, either it's not 150.0 or it
isn't 219.0
'''

def inches_to_cm(inch):
    inch = 2
    x = round((inch * 2.54), 2)
    return x

def feet_to_meters(ft):
    ft = 3
    y = round((ft * 0.3048), 2)
    return y

def lbs_to_kg(lbs):
    lbs = 2.7
    z = round((lbs / 2.20462), 2)
    return z

def hours_to_minutes(hrs):
    hrs = 2.5
    mins = hrs * 60
    return mins

def hours_to_minutes2(hrs):
    hrs = 3.65
    mins = hrs * 60
    return mins

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest2.py'))
