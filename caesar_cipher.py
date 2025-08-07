def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

# Main Program
print("Caesar Cipher Program")
choice = input("Do you want to Encrypt (E) or Decrypt (D)? ").upper()
message = input("Enter your message: ")
shift = int(input("Enter shift value (e.g. 3): "))

if choice == 'E':
    encrypted = encrypt(message, shift)
    print("Encrypted Message:", encrypted)
elif choice == 'D':
    decrypted = decrypt(message, shift)
    print("Decrypted Message:", decrypted)
else:
    print("Invalid choice. Please enter E or D.")
          
