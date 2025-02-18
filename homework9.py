'''
Homework9
Name: Jesse Brennecka
github link: https://github.com/jbrennecka/python/blob/main/homework9.py
'''

def bubble_sort(lst):
    # list to variable, variable sorting, then print answer
    var = lst
    var.sort()
    print(var)
    return 

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest9.py'))
