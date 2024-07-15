def caesar_cipher(text, shift, encrypt=True):
    result = ""
    
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            shift_base = 65 if char.isupper() else 97
            if encrypt:
                result += chr((ord(char) + shift - shift_base) % 26 + shift_base)
            else:
                result += chr((ord(char) - shift - shift_base) % 26 + shift_base)
        else:
            result += char  # Non-letter characters remain the same
            
    return result

def main():
    while True:
        choice = input("Do you want to (e)ncrypt or (d)ecrypt a message? (e/d): ").lower()
        if choice in ['e', 'd']:
            break
        print("Invalid choice. Please enter 'e' to encrypt or 'd' to decrypt.")

    message = input("Enter your message: ")
    shift = int(input("Enter the shift value: "))

    if choice == 'e':
        result = caesar_cipher(message, shift, encrypt=True)
        print(f"Encrypted message: {result}")
    else:
        result = caesar_cipher(message, shift, encrypt=False)
        print(f"Decrypted message: {result}")

if __name__ == "__main__":
    main()
