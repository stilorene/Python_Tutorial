import time

text = 'Hallo Rene der Zerstörer'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'


def vigenere(message, key, direction = -1):   
    encrypted_text = ''
    for char in message.lower():
        
        if not char.isalpha():
            encrypted_text += char     
        else:
            index = key.find(char)
            new_index = (index + shift*direction) % len(key)
            new_char = key[new_index] 
            encrypted_text += new_char 
            
    print(f'aktuelle char: {text}' f' Verschschlüsselte Text: {encrypted_text}' )
    
def encrypt(message, key):
    return vigenere(message, key)

def decrypt(message, key):
    return vigenere(message, key, -1)


            
vigenere(text, alphabet)   
# Verschlüsselte Nachricht: kdoor uhqh ghu chuvwcuhu