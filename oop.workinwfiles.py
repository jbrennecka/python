'''
Name: Jesse Brennecka
Object Oriented Programming: Working With Real Files
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