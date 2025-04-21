'''
Name: Jesse Brennecka
Object Oriented Programming: Generators, iterators, and closures
Notes: 
    When making this, I first off believed that you wanted a printout of a list containing the combinations, but as
    I kept looking at the assignment page, there was no clarification on if that is how I should turn it in or it 
    was another method. So, to be on the safe side, I made this program only return the combinations themselves,
    and not the list that I was creating before.

'''

def two_letter_combinations(char):
    #take one letter from list and add to other element of same list

    a = 0
    while a < len(char):
        b = 0
        while b < len(char):
            p = char[a]
            q = char[b]
            yield p+q
            b += 1
        a += 1
    
def main():
    #call generator func and print combos of vowels
    
    charList = ['a', 'e', 'i', 'o', 'u']
    getList = two_letter_combinations(charList)
    for num in getList:
        print(num)
    pass

main()