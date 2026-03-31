import math

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

def main():
    text = input("Enter text: ")
    cols = int(input("Enter columns: "))
    cipher = encrypt_route_cipher(text, cols)
    print("Ciphertext:", cipher)
    plain = decrypt_route_cipher(cipher, cols)
    print("Decrypted:", plain)

if __name__ == "__main__":
    main()
