'''
Homework14
Name: Jesse Brennecka
github link: https://github.com/jbrennecka/python/blob/main/homework14.py
'''

meter = 0
kg = 0

def convert_to_kg(lbs):
    kg = round((lbs * 0.453592), 2)
    return kg

def convert_to_meters(inches):
    meter = round((inches * 0.0254), 2)
    return meter

def bmi_calculation(lbs,height):
    bmi = convert_to_kg(lbs) / (convert_to_meters(height) * convert_to_meters(height))
    if bmi < 18.5:
        print("\"underweight\"")
    elif bmi > 18.5 and bmi < 24.9:
        print("\"normal weight\"")
    elif bmi > 24.9 and bmi < 29.9:
        print("\"overweight\"")
    else:
        print("\"obese\"")
    return

#   I must mention that the test wouldn't pass unless I added the \" for the bmi_calculation function
#   first attempt only returned the string necessary, but it didn't have "" but ''
#   second attempt only returned the word, no string indicators (no "", no '')

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest14.py'))
