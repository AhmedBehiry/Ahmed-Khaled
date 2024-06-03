import tkinter as tk
from tkinter import messagebox
import math

def rail_fence_encrypt(text, rails):
    fence = [['\n' for _ in range(len(text))] for _ in range(rails)]
    direction = -1
    
    row, col = 0, 0
    
    for char in text:
        if row == 0 or row == rails - 1:
            direction *= -1
        
        fence[row][col] = char
        col += 1
        row += direction
    
    encrypted_text = ''
    for i in range(rails):
        for j in range(len(text)):
            if fence[i][j]!= '\n':
                encrypted_text += fence[i][j]
    
    return encrypted_text

def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

def calculate_metrics(original_text, encrypted_text):
    mse = sum((ord(a) - ord(b)) ** 2 for a, b in zip(original_text, encrypted_text)) / len(original_text)
    psnr = 10 * math.log10((255 ** 2) / mse)
    return psnr, mse

def encrypt_text():     
    original_text = entry.get()
    # rails is the number of rows 
    key = 2  # Example number of rails, adjust as needed
    rail_encrypted_text = rail_fence_encrypt(original_text, key)
    caesar_encrypted_text = caesar_encrypt(original_text, 3)  # Example shift value, adjust as needed
    
    psnr_rail, mse_rail = calculate_metrics(original_text, rail_encrypted_text)
    psnr_caesar, mse_caesar = calculate_metrics(original_text, caesar_encrypted_text)
    
    messagebox.showinfo("Encryption Results", 
                        f"Rail Fence Cipher Encrypted Text: {rail_encrypted_text}\n"
                        f"PSNR (Rail Fence Cipher): {psnr_rail}\n"
                        f"MSE (Rail Fence Cipher): {mse_rail}\n\n"
                        f"Caesar Cipher Encrypted Text: {caesar_encrypted_text}\n"
                        f"PSNR (Caesar Cipher): {psnr_caesar}\n"
                        f"MSE (Caesar Cipher): {mse_caesar}")

# Create GUIcd 
root = tk.Tk()
root.title("Text Encryption")
root.geometry("400x200")

label = tk.Label(root, text="Enter text to encrypt:")
label.pack()

entry = tk.Entry(root, width=50)
entry.pack()

encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_text)
encrypt_button.pack()

root.mainloop()
