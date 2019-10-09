import math as m

ALPHABET = ['a', 'b', 'c', 'd', 
            'e', 'f', 'g', 'h', 
            'i', 'j', 'k', 'l', 
            'm', 'n', 'o', 'p',  
            'q', 'r', 's', 't', 
            'u', 'v', 'w', 'x', 
            'y', 'z']


NEW_ALPHABET = {}


def affine_cipher(plaintext, alpha1, alpha2, beta1, beta2):
    plaintext = plaintext.lower()
    ciphertext = ''
    for index in range(len(plaintext)):
        if plaintext[index].isalpha():
            if index == 0:
                ciphertext += ALPHABET[ ( alpha1 * ALPHABET.index( plaintext[index] ) + beta1 ) % len(ALPHABET) ]
            elif index == 1:
                ciphertext += ALPHABET[ ( alpha2 * ALPHABET.index( plaintext[index] ) + beta2 ) % len(ALPHABET) ]
            else:
                alpha = (alpha1 * alpha2) % len(ALPHABET)
                beta = (beta1 + beta2) % len(ALPHABET)

                # print("alpha", index, " : ", alpha)
                # print("beta", index, " : ", beta)

                ciphertext += ALPHABET[ ( alpha * ALPHABET.index( plaintext[index] ) + beta ) % len(ALPHABET) ]

                # print(plaintext[index], "[", ALPHABET.index(plaintext[index]), "]", " -> ", ciphertext[index], "[", ALPHABET.index(ciphertext[index]), "]")

                alpha1 = alpha2
                alpha2 = alpha
                beta1 = beta2
                beta2 = beta
        else:
            ciphertext += plaintext[index]

    return ciphertext


def find_modulo(alpha):
    modulo = 1
    n = modulo * alpha
    while n % len(ALPHABET) != 1:
        modulo += 1
        n = modulo * alpha

    return modulo


def affine_dechipher(ciphertext, alpha1, alpha2, beta1, beta2):
    deciphertext = ''
    for index in range(len(ciphertext)):
        if ciphertext[index].isalpha():
            if index == 0:
                modulo = find_modulo(alpha1)

                deciphertext += ALPHABET[ ( ( ALPHABET.index(ciphertext[index]) - beta1 ) * modulo ) % len(ALPHABET) ]

                # print("(", ALPHABET.index(ciphertext[index]), " - ", beta1, ") * ", modulo)

            elif index == 1:
                modulo = find_modulo(alpha2)

                deciphertext += ALPHABET[ ( ( ALPHABET.index(ciphertext[index]) - beta2 ) * modulo ) % len(ALPHABET) ]

                # print("(", ALPHABET.index(ciphertext[index]), " - ", beta2, ") * ", modulo)

            else:
                alpha = (alpha1 * alpha2) % len(ALPHABET)
                beta = (beta1 + beta2) % len(ALPHABET)

                modulo = find_modulo(alpha)

                deciphertext += ALPHABET[ ( ( ALPHABET.index(ciphertext[index]) - beta ) * modulo ) % len(ALPHABET) ]

                # print("(", ALPHABET.index(ciphertext[index]), " - ", beta, ") * ", modulo)

                alpha1 = alpha2
                alpha2 = alpha
                beta1 = beta2
                beta2 = beta
        else:
            deciphertext += ciphertext[index]

    return deciphertext


# f = open('plaintext', 'r')

while True:
    alpha1 = int(input("Input alpha1: "))
    alpha2 = int(input("Input alpha2: "))

    beta1 = int(input("Input beta1: "))
    beta2 = int(input("Input beta2: "))
    if alpha1 > 25 or alpha2 < 0 or alpha2 > 25 or alpha2 < 0 or m.gcd(len(ALPHABET), alpha1) != 1 or m.gcd(len(ALPHABET), alpha2) != 1:
        print("\nError: Alphabet power and alpha key are not coprime. Available alpha values: 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23 and 25\n")
    else:
        break


plaintext = input("Input your text: ")
ciphertext = affine_cipher(plaintext, alpha1, alpha2, beta1, beta2)
print("Encrypted text: ", ciphertext)

deciphertext = affine_dechipher(ciphertext, alpha1, alpha2, beta1, beta2)
print("Decrypted text: ", deciphertext)
