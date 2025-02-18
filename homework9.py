'''
Homework9
Name: Jesse Brennecka
github link:
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