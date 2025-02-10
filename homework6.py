'''
Homework6
Name: Jesse Brennecka
github link:
'''

def div_by_seven(num):
    for num in range(1, num):
        if num % 7 == 0:
            print(num)
    return 

def squares_of_numbers(num):
    for x in range(1, num):
        x = pow(x, 2)
        print(x) 
    return 

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest6.py'))