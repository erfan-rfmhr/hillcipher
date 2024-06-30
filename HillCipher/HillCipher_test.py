import numpy as np
from key_create import key_matrix_creator
# Function to convert the number matrix to their respective alphabet matrix
def matrix_to_letter(matrix):
    encrypted_string = ''
    for row in matrix:
        for num in row:
            encrypted_string += chr(num + 97)
    return encrypted_string

# Function for encryption
def encrypt(plaintext, key):
    word_list = plaintext.split(" ")    
    encrypted_message = ''
    
    for word in word_list:
        length = len(word)
        if length % 2 != 0:
            word += 'a'
        else:
            pass
        encrypted_matrix = []
        for i in range(0, len(word), 2):
            l = []
            try:
                l += [ord(word[i]) - 97, ord(word[i + 1]) - 97]
            except:
                l += [ord(word[i]) - 97, 0]
            c = np.matmul(key, l)  # multiplying the matrix to obtain the resultant encrypted matrix
            encrypted_matrix.append(c % 26)  # taking the modulo of each array to be inserted into the matrix

        encrypted_message += " " + matrix_to_letter(encrypted_matrix)  # concatenating the encrypted string as one string

    return encrypted_message

# Function for decryption
def decrypt(ciphertext, key):
    word_list = ciphertext.split(" ")
    decrypted_message = ''
    
    for word in word_list:
        length = len(word)
        decrypted_matrix = []
        for i in range(0, len(word), 2):
            l = []
            try:
                l += [ord(word[i]) - 97, ord(word[i + 1]) - 97]
            except:
                l += [ord(word[i]) - 97, 0]
            c = np.matmul(key, l)  # multiplying the matrix to obtain the resultant decrypted matrix
            decrypted_matrix.append(c % 26)  # taking the modulo of each array to be inserted into the matrix

        decrypted_message += " " + matrix_to_letter(decrypted_matrix)[0:length]  # concatenating the decrypted string as one string

    return decrypted_message

# Main program starts here
msg = input("Enter the message for encryption: ")
key = np.array([[1, 2], [1, 3]])
key = np.array([[9, 8], [10, 9]])

encrypted_message = encrypt(msg, key)
print("Encrypted message:", encrypted_message)


decrypted_message = decrypt(encrypted_message, np.linalg.inv(key).astype(int))
print("Decrypted message:", decrypted_message)