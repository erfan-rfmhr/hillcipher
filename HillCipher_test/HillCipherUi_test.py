
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QTextEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette

import numpy as np


class EncryptionApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Encryption App")
        self.setGeometry(300, 300, 500, 300)

        self.plaintext_textedit = QTextEdit()
        self.encrypted_textedit = QTextEdit()
        self.decrypt_textedit = QTextEdit()
        self.decrypt_textedit.hide()  

        self.encrypt_button = QPushButton("Encrypt", self)
        self.decrypt_button = QPushButton("Decrypt", self)

        self.setup_ui()

    def setup_ui(self):
        plaintext_label = QLabel("Plaintext:")
        encrypted_label = QLabel("Encrypted:")
        decrypt_label = QLabel("Decrypted:")

        # Apply styles to the labels
        plaintext_label.setStyleSheet("font-weight: bold;")
        encrypted_label.setStyleSheet("font-weight: bold;")
        decrypt_label.setStyleSheet("font-weight: bold;")

        layout = QVBoxLayout()
        form_layout = QHBoxLayout()
        button_layout = QHBoxLayout()

        form_layout.addWidget(plaintext_label)
        form_layout.addWidget(self.plaintext_textedit)
        form_layout.addWidget(encrypted_label)
        form_layout.addWidget(self.encrypted_textedit)
        form_layout.addWidget(decrypt_label)
        form_layout.addWidget(self.decrypt_textedit)

        button_layout.addWidget(self.encrypt_button)
        button_layout.addWidget(self.decrypt_button)

        layout.addLayout(form_layout)
        layout.addLayout(button_layout)

        # Set margins and spacing for the main layout
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(10)

        self.setLayout(layout)

        self.encrypt_button.clicked.connect(self.encrypt)
        self.decrypt_button.clicked.connect(self.decrypt)

        # Set the background color
        self.setStyleSheet("background-color: gray;")

    def matrix_to_letter(self, matrix):
        encrypted_string = ''
        for row in matrix:
            for num in row:
                encrypted_string += chr(num + 97)
        return encrypted_string

    def encrypt(self):
        plaintext = self.plaintext_textedit.toPlainText()
        key = np.array([[1, 2], [1, 3]])

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
                c = np.matmul(key, l)
                encrypted_matrix.append(c % 26)

            encrypted_message += " " + self.matrix_to_letter(encrypted_matrix)

        self.encrypted_textedit.setPlainText(encrypted_message.strip())

    def decrypt(self):
        ciphertext = self.encrypted_textedit.toPlainText()
        key = np.array([[1, 2], [1, 3]])
        key = np.linalg.inv(key).astype(int)

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
                c = np.matmul(key, l)
                decrypted_matrix.append(c % 26)

            decrypted_message += " " + self.matrix_to_letter(decrypted_matrix)[0:length]

        self.plaintext_textedit.setPlainText(decrypted_message.strip())
        self.decrypt_textedit.show()  # Show the key_textedit after decryption
        self.decrypt_textedit.setPlainText(decrypted_message.strip())


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Set the application style
    app.setStyle("Fusion")

    window = EncryptionApp()
    window.show()
    sys.exit(app.exec_())