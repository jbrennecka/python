'''
Homework5
Name: Jesse Brennecka
github link: https://github.com/jbrennecka/python/blob/main/homework5.py
'''

def collatz_conjecture(num):
    print(float(num))
    while num != 1.0:
        if num % 2 == 0:
            num = num / 2
            print(num)
        else:
            num = num * 3 + 1
            print(num)
    return

def add_numbers(num):
    x = 1
    y = 0
    while x < num:
        y = y + x
        x = x + 1
        
    print(y)
    return

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest5.py'))
