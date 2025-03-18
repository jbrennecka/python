'''
Homework23
Name:   Jesse Brennecka
github link: 
'''

def group_by_first_letter(words):
    d = {}
    for w in words:
        if w[0] in d.keys():
            ins = d[w[0]]
            ins.append(w)
            d.update({w[0]: ins})
        else:
            ins = [w]
            d.update({w[0]: ins})
    print(d)

def convert_to_sentence(words):
    sent = ''
    for w in words:
        if w == words[-1]:
            sent = sent + w + '.'
        else:
            sent = sent + w + ' '
    print('\'' + sent + '\'')


if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest23.py'))