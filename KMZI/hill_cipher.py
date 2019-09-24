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


def getMatricesFromPlaintext(plaintext, key_size):
    matrices = []
    n = m.sqrt(key_size)

    while int( len(plaintext) / key_size ) == 0:
        plaintext.append( ALPHABET[28] )

    for symbol in plaintext:
        row = []
        i = 0

        while i != n:
            row.append( ALPHABET.index(symbol) )
            i += 1
        
        matrices.append(row)

    return matrices


def getKeyMatrix(key):
    n = m.sqrt( len(key) ) # matrix size
    matrix = []

    for value in key:
        row = []
        i = 0
        while i != n:
            row.append( ALPHABET.index(value) )
            i += 1
        matrix.append(row)

    return np.array(matrix, dtype=int)


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




