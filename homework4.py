'''
Homework4
Name: Jesse Brennecka
github link: 
'''

def grade_calculator(score):
    if score <= 100:
        if score >= 0:
            if score < 60:
                print('\'F\'')
            elif score < 70:
                print('\'D\'')
            elif score < 80:
                print('\'C\'')
            elif score < 90:
                print('\'B\'')
            else:
                print('\'A\'')
        else:
            print('\'Enter a grade between 0-100\'')
    else: print('\'Enter a grade between 0-100\'')
    return

def even_or_odd(num):
    if num % 2 == 0:
        print('\'even\'')
    else:
        print('\'odd\'')
    return 



if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest4.py'))