'''
Homework18
Name: Jesse Brennecka
github link:
'''

def iterate_dictionary(lst):
    dict = {1:"one",2:"two",3:"three"}
    for num in lst:
        try:
            print(dict[num])
        except:
            print("Number not in dictionary")
    # your code here
    return

def check_if_positive(lst):
    for x in lst:
        try:
            ans = int(x)
            if ans > 0:
                print(x)
            else:
                print("not positive")
        except ValueError:
            print("not positive")
    return

def division(lst):
    for x in lst:
        try:
            ans = 100 / x
            print(round(ans, 2))
        except ZeroDivisionError:
            print("can\'t divide by zero")
    return 

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest18.py'))