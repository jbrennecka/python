'''
Name: Jesse Brennecka
Object Oriented Programming: Working With Real Files
github: https://github.com/jbrennecka/python/blob/main/oop.workinwfiles.py
Notes:
    A simple program, obviously, just to make sure we're able to read a file and manipulate the data within. I did
    notice, however, that when creating and testing the program, that the 'sales_totals.txt' file had to be outside of
    the folder that contained the .py file, or else it would continue to fail.
'''

def main():
    amt = 0
    avg = 0
    noOfLines = 0

    try:
        fle = open('sales_totals.txt', 'r')
        fleRead = fle.read()
        fle.close()
        fle = open('sales_totals.txt', 'r')
        fleLines = fle.readlines()
        for i in fleLines:
            i = i.replace('\n','')
            amt = amt + float(i)
            print('\t' + str(i) + '\n')
        noOfLines = fleRead.count('\n')
        avg = amt/noOfLines
        print(f"amount:\n{amt}\naverage:\n{avg}\nnumber of lines:\n{noOfLines}")
        fle.close()
    except:
        print('failed')
    pass

main()
