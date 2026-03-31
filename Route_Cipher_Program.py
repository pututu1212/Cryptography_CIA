import math
import hashlib

def hash_text(text):
    return hashlib.sha256(text.encode()).hexdigest()

def encrypt_route_cipher(text, cols):
    if cols <= 0:
        raise ValueError("Columns must be positive.")

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

def decrypt_route_cipher(cipher, cols):
    if cols <= 0:
        raise ValueError("Columns must be positive.")

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

def main():
    text = input("Enter text: ")
    cols = int(input("Enter columns: "))

    # Hash before encryption
    original_hash = hash_text(text)

    cipher = encrypt_route_cipher(text, cols)
    print("Ciphertext:", cipher)

    decrypted = decrypt_route_cipher(cipher, cols)
    print("Decrypted:", decrypted)

    # Hash after decryption
    decrypted_hash = hash_text(decrypted)

    print("Original Hash :", original_hash)
    print("Decrypted Hash:", decrypted_hash)

    if original_hash == decrypted_hash:
        print("Integrity Verified ✅")
    else:
        print("Integrity Compromised ❌")

if __name__ == "__main__":
    main()
