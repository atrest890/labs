from math import sqrt
from numpy.linalg import inv
from numpy import matmul
from numpy import remainder
from numpy import array
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

def addSymbols(text, size):
    while sqrt(len(text)) != size:
        text += ALPHABET[-1]

    return text

def fromTextToMatrix(text):
    n = int(sqrt(len(text)))
    matrix = []

    for pos in range(0, len(text), n):
        matrix.append([ALPHABET.index(x) for x in text[pos:pos+n]])

    return array(matrix)


def getNewKey(key2, key1):
    return matmul(key2, key1)


def getNewInverseKey(key1, key2):
    return array(Matrix(matmul(key1, key2)).inv_mod(POWER), dtype=int)


def fromMatrixToText(matrix):
    return ''.join([x for x in array(matrix).flatten()])


def encrypt(text, key1, key2):
    key1, key2 = fromTextToMatrix(key1), fromTextToMatrix(key2)
    matrix = fromTextToMatrix(text)
    new_matrix = []

    n = int(sqrt(len(text)))

    for i in range(0, n):
        if i == 0:
            new_block = matmul(key1, matrix[0])

        elif i == 1:
            new_block = matmul(key2, matrix[1])

        else:
            new_key = getNewKey(key2, key1)
            new_block = matmul(new_key, matrix[i])
            key1 = key2
            key2 = new_key

        new_block = remainder(new_block, POWER)
        new_matrix.append([ALPHABET[i] for i in new_block])

    return fromMatrixToText(new_matrix)

def to_array(matrix):
    return array(matrix, dtype=int)

def inv_mod(matrix):
    return array(matrix.inv_mod(POWER), dtype=int)

def decrypt(text, key1, key2):
    key1 = Matrix(fromTextToMatrix(key1))
    key2 = Matrix(fromTextToMatrix(key2))
    matrix = fromTextToMatrix(text)
    new_matrix = []

    n = int(sqrt(len(text)))

    for i in range(0, n):
        if i == 0:
            new_block = matmul(inv_mod(key1), matrix[0])
        elif i == 1:
            new_block = matmul(inv_mod(key2), matrix[1])
        else:
            new_key = Matrix(getNewKey(to_array(key2), to_array(key1)))
            new_block = matmul(inv_mod(new_key), matrix[i])
            key1 = key2
            key2 = new_key

        new_block = remainder(new_block, POWER)
        new_matrix.append([ALPHABET[i] for i in new_block])

    return fromMatrixToText(new_matrix)


plaintext = input("Input your text: ")
key1 = input("Input your first key: ")
key2 = input("Input your second key: ")

encrypted_text = encrypt(plaintext, key1, key2)

print("Encrypted text: {0}".format(encrypted_text))

decrypted_text = decrypt(encrypted_text, key1, key2)

print("Decrypted text: {0}".format(decrypted_text))