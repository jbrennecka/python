'''
Homework8
Name: Jesse Brennecka
github link:
'''

def sum_numbers(lst):
    y = 0
    for x in range(len(lst)):
        y += lst[x]
    print(y)
    return 

def largest_number(lst):
    y = 0
    for x in range(len(lst)):
        if y < lst[x]:
            y = lst[x]
    print(y)
    return 

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest8.py'))
