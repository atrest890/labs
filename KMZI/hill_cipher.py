import math as m
import numpy as np

ALPHABET = ['a', 'b', 'c', 'd', 
            'e', 'f', 'g', 'h', 
            'i', 'j', 'k', 'l', 
            'm', 'n', 'o', 'p',  
            'q', 'r', 's', 't', 
            'u', 'v', 'w', 'x', 
            'y', 'z', ' ', ',',
            '.']

POWER = len(ALPHABET)


def getListFromStr(string):
    return [x for x in string]


def getPlainMatrix(plaintext, key_size):
    matrix = []
    n = int( m.sqrt(key_size) )

    index1 = 0
    index2 = n

    while int( len(plaintext) / key_size ) == 0:
        plaintext += ALPHABET[26]

    while index1 != len(plaintext):
        matrix.append( [ ALPHABET.index(x) for x in plaintext[index1 : index2] ] )
        index1 = index2
        index2 += n

    return matrix


def getKeyMatrix(key):
    n = int( m.sqrt( len(key) ) )
    matrix = []

    index1 = 0
    index2 = n

    while index1 != len(key):
        matrix.append( [ ALPHABET.index(x) for x in key[index1 : index2] ] )
        index1 = index2
        index2 += n

    return matrix


def hillEncrypt(plaintext, key):
    key_matrix = getKeyMatrix(key)
    plain_matrix = getPlainMatrix(plaintext, len(key))
    encrypted_text = ''

    for row in plain_matrix:
        mult_matrix = np.dot(key_matrix, row)
        new_matrix = [x % POWER for x in mult_matrix]
        encrypted_text += ''.join( [ALPHABET[x] for x in new_matrix] )
        
    return encrypted_text


def hillDecrypted():
    pass


plaintext = ''
key = ''


while True:
    plaintext = input("Input your text: ")
    key = input("Input your key: ")

    if m.sqrt( len(key) ) - int( m.sqrt( len(key) ) ) != 0:
        print("\nError: the length of your key is invalid - it must be a value from which the root can be extracted\n")
    else:
        break

encrypedText = hillEncrypt(plaintext, getListFromStr(key))

print( "Encrypted text: {0}".format(encrypedText) )




