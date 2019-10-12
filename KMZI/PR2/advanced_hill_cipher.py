import math as m
import numpy as np
from sympy import Matrix


ALPHABET = ['a', 'b', 'c', 'd', 
            'e', 'f', 'g', 'h', 
            'i', 'j', 'k', 'l', 
            'm', 'n', 'o', 'p',  
            'q', 'r', 's', 't', 
            'u', 'v', 'w', 'x', 
            'y', 'z', ' ', ',',
            '.']

POWER = len(ALPHABET)


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


def getNewKey(key2, key1):
    return np.matmul(key2, key1)


def getNewInverseKey(inv_key1, inv_key2):
    return np.matmul(inv_key1, inv_key2)


while True:
    plaintext = input("Input your text: ")
    key = input("Input your key: ")

    textMatrix = np.array(getPlainMatrix(plaintext, len(key)))
    print("Plain text matrix is\n", textMatrix)

    keyMatrix = np.array(getMatrix2(key))
    print("\nKey matrix is\n", keyMatrix)

    if keyMatrix.shape[0] != keyMatrix.shape[1]:
        print("\nError: key must be square matrix\n")
    else:
        break

encryptedText = hillEncrypt(textMatrix, keyMatrix)

print("Encrypted text: {0}".format(encryptedText))

encryptedMatrix = np.array(getMatrix(encryptedText))

decryptedText = hillDecrypt(encryptedMatrix, keyMatrix)

print("Decrypted text: {0}".format(decryptedText))