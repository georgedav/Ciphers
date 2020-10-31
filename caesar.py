def caesar(text,shift):
    alphabet='abcdefghijklmnopqrstuvwxyz'
    P= ''' !()-[]{};:'"\,<>./?@#$%^&*_~'''
    A=[]
    L=list(text)
    for i in L:
        if i in P:
            A.append(i)
        else:
            A.append(alphabet[(shift + alphabet.index(i)) % 26])
    text=''
    for i in A:
        text+=i
    return text

#example print(caesar('How are you?',9))
