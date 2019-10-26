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

    return array(matrix, dtype=int)


def to_text(matrix):
    return ''.join([ALPHABET[x] for x in array(matrix).flatten()])


def encrypt(text, key):
    n = int(sqrt(len(key)))
    matrix = to_matrix(text, n)
    key = to_matrix(key, n)
    new_matrix = []
    m = len(text) // n

    for i in range(0, m):
        new_block = remainder(matmul(key, matrix[i]), LENGTH)

        # print("Block {0}:\n{1}".format(i, new_block))

        new_matrix.append(new_block)

    return to_text(array(new_matrix, dtype=int))


def decrypt(text, key):
    n = int(sqrt(len(key)))
    matrix = to_matrix(text, n)

    # print("Matrix:\n", matrix)

    key = to_matrix(key, n)
    inv_key = array(Matrix(key).inv_mod(LENGTH), dtype=int)
    new_matrix = []
    m = len(text) // n
    
    for i in range(0, m):
        new_block = remainder(matmul(inv_key, matrix[i]), LENGTH)

        # print("Block {0}:\n{1}".format(i, new_block))

        new_matrix.append(new_block)

    return to_text(array(new_matrix, dtype=int))


text = input("Input your text: ")
while (True):
    key = input("Input your key: ")
    n = sqrt(len(key))

    if not n.is_integer():
        print("\nError: The key is nonsquare\n")
        continue

    n = int(n)

    try:
        Matrix(to_matrix(key, n)).inv()

    except ValueError:
        print("\nError: the key matrix has det = 0; not invertible\n")
        continue


    if not is_multiple(text, n):
        text = lengthen(text, n)

    break

encrypted_text = encrypt(text, key)

print("Encrypted text: {0}".format(encrypted_text))

decrypted_text = decrypt(encrypted_text, key)

print("Decrypted text: {0}".format(decrypted_text))
