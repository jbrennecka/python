'''
Name: Jesse Brennecka
Object Oriented Programming: Processing Files
github: https://github.com/jbrennecka/python/blob/main/personal_diary.py
Notes:
    When creating this, I was wondering if I needed to catch if the entries for the dates and time-of-day can be anything,
    although wouldn't it be more efficient to make the computer itself enter the time of day and the date of the entry being placed?
    Either way, this program does not check if the entries are dates and times, but they are saved onto different lines 
    and has a trailing empty line for each entry.
'''
class fileNotFound(Exception):
    def __init__(self, mssg):
        self.mssg = mssg

def main():
    #
    tod = input("Please enter the time of day: \n")
    date = input("Please enter the date: \n")
    entry = input("Please type in your entry:\n")

    try:
        fle = open('diary.txt', '+a')
        diaryEntry = f"Time of day: {tod}\nDate of entry: {date}\nEntry:\n\t{entry}\n\n"
        fle.write(diaryEntry)
        fle.close()
        pass
    except Exception:
        print("file does not exist, so one was created")
        fle = open('diary.txt', 'x')
        diaryEntry = f"Time of day: {tod}\nDate of entry: {date}\nEntry:\n\t{entry}"
        fle.write(diaryEntry)
        fle.close()
        pass
    print("entry has been saved.")

main()
