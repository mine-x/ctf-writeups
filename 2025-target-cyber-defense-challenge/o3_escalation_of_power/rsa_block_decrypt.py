from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

# Load decrypted private key
with open("mysshkey_decrypted.pem", "rb") as f:
    private_key = serialization.load_pem_private_key(f.read(), password=None)

# Load the RSA-encrypted AES key (first 512 bytes of flag.bin)
with open("rawflag.txt", "rb") as f:
    data = f.read()

rsa_ciphertext = data[:512]  # adjust size based on your key
aes_ciphertext = data[512:]  # the rest is AES-encrypted flag

# Decrypt RSA to get AES key
aes_key = private_key.decrypt(
    rsa_ciphertext,
    padding.PKCS1v15()  # try OAEP if PKCS1v15 fails
)

print("Recovered AES key:", aes_key.hex())
