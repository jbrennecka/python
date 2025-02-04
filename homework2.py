'''
Homework2
Name: Jesse Brennecka
github link: https://github.com/jbrennecka/python/blob/main/homework2.py
'''

def inches_to_cm(inch):
    x = round((inch * 2.54), 2)
    return x

def feet_to_meters(ft):
    y = round((ft * 0.3048), 2)
    return y

def lbs_to_kg(lbs):
    z = round((lbs / 2.20462), 2)
    return z

def hours_to_minutes(hrs):
    mins = hrs * 60
    return mins

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest2.py'))
