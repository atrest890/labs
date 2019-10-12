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

def getMatrix(key):
    n = int( m.sqrt( len(key) ) )
    matrix = []

    index1 = 0
    index2 = n

    while index1 != len(key):
        matrix.append( [ ALPHABET.index(x) for x in key[index1 : index2] ] )
        index1 = index2
        index2 += n

    return matrix

def getMatrix2(key):
    n = int( m.sqrt( len(key) ) )
    matrix = []

    for pos in range(0, n):
        matrix.append( [ ALPHABET.index(x) for x in key[pos::n]] )

    return matrix


def getNewKey(key2, key1):
    return np.matmul(key2, key1)


def getNewInverseKey(inv_key1, inv_key2):
    return np.matmul(inv_key1, inv_key2)


def getInverseKey(key):
    inverseKey = Matrix(key).inv_mod(POWER)

    return np.array(inverseKey, dtype=int)

def hillEncrypt(textMatrix, keyMatrix):
    encMatrix = np.matmul(textMatrix, keyMatrix)
    encMatrix = np.remainder(encMatrix, POWER)

    encText = ''
    for row in encMatrix:
        encText += ''.join( [ALPHABET[i] for i in row] )

    return encText


def hillDecrypt(text, key):
    inverseKey = getInverseKey(key)
    decMatrix = np.matmul(text, inverseKey)
    decMatrix = np.remainder(decMatrix, POWER).flatten()
    
    return ''.join( [ALPHABET[i] for i in decMatrix] )


while True:
    plaintext = input("Input your text: ")
    key1 = input("Input your first key: ")
    key2 = input("Input your second key: ")

    textMatrix = np.array(getPlainMatrix(plaintext, len(key)))
    print("Plain text matrix is\n", textMatrix)

    keyMatrix1 = np.array(getMatrix2(key1))
    print("\nFirst key matrix is\n", keyMatrix1)

    keyMatrix2 = np.array(getMatrix2(key2))
    print("\nSecond key matrix is\n", keyMatrix2)


    if keyMatrix.shape[0] != keyMatrix.shape[1]:
        print("\nError: key must be square matrix\n")
    else:
        break

encryptedText = hillEncrypt(textMatrix, keyMatrix)

print("Encrypted text: {0}".format(encryptedText))

encryptedMatrix = np.array(getMatrix(encryptedText))

decryptedText = hillDecrypt(encryptedMatrix, keyMatrix)

print("Decrypted text: {0}".format(decryptedText))