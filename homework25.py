'''
Homework24
Name:   Jesse Brennecka
github link: https://github.com/jbrennecka/python/blob/main/homework25.py
'''

def flowers(idx,list_of_flowers):
    try:
        print('You selected: ' + list_of_flowers[idx])
    except IndexError:
        print('Number out of range! Please choose a valid flower number.')
    except TypeError:
        print('Invalid input! Please enter a number.')

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest25.py'))
