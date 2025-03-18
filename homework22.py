'''
Homework22
Name:   Jesse Brennecka
github link: https://github.com/jbrennecka/python/blob/main/homework22.py
'''
def mask_creditcard(string):
    card = ""
    count = 0
    for i in str(string):
        count += 1
        if count <= 12:
            card += "*"
        else:
            card += i
    print('\'' + card + '\'')
    
def remove_vowels(string):
    vowels = "aeiouAEIOU"
    sent = ""
    for i in str(string):
        if i not in vowels:
            sent += i
    print('\'' + sent + '\'')


if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest22.py'))
