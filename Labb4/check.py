import os, time, csv
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad


#AES Encryption / Decryption
def aes_encrypt_decrypt():
    try:
        key_size = int(input("Enter AES key size (128 or 256): ")) // 8
        mode_choice = input("Enter mode (ecb/cfb): ").lower()
        file_in = input("Enter file name to encrypt: ")

        with open(file_in, "rb") as f:
            data = f.read()

        key = get_random_bytes(key_size)
        iv = get_random_bytes(16)
        start = time.time()

        if mode_choice == "ecb":
            cipher = AES.new(key, AES.MODE_ECB)
        elif mode_choice == "cfb":
            cipher = AES.new(key, AES.MODE_CFB, iv)
        else:
            print("Invalid mode selected.")
            return

        ciphertext = cipher.encrypt(pad(data, AES.block_size))
        with open("aes_enc.bin", "wb") as f:
            f.write(ciphertext)
        print("Encrypted file saved as aes_enc.bin")

        # Decryption
        if mode_choice == "ecb":
            cipher_dec = AES.new(key, AES.MODE_ECB)
        else:
            cipher_dec = AES.new(key, AES.MODE_CFB, iv)

        plaintext = unpad(cipher_dec.decrypt(ciphertext), AES.block_size)
        print("Decrypted text:\n", plaintext.decode(errors="ignore"))
        end = time.time()
        print("Execution time:", round(end - start, 6), "seconds")

    except Exception as e:
        print("Error during AES operation:", e)


#RSA Encryption / Decryption
def rsa_encrypt_decrypt():
    try:
        if not os.path.exists("private.pem"):
            print("Generating RSA key pair (2048 bits)...")
            key = RSA.generate(2048)
            with open("private.pem", "wb") as f:
                f.write(key.export_key())
            with open("public.pem", "wb") as f:
                f.write(key.publickey().export_key())
            print("RSA keys generated and saved as private.pem & public.pem")

        private_key = RSA.import_key(open("private.pem").read())
        public_key = RSA.import_key(open("public.pem").read())

        file_in = input("Enter file name to encrypt: ")
        with open(file_in, "rb") as f:
            data = f.read()

        start = time.time()
        cipher_rsa = PKCS1_OAEP.new(public_key)
        enc_data = cipher_rsa.encrypt(data)
        with open("rsa_enc.bin", "wb") as f:
            f.write(enc_data)
        print("Encrypted file saved as rsa_enc.bin")

        cipher_rsa = PKCS1_OAEP.new(private_key)
        dec_data = cipher_rsa.decrypt(enc_data)
        print("Decrypted text:\n", dec_data.decode(errors="ignore"))
        end = time.time()
        print("Execution time:", round(end - start, 6), "seconds")

    except Exception as e:
        print("Error during RSA operation:", e)


#RSA Signature & Verification
def rsa_signature():
    try:
        if not os.path.exists("private.pem") or not os.path.exists("public.pem"):
            print("RSA keys not found! Generate them first using RSA Encrypt/Decrypt option.")
            return

        private_key = RSA.import_key(open("private.pem").read())
        public_key = RSA.import_key(open("public.pem").read())

        file_in = input("Enter file name to sign: ")
        with open(file_in, "rb") as f:
            data = f.read()

        hash_data = SHA256.new(data)
        signature = pkcs1_15.new(private_key).sign(hash_data)
        with open("signature.bin", "wb") as f:
            f.write(signature)
        print("Signature generated and saved as signature.bin")

        # Verification
        try:
            pkcs1_15.new(public_key).verify(hash_data, signature)
            print("Signature verification successful ✅")
        except (ValueError, TypeError):
            print("Verification failed ❌")

    except Exception as e:
        print("Error during RSA signature operation:", e)


#SHA-256 Hashing
def sha256_hash():
    try:
        file_in = input("Enter file name to hash: ")
        with open(file_in, "rb") as f:
            data = f.read()

        start = time.time()
        hash_value = SHA256.new(data).hexdigest()
        end = time.time()

        print("SHA-256 hash:", hash_value)
        print("Execution time:", round(end - start, 6), "seconds")
    except Exception as e:
        print("Error during SHA hashing:", e)


#Timing Experiment (Starting from 16 bits as per Lab Manual)

def timing_experiment():
    aes_results = []
    rsa_results = []

    file_in = input("Enter text file name to use for timing: ")
    with open(file_in, "rb") as f:
        data = f.read()

    print("\n=== AES Timing Experiment (starting from 16 bits) ===")
    for n in [16, 32, 64, 128, 256]:
        start = time.time()
        key = get_random_bytes(max(1, n // 8))
        try:
            cipher = AES.new(key.ljust(16, b'\0')[:16], AES.MODE_ECB)
            cipher.encrypt(pad(data, 16))
        except ValueError:
            pass
        elapsed = time.time() - start
        aes_results.append((n, elapsed))
        print(f"AES Key size {n} bits: {round(elapsed, 6)} seconds")

    print("\n=== RSA Timing Experiment (starting from 16 bits) ===")
    for n in [16, 32, 64, 128, 256]:
        start = time.time()
        try:
            key = RSA.generate(max(512, n))
            public_key = key.publickey()
            cipher = PKCS1_OAEP.new(public_key)
            cipher.encrypt(data[:62])  
        except ValueError:
            pass
        elapsed = time.time() - start
        rsa_results.append((n, elapsed))
        print(f"RSA Key size {n} bits: {round(elapsed, 6)} seconds")

    with open("timing_results_lab.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Algorithm", "Key_Size_bits", "Execution_Time_seconds"])
        for n, t in aes_results:
            writer.writerow(["AES", n, round(t, 6)])
        for n, t in rsa_results:
            writer.writerow(["RSA", n, round(t, 6)])

    print("\nExperimental results saved to timing_results_lab.csv ✅")



# Menu
def menu():
    print("\n=== Crypto Lab 4 Menu ===")
    print("1. AES Encrypt/Decrypt")
    print("2. RSA Encrypt/Decrypt")
    print("3. RSA Signature & Verify")
    print("4. SHA-256 Hash")
    print("5. Timing Experiment")
    print("6. Exit")


# Main Loop 
if __name__ == "__main__":
    while True:
        menu()
        choice = input("Select option: ")

        if choice == '1':
            aes_encrypt_decrypt()
        elif choice == '2':
            rsa_encrypt_decrypt()
        elif choice == '3':
            rsa_signature()
        elif choice == '4':
            sha256_hash()
        elif choice == '5':
            timing_experiment()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid option. Try again.")