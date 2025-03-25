'''
Homework24
Name:   Jesse Brennecka
github link: 
'''

def is_valid_password(word):
    spec = "!@#$%&*"
    ifOneUpper = False
    ifOneLower = False
    ifOneDigit = False
    ifSpecChar = False
    if len(word) > 8 or len(word) < 20:
        for x in word:
            if x.isupper():
                ifOneUpper = True
            if x.islower():
                ifOneLower = True
            if x.isdigit():
                ifOneDigit = True
            if x in spec:
                ifSpecChar = True
                
    if ifOneLower == True and ifOneUpper == True and ifOneDigit == True and ifSpecChar == True:
        return True
    else:
        return False        
        
if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest24.py'))