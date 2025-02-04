'''
Homework2.5
Name: Jesse Brennecka
github link: https://github.com/jbrennecka/python/blob/main/homework25.py
'''

#using given input from other file, take var and organize into correct grammar and sentence structure
def birthday(month,day,year):
    start = "Your birthday is"
    print('\'' + str(start), month, str(day) + ',', str(year) + '.\'')
    return 

def address(street,city,state,zip):
    start2 = "Your address is"

    print('\'' + start2, str(street) + ',', city + ',', state + ',', str(zip) + '.\'')

    return 

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest25.py'))
