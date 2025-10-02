# Image Encryption Tool

![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

A simple, secure command-line tool to encrypt and decrypt image files using the `cryptography` library in Python. This tool uses symmetric (secret-key) encryption, ensuring that only someone with the correct key can view the original image.

## Features

* **Strong Encryption:** Utilizes the Fernet implementation, which uses AES-128 in CBC mode with a PKCS7 padding, and HMAC with SHA256 for authentication.
* **Automatic Key Management:** Automatically generates and saves an encryption key if one is not found.
* **User-Friendly CLI:** An easy-to-use menu-driven interface for encryption and decryption.
* **File Agnostic:** While designed for images, it can encrypt and decrypt any file type.

## How It Works

The script uses **symmetric-key encryption**. This means the same key is used for both encrypting and decrypting the data.

1.  **Key Generation:** When you first run the script to encrypt a file, it checks for a key file named `image_encryption_key.key`. If it doesn't exist, a new, cryptographically secure key is generated and saved.
2.  **Encryption:** The tool reads the image file as binary data, encrypts this data using the key, and saves the encrypted content to a new file.
3.  **Decryption:** The tool reads the encrypted file, uses the same key to decrypt the content, and saves the original binary data back into an image file.

## Prerequisites

* Python 3.7 or higher
* `pip` (Python package installer)

## Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/Image-Encryption-Tool.git](https://github.com/your-username/Image-Encryption-Tool.git)
    cd Image-Encryption-Tool
    ```

2.  **Install the required package:**
    It is highly recommended to use a virtual environment.
    ```bash
    # Create and activate a virtual environment (optional but recommended)
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

    # Install the dependency
    pip install -r requirements.txt
    ```

## Usage

Run the script from your terminal:

```bash
python encryptor.py
```
*(Assuming you've renamed the script file to `encryptor.py`)*

You will be presented with a menu:

```
Image Encryption Tool
1. Encrypt an image
2. Decrypt an image
3. Exit
Enter your choice (1-3):
```

### Example: Encrypting an Image

1.  Choose option `1`.
2.  Enter the path to your source image (e.g., `my_cat.jpg`).
3.  Enter the desired path for the encrypted output file (e.g., `my_cat_encrypted.dat`).

```
Enter your choice (1-3): 1
Enter the path to the image file: images/my_cat.jpg
Enter the output path for encrypted file: encrypted/my_cat.dat
Image encrypted successfully. Saved to encrypted/my_cat.dat
```

### Example: Decrypting an Image

1.  Choose option `2`.
2.  Enter the path to your encrypted file (e.g., `encrypted/my_cat.dat`).
3.  Enter the desired path for the decrypted image (e.g., `decrypted/my_cat_restored.jpg`).

```
Enter your choice (1-3): 2
Enter the path to the encrypted file: encrypted/my_cat.dat
Enter the output path for decrypted image: decrypted/my_cat_restored.jpg
Image decrypted successfully. Saved to decrypted/my_cat_restored.jpg
```

---

## ⚠️ Important Security Notice

* **KEY MANAGEMENT IS CRITICAL:** The `image_encryption_key.key` file is your master key.
    * **Do NOT lose this key.** If you lose the key, all files encrypted with it will be permanently unrecoverable. There is no "forgot password" option.
    * **Do NOT share this key publicly.** Anyone with this key can decrypt your files.
    * **Backup your key** in a secure, offline location (like a password manager or an encrypted USB drive).
* **DO NOT COMMIT YOUR KEY TO GIT.** The `.gitignore` file included in this repository is configured to prevent the key file from being accidentally uploaded.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
