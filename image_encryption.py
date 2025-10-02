from cryptography.fernet import Fernet
import os

def generate_key():
    """Generate a new encryption key and save it to a file."""
    key = Fernet.generate_key()
    with open('image_encryption_key.key', 'wb') as key_file:
        key_file.write(key)
    return key

def load_key():
    """Load the encryption key from a file."""
    try:
        return open('image_encryption_key.key', 'rb').read()
    except FileNotFoundError:
        print("Key file not found. Generating a new key...")
        return generate_key()

def encrypt_image(input_path, output_path):
    """Encrypt an image file."""
    try:
        # Load or generate the encryption key
        key = load_key()
        fernet = Fernet(key)
        
        # Read the image file
        with open(input_path, 'rb') as image_file:
            image_data = image_file.read()
        
        # Encrypt the image data
        encrypted_data = fernet.encrypt(image_data)
        
        # Save the encrypted data
        with open(output_path, 'wb') as encrypted_file:
            encrypted_file.write(encrypted_data)
        
        print(f"Image encrypted successfully. Saved to {output_path}")
        
    except Exception as e:
        print(f"Error during encryption: {str(e)}")

def decrypt_image(input_path, output_path):
    """Decrypt an encrypted image file."""
    try:
        # Load the encryption key
        key = load_key()
        fernet = Fernet(key)
        
        # Read the encrypted image file
        with open(input_path, 'rb') as encrypted_file:
            encrypted_data = encrypted_file.read()
        
        # Decrypt the image data
        decrypted_data = fernet.decrypt(encrypted_data)
        
        # Save the decrypted image
        with open(output_path, 'wb') as decrypted_file:
            decrypted_file.write(decrypted_data)
        
        print(f"Image decrypted successfully. Saved to {output_path}")
        
    except Exception as e:
        print(f"Error during decryption: {str(e)}")

def main():
    while True:
        print("\nImage Encryption Tool")
        print("1. Encrypt an image")
        print("2. Decrypt an image")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            input_path = input("Enter the path to the image file: ")
            if not os.path.exists(input_path):
                print("Input file does not exist!")
                continue
            output_path = input("Enter the output path for encrypted file: ")
            encrypt_image(input_path, output_path)
        
        elif choice == '2':
            input_path = input("Enter the path to the encrypted file: ")
            if not os.path.exists(input_path):
                print("Input file does not exist!")
                continue
            output_path = input("Enter the output path for decrypted image: ")
            decrypt_image(input_path, output_path)
        
        elif choice == '3':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()