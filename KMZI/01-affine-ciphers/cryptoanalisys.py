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



plaintext = 'analysis'

ciphertext = affine_cipher(plaintext, 5, 7, 2, 4)

temp = plaintext

i = 1

while ciphertext != plaintext:
    ciphertext = affine_cipher(temp, 5, 7, 2, 4)
    temp = ciphertext
    print('[{0}]: {1}'.format(i, ciphertext))
    i += 1
    