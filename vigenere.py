
#Input text L, and A: a string of the 26 letters in the order such that a is
# replaced by A[0], b by A[1] , and so on to z being replaced by A[25]
def vigenere(L,A):
    P = ''' !()-[]{};:'"\,<>./?@#$%^&*_~'''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    char=list(L.lower())
    text=[]
    t=''
    for i in L:
        if i in P:
            text.append(i)
        else:
            text.append(A[int(alphabet.index(i.lower()))])
    for i in text:
        t+=i
    return t

# example print(vigenere('my vigenere code cipher','qwertyuiopasdfghjklzxcvbnm'))
def reverse_vigenere(L,A):
    P = ''' !()-[]{};:'"\,<>./?@#$%^&*_~'''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    char=list(L.lower())
    text=[]
    t=''
    for i in L:
        if i in P:
            text.append(i)
        else:
            text.append(alphabet[int(A.index(i.lower()))])
    for i in text:
        t+=i
    return t
