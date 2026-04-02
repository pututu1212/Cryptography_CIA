import math


# Custom Hash Function
def custom_hash(text):
    hash_value = 0
    for i in range(len(text)):
        hash_value += (i + 1) * ord(text[i])
    return hash_value % 100000


# Encryption (Route Cipher)
def encrypt_route_cipher(text, cols):
    text = text.replace(" ", "").upper()
    rows = math.ceil(len(text) / cols)

    matrix = [['X' for _ in range(cols)] for _ in range(rows)]
    k = 0

    for i in range(rows):
        for j in range(cols):
            if k < len(text):
                matrix[i][j] = text[k]
                k += 1

    cipher = ""
    for j in range(cols):
        for i in range(rows):
            cipher += matrix[i][j]

    return cipher


# Decryption (Route Cipher)
def decrypt_route_cipher(cipher, cols):
    rows = math.ceil(len(cipher) / cols)

    matrix = [['' for _ in range(cols)] for _ in range(rows)]
    k = 0

    for j in range(cols):
        for i in range(rows):
            if k < len(cipher):
                matrix[i][j] = cipher[k]
                k += 1

    text = ""
    for i in range(rows):
        for j in range(cols):
            text += matrix[i][j]

    return text.rstrip('X')



# MAIN
if __name__ == "__main__":

    plaintext = "Affine Cipher Test"
    cols = 4

    original_hash = custom_hash(plaintext)

    cipher = encrypt_route_cipher(plaintext, cols)
    decrypted = decrypt_route_cipher(cipher, cols)

    decrypted_hash = custom_hash(decrypted)

    print("Plaintext       :", plaintext)
    print("Original Hash   :", original_hash)
    print("Ciphertext      :", cipher)
    print("Decrypted Text  :", decrypted)
    print("Decrypted Hash  :", decrypted_hash)

    if original_hash == decrypted_hash:
        print("Integrity Check : SUCCESS")
    else:
        print("Integrity Check : FAILED")
