'''
Homework21
Name:   Jesse Brennecka
github link: https://github.com/jbrennecka/python/blob/main/homework21.py
'''
def is_palindrome(string):
    sent1 = []
    sent2 = []
    for i in str(string):
        sent1.append(i)
    for i in str(string):
        sent2.append(i)
    sent2.reverse()
    if sent1 == sent2:
        return True
    else:
        return False
    
def is_anagram(string1,string2):
    sent1 = []
    sent2 = []
    for i in str(string1):
        sent1.append(i)
    for i in str(string2):
        sent2.append(i)
    sent1.sort()
    sent2.sort()
    if sent1 == sent2:
        return True
    else:
        return False


if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest21.py'))
