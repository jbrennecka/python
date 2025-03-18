'''
Homework20
Name:   Jesse Brennecka
github link: https://github.com/jbrennecka/python/blob/main/homework20.py
'''

def convert_to_ascii(string):
    if len(string) == 1:
        print(ord(str(string)))
    else:
        lst = []
        for i in string:
            lst.append(ord(str(i)))
        print(lst)
    
def filter_non_ascii(string):
    if len(string) == 1:
        if str(string).isprintable():
            print(string)
    else:
        p = ""
        for i in str(string):
            if ord(i) < 126 and ord(i) > 31:
                p += i
        print(p)    

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest20.py'))
