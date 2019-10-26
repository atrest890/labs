import math as m

ALPHABET = ['a', 'b', 'c', 'd', 
            'e', 'f', 'g', 'h', 
            'i', 'j', 'k', 'l', 
            'm', 'n', 'o', 'p',  
            'q', 'r', 's', 't', 
            'u', 'v', 'w', 'x', 
            'y', 'z']


NEW_ALPHABET = []

def get_new_alphabet(alpha, beta):
    for index in range(len(ALPHABET)):
        NEW_ALPHABET.append( ALPHABET[ (alpha * index + beta) % len(ALPHABET) ] )
    return NEW_ALPHABET


def affine_cipher(plaintext, alpha, beta):
    plaintext = plaintext.lower()
    NEW_ALPHABET = get_new_alphabet(alpha, beta)
    ciphertext = ''
    for symbol in plaintext:
        if symbol.isalpha():
            ciphertext += NEW_ALPHABET[ ALPHABET.index(symbol) ]
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
            deciphertext += NEW_ALPHABET[ ( ( NEW_ALPHABET.index(symbol) - beta ) * modulo ) % len(ALPHABET) ]
        else:
            deciphertext += symbol

    return deciphertext



while True:
    alpha = int(input("Input alpha: "))
    beta = int(input("Input beta: "))

    if alpha > 25 or alpha < 1 or m.gcd(len(ALPHABET), alpha) != 1:
        print("\nError: Alphabet power and alpha key are not coprime. Available alpha values: 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23 and 25\n")
    else:
        break
    

# for file

# f = open('plaintext', 'r')

# plaintext = f.read()

# print("\n----------TEXT----------:\n")
# print(plaintext)

# ciphertext = affine_cipher(plaintext, alpha, beta)
# print("\n----------ENCRYPTED TEXT:----------\n", ciphertext)

# deciphertext = affine_dechipher(ciphertext, alpha, beta)
# print("\n----------DECRYPTED TEXT:----------\n\n", deciphertext)

# f.close()

# f = open('ciphertext', 'w')
# f.write(ciphertext)


# for console

plaintext = input("Input your text: ")
ciphertext = affine_cipher(plaintext, alpha, beta)
print("Encrypted text: {0}".format(ciphertext))
encypted_text = affine_dechipher(ciphertext, alpha, beta)
print("Decrypted text: {0}".format(encypted_text))
