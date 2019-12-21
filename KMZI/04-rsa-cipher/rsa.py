ALPHABET = ['a', 'b', 'c', 'd', 
            'e', 'f', 'g', 'h', 
            'i', 'j', 'k', 'l', 
            'm', 'n', 'o', 'p',  
            'q', 'r', 's', 't', 
            'u', 'v', 'w', 'x', 
            'y', 'z']


def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y


def euler(p, q):
    return (p-1) * (q-1)


def generate_keys():
    p = int(input("Input p: "))
    q = int(input("Input q: "))
    n = p*q
    f = euler(p, q)
    print("Euler function value: {0}".format(f))
    e = int(input("Input e. Recommended values are 3, 17, 65537: "))
    d, x, y  = egcd(e, f)
    return ((e, n), (x % f, n))


def encrypt(text, public_key):
    e, n = public_key
    text = (text ** e) % n
    new_text = [(x**e) % n for x in text]
    return new_text

text = int(input("Input your text: "))

public_key, private_key = generate_keys()

print("Public key:\t{0}\nPrivate key:\t{1}".format(public_key, private_key))

encrypted_text = encrypt(text, public_key)

print("Encrypted text: ", encrypted_text)