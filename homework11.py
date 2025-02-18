'''
Homework11
Name: Jesse Brennecka
github link: 
'''

def count_zeros(lst):
    # sorry for the lateness, the 'replace with zero' function was giving me trouble
    a = lst[:]
    x = 0
    for y in a:
        for z in y:
            if z == 0:
                x += 1
    print(x)
    return 

def replace_with_zero(lst):
    # your code here
    a = lst[:]
    c = []
    for x in a:
        b = []
        for y in x:
            if y <= 0:
                y = 0
            b.append(y)
        c.append(b)
    print(c)
    return

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest11.py'))