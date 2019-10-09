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

def extendedEuclid(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = extendedEuclid(b % a, a)
        return (g, y - (b // a) * x, x)


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


def hillEncrypt(plaintext, key):
    key_matrix = getMatrix2(key)
    plain_matrix = getPlainMatrix(plaintext, len(key))
    encrypted_text = ''

    encrypted_matrix = np.matmul(plain_matrix, key_matrix)
    encrypted_matrix = np.remainder(encrypted_matrix, POWER)

    for row in encrypted_matrix:
        for i in row:
            encrypted_text = ALPHABET[i]

    # for row in plain_matrix:
    #     mult_matrix = np.dot(key_matrix, row)
    #     new_matrix = [x % POWER for x in mult_matrix]
    #     encrypted_text += ''.join( [ALPHABET[x] for x in new_matrix] )
        
    return encrypted_text


def hillDecrypt(encryptedText, key):
    encrypted_matrix = getMatrix2(encryptedText)
    key_inv_matrix = np.linalg.inv( getMatrix2(key) )
    temp = np.dot(key_inv_matrix, encrypted_matrix)
    decrypted_matrix = [ (x % POWER).astype(int) for x in temp ]

    decrypted_text = ''
    for row in decrypted_matrix:
        mult_matrix = np.dot(key_inv_matrix, row)
        new_matrix = [x % POWER for x in mult_matrix]
        decrypted_text = ''.join( [ALPHABET[x] for x in new_matrix] )

    return decrypted_text
    


plaintext = ''
key = ''


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

encryptedText = hillEncrypt(plaintext, key)

print("Encrypted text: {0}".format(encryptedText))

# decryptedText = hillDecrypt(encryptedText, getListFromStr(key))

# print("Decrypted text: {0}".format(decryptedText))




