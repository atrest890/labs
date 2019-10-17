# CRYPTOGRAPHIC METHODS OF INFORMATION SECURITY
This folder contains the following ciphers:
1. Affine cipher
2. Advanced Affine cipher
3. Hill cipher
4. Advanced Hill cipher

## Affine cipher
**Affine cipher** is a monoalphabetic substitution cipher. The cipher is less secure than a substitution cipher as it vulnerable to all the attacks that work against substitution ciphers, in addition to other attacks. The cipher's primary weakness comes from the fact that if the cryptanalyst can discover (by means of frequency analysis, brute force, guessing or otherwise) the plaintext of two ciphertext characters, then the key can be obtained by solving a simultaneous equation.  
  
The 'key' for the Affine cipher consists of 2 numbers, we'll call them a and b. The following discussion assumes the use of a 26 character alphabet (m = 26). a should be chosen to be relatively prime to m (i.e. a should have no factors in common with m). For example 15 and 26 have no factors in common, so 15 is an acceptable value for a, however 12 and 26 have factors in common (e.g. 2) so 12 cannot be used for a value of a. When encrypting, we first convert all the letters to numbers ('a'=0, 'b'=1, ..., 'z'=25). The ciphertext letter c, for any given letter p is (remember p is the number representing a letter):

## Advanced Affine cipher

## Hill cipher

## Advanced Hill cipher

## Vigenère cipher