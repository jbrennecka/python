'''
Homework24
Name:   Jesse Brennecka
github link: https://github.com/jbrennecka/python/blob/main/homework26.py
'''

def dictionary_exceptions(key,dict):
    try:
        print("The price of " + key +" is $" + str(dict[key]))
    except KeyError:
        print("Error: Flower not found! Please enter Rose, Lily, or Tulip.")

def string_exceptions(idx,str):
    try:
        x = str[idx]
        print("The character at index", idx, "is:", x)
    except ValueError:
        print("Error: Please enter a valid number for the index.")
    except IndexError:
        print("Error: Index out of range! Please enter a valid index.")
    except TypeError:
        print("Error: String indices must be integers, not '"+ type(idx).__name__+ "'")


if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest26.py'))
