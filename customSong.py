'''
AdLibs program
When the program runs, the program will ask for input from the user
 - Jesse Brennecka
 - github: https://github.com/jbrennecka/python/blob/main/customSong.py
'''

action = input("Please enter an action that ends in -ing': ")
obj = input("Please enter an object: ")
action_1 = input("Please enter another action that ends in -ing: ")
noun = input("Please enter a plural noun: ")
adv = input("Please enter an adverb: ")
obj_1 = input("Please enter another object: ")
adv_1 = input("Please enter another adverb: ")
noun_1 = input("Please enter another plural noun: ")


def custom_song(action, obj, noun, adv, action_1, obj_1, noun_1, adv_1):
    '''The original lyrics are from the song 'Counting Stars', By OneRepublic.'''

    line_1 = f"Lately, I been, I been {action} sleep"
    line_2 = f"Dreaming about the {obj} that we could be"
    line_3 = f"But, {noun}, I been, I been praying {adv}"
    line_4 = f"Said, \"No more counting {noun_1}, we\'ll be counting {obj_1}\""
    line_5 = f"Lately, I been, I been {action_1} sleep"
    line_6 = f"Dreaming about the {obj} that we could be"
    line_7 = f"But, {noun}, I been, I been praying {adv_1}"
    line_8 = f"Said, \"No more counting {noun_1}, we\'ll be counting {obj_1}\""
    line_9 = f"Yeah, we\'ll be counting {obj_1}"

    print(line_1, "\n", line_2, "\n", line_3, "\n", line_4, "\n", line_5, "\n", line_6, "\n", line_7, "\n", line_8, "\n", line_9)

custom_song(action, obj, noun, adv, action_1, obj_1, noun_1, adv_1)
