ALPHABET = ['a', 'b', 'c', 'd', 
            'e', 'f', 'g', 'h', 
            'k', 'j', 'k', 'l', 
            'm', 'n', 'o', 'p',  
            'q', 'r', 's', 't', 
            'u', 'v', 'w', 'x', 
            'y', 'z']


NEW_ALPHABET = []

def get_new_alphabet(alpha, beta):
    for index in range(len(ALPHABET)):
        NEW_ALPHABET.append( ALPHABET[(alpha * index + beta) % len(ALPHABET)] )
        print(NEW_ALPHABET[index])
    return NEW_ALPHABET

def affine_cipher(plaintext, alpha, beta):
    NEW_ALPHABET = get_new_alphabet(alpha, beta)
    ciphertext = ''
    for symbol in plaintext:
        if symbol.isalpha():
            ciphertext += NEW_ALPHABET[ALPHABET.index(symbol)]
        else:
            ciphertext += symbol

    return ciphertext


def find_modulo(alpha):
    modulo = 1
    n = modulo * alpha
    while n % len(ALPHABET) != 1:
        modulo += 1
        n = modulo * alpha

    return modulo

def affine_dechipher(ciphertext, alpha, beta):
    modulo = find_modulo(alpha)
    deciphertext = ''
    for symbol in ciphertext:
        if symbol.isalpha():
            deciphertext += NEW_ALPHABET[ ( ( NEW_ALPHABET.index(symbol) - beta ) * modulo ) % len(ALPHABET)]
        else:
            deciphertext += symbol

    return deciphertext


alpha = int(input())
beta = int(input())

print("Alphabet: ")
for index in range(len(ALPHABET)):
    print(ALPHABET[index], end=" ")

plaintext = input()
ciphertext = affine_cipher(plaintext, alpha, beta)
print(ciphertext)

deciphertext = affine_dechipher(ciphertext, alpha, beta)
print(deciphertext)