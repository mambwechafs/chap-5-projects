from cryptography.fernet import Fernet

def generate_key(password):
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)

def load_key():
    with open('key.key', 'rb') as key_file:
        key = key_file.read()
    return key

def encrypt_file(filename, password):
    key = load_key()
    cipher = Fernet(key)
    with open(filename, 'rb') as file:
        file_data = file.read()
    encrypted_data = cipher.encrypt(file_data)
    with open(f'encrypted_{filename}', 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)

def decrypt_file(filename, password):
    key = load_key()
    cipher = Fernet(key)
    with open(filename, 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = cipher.decrypt(encrypted_data)
    with open(f'decrypted_{filename}', 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)

# Example usage
generate_key('mypassword')
encrypt_file('plaintext.txt', 'mypassword')
decrypt_file('encrypted_plaintext.txt', 'mypassword')
