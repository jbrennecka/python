'''
Homework15
Name: Jesse Brennecka
github link: https://github.com/jbrennecka/python/blob/main/homework15.py
'''

def factorial(n):
    if n != 0 or n != 1:
        m = 1
        for x in range(1, n+1):
            m *= x
        return m    
    else:
        return 1

def main(num1):
    
    ans = factorial(num1)
    print("\"The factorial of " + str(num1) + " is " + str(ans) + ".\"")
    return

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest15.py'))
