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


LENGTH = len(ALPHABET)


def is_multiple(text, n):
    return len(text) % n == 0


def lengthen(text, n):
    while len(text) % n != 0:
        text += ALPHABET[-1]

    return text


def to_matrix(text, n):
    matrix = []

    for pos in range(0, len(text), n):
        matrix.append([ALPHABET.index(x) for x in text[pos:pos+n]])

    return array(matrix)


def new_key(key2, key1):
    return matmul(key2, key1)


def new_inv_key(key1, key2):
    return array(Matrix(matmul(key1, key2)).inv_mod(LENGTH), dtype=int)


def to_text(matrix):
    return ''.join([x for x in array(matrix).flatten()])


def encrypt(text, key1, key2):
    n = int(sqrt(len(key1)))
    key1, key2 = to_matrix(key1, n), to_matrix(key2, n)

    matrix = to_matrix(text, n)

    new_matrix = []

    m = len(text) // n

    for i in range(0, m):
        if i == 0:
            new_block = matmul(key1, matrix[0])

        elif i == 1:
            new_block = matmul(key2, matrix[1])

        else:
            key_i = new_key(key2, key1)
            new_block = matmul(key_i, matrix[i])
            key1 = key2
            key2 = key_i

        new_block = remainder(new_block, LENGTH)

        new_matrix.append([ALPHABET[i] for i in new_block])

    return to_text(new_matrix)


def to_array(matrix):
    return array(matrix, dtype=int)


def inv_mod(matrix):
    return array(matrix.inv_mod(LENGTH), dtype=int)


def decrypt(text, key1, key2):
    n = int(sqrt(len(key1)))
    key1 = Matrix(to_matrix(key1, n))
    key2 = Matrix(to_matrix(key2, n))
    matrix = to_matrix(text, n)
    new_matrix = []

    # print("C Matrix:\n{0}".format(matrix))

    n = int(sqrt(len(key1)))
    m = len(text) // n

    for i in range(0, m):
        if i == 0:
            new_block = matmul(inv_mod(key1), matrix[0])
            # print("Key {0}:\n{1}".format(i, inv_mod(key1)))
        elif i == 1:
            new_block = matmul(inv_mod(key2), matrix[1])
            # print("Key {0}:\n{1}".format(i, inv_mod(key2)))
        else:
            key_i = Matrix(new_key(to_array(key2), to_array(key1)))
            new_block = matmul(inv_mod(key_i), matrix[i])
            key1 = key2
            key2 = key_i

            # print("Key {0}:\n{1}".format(i, inv_mod(key_i)))

        new_block = remainder(new_block, LENGTH)

        # print("Block {0}:\n{1}".format(i, new_block))

        new_matrix.append([ALPHABET[i] for i in new_block])

    # print("P Matrix:\n{}".format(new_matrix))

    return to_text(new_matrix)


text = input("Input your text: ")
while (True):
    key1 = input("Input your first key: ")
    n1 = sqrt(len(key1))

    if not n1.is_integer():
        print("\nError: The first key length must have whole square\n")
        continue

    key2 = input("Input your second key: ")
    n2 = sqrt(len(key2))

    if not n2.is_integer():
        print("\nError: The second key length must have whole square\n")
        continue

    n1, n2  = int(n1), int(n2)

    if len(key1) != len(key2):
        print("\nError: keys have different length\n")
        continue

    try:
        Matrix(to_matrix(key1, n1)).inv()

    except ValueError:
        print("\nError: the first key matrix has det = 0; not invertible\n")
        continue

    try:
        Matrix(to_matrix(key2, n2)).inv()

    except ValueError:
        print("\nError: the second key matrix has det = 0; not invertible\n")
        continue


    if not is_multiple(text, n1):
        text = lengthen(text, n2)

    break

encrypted_text = encrypt(text, key1, key2)

print("Encrypted text: {0}".format(encrypted_text))

decrypted_text = decrypt(encrypted_text, key1, key2)

print("Decrypted text: {0}".format(decrypted_text))