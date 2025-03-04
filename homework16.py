'''
Homework16
Name: Jesse Brennecka
github link:
'''

def pythagorean_thm(tuple):
    a = tuple[0]
    b = tuple[1]
    c = ((a*a) + (b*b)) ** 0.5
    c = round(c, 2)
    if c % 1 == 0:
        return int(c)
    return c

def distance_between_points(tuple1,tuple2):
    a = tuple1[0]
    b = tuple1[1]
    c = tuple2[0]
    d = tuple2[1]
    e = ((((c - a) ** 2) + ((d - b) ** 2)) ** 0.5)
    e = round(e, 2)
    if e % 1 == 0:
        return int(e)
    return e

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest16.py'))