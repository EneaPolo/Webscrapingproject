from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
import json
import base64

# Funksioni për enkriptim
def encrypt_data(data, key):
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data.encode('utf-8'))
    return cipher.nonce + tag + ciphertext

# Shkruaj një çelës AES të rastësishëm
key = get_random_bytes(16)

# Lexo të dhënat nga data.json
with open('data.json', 'r') as f:
    data = json.load(f)

# Enkripto të dhënat
encrypted_data = []
for entry in data:
    encrypted_entry = encrypt_data(entry['title'], key)
    encrypted_data.append({'encrypted_title': base64.b64encode(encrypted_entry).decode('utf-8')})

# Ruaj të dhënat e enkriptuara në një skedar të ri
with open('encrypted_data.json', 'w') as f:
    json.dump(encrypted_data, f, indent=4)

print("Të dhënat u enkriptuan dhe u ruajtën në encrypted_data.json.")
