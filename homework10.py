'''
Homework10
Name: Jesse Brennecka
github link: https://github.com/jbrennecka/python/edit/main/homework10.py
'''


def find_missing_number(lst):
    x = 0
    llst = lst[:]
    llst.sort()
    nlst = []
    for i in llst:
        while x <= i:
            if x in llst:
                x += 1
            else:
                nlst.append(x)
                x += 1
            
    print(nlst)
    return 

def even_partition(lst):
    x = 0
    xlst = lst[:]
    ylst = []
    for x in xlst:
        if x % 2 == 0:
            ylst.append(x)
            x += 1
        else:
            x += 1
    print(ylst)
    return

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest10.py'))
