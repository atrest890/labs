ALPHABET = ['a', 'b', 'c', 'd', 
            'e', 'f', 'g', 'h', 
            'i', 'j', 'k', 'l', 
            'm', 'n', 'o', 'p',  
            'q', 'r', 's', 't', 
            'u', 'v', 'w', 'x', 
            'y', 'z']

LENGTH = len(ALPHABET)

def tabula_recta():
    square = []
    for i in range(LENGTH, 0, -1):
        square.append([ALPHABET[LENGTH-i:] + ALPHABET[:-i]])

    return square

def key(text, key_word):
    n = len(key_word)
    for i in range(n, len(text)):
        key_word += key_word[i%n]

    return key_word
