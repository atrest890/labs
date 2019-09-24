import math as m
import numpy as np

ALPHABET = ['a', 'b', 'c', 'd', 
            'e', 'f', 'g', 'h', 
            'i', 'j', 'k', 'l', 
            'm', 'n', 'o', 'p',  
            'q', 'r', 's', 't', 
            'u', 'v', 'w', 'x', 
            'y', 'z', '.', ',',
            ' ']

POWER = len(ALPHABET)

def getListFromStr(string):
    return [x for x in string]
    

def getKeyMatrix(key):
    n = m.sqrt( len(key) ) # matrix size

    matrix = []

    for value in key:
        row = []
        i = 0
        while i != n:
            row.append(value)
            i += 1
        matrix.append(row)

    


def hillEncrypt(plaintext, key):
    pass



def hillDecrypted():
    pass


plaintext = ''
key = ''


while True:
    input("Input your text: ", plaintext)
    input("Input your key: ", key)

    if m.sqrt(key) - int(m.sqrt(key)) != 0:
        print("\nError: the length of your key is invalid - it must be a value from which the root can be extracted\n")
    else:
        break

# encrypedText = hillEncrypt(plaintext, key)




