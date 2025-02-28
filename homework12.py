'''
Homework12
Name: Jesse Brennecka
github link: https://github.com/jbrennecka/python/blob/main/homework12.py
'''

def rectangle(w, h):
    a = w * h
    print('\'The area of the rectangle is', str(a), 'square units\'')

def circle(rad):
    a = 3.14 * rad * rad
    format_a = f"{a:.2f}"
    format_a = float(format_a)
    format_a = f"{format_a:g}"
    print('\'The area of a circle is', str(format_a), 'square units\'')

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest12.py'))
