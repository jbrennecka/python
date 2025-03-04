'''
Homework17
Name: Jesse Brennecka
github link:
'''


def frequency_counter(lst):
    count = {}
    for x in lst:
        if x in count:
            count[x]+=1
        else:
            count[x]=1
    return count

def translation(english_words):
    A = 'Alfa'
    B = 'Bravo'
    C = 'Charlie'
    D = 'Delta'
    E = 'Echo'
    F = 'Foxtrot'
    G = 'Golf'
    H = 'Hotel'
    I = 'India'
    J = 'Juliette'
    K = 'Kilo'
    L = 'Lima'
    M = 'Mike'
    N = 'November'
    O = 'Oscar'
    P = 'Papa'
    Q = 'Quebec'
    R = 'Romeo'
    S = 'Sierra'
    T = 'Tango'
    U = 'Uniform'
    V = 'Victor'
    W = 'Whiskey'
    XX = 'X-Ray'
    Y = 'Yankee'
    Z = 'Zulu'
                        # 'XX' was used to better tell which variable was being used
                        #  Also, alpha was spelled wrong, it is not 'alfa'
    for x in english_words:
        if x == 'A' or x == 'a':
            print(A)
        elif x == 'B' or x == 'b':
            print(B)
        elif x == 'C' or x == 'c':
            print(C)
        elif x == 'D' or x == 'd':
            print(D)
        elif x == 'E' or x == 'e':
            print(E)
        elif x == 'F' or x == 'f':
            print(F)
        elif x == 'G' or x == 'g':
            print(G)
        elif x == 'H' or x == 'h':
            print(H)
        elif x == 'I' or x == 'i':
            print(I)
        elif x == 'J' or x == 'j':
            print(J)
        elif x == 'K' or x == 'k':
            print(K)
        elif x == 'L' or x == 'l':
            print(L)
        elif x == 'M' or x == 'm':
            print(M)
        elif x == 'N' or x == 'n':
            print(N)
        elif x == 'O' or x == 'o':
            print(O)
        elif x == 'P' or x == 'p':
            print(P)
        elif x == 'Q' or x == 'q':
            print(Q)
        elif x == 'R' or x == 'r':
            print(R)
        elif x == 'S' or x == 's':
            print(S)
        elif x == 'T' or x == 't':
            print(T)
        elif x == 'U' or x == 'u':
            print(U)
        elif x == 'V' or x == 'v':
            print(V)
        elif x == 'W' or x == 'w':
            print(W)
        elif x == 'X' or x == 'x':
            print(XX)
        elif x == 'Y' or x == 'y':
            print(Y)
        elif x == 'Z' or x == 'z':
            print(Z)
    return 

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest17.py'))