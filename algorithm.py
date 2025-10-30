def encrypt(text):
    """
    Encrypts a string by converting alphabet letters to numbers (a=1, b=2, etc.)
    and numbers to alphabet letters (0=a, 1=b, etc.).
    
    Each converted item is separated by a comma to avoid ambiguity.
    """
    encrypted_parts = []
    for char in text:
        if 'a' <= char.lower() <= 'z':
            if char.islower():
                encrypted_parts.append(str(ord(char) - ord('a') + 1))
            else:  
                encrypted_parts.append(str(ord(char) - ord('A') + 1))
        elif '0' <= char <= '9':
            encrypted_parts.append(chr(ord('a') + int(char)))
        else:
            encrypted_parts.append(char)
    return ",".join(encrypted_parts)


def decrypt(text):
    """
    Decrypts a comma-separated string by converting numbers back to 
    alphabet letters (1=a, 2=b, etc.) and alphabet letters back to 
    numbers (a=0, b=1, etc.).
    """
    decrypted_text = []
    parts = text.split(',')
    
    for part in parts:
        if part.isdigit():

            num = int(part)
            if 1 <= num <= 26:
                decrypted_text.append(chr(ord('a') + num - 1))
            else:
                decrypted_text.append(part)
        elif len(part) == 1 and 'a' <= part.lower() <= 'j':
            decrypted_text.append(str(ord(part.lower()) - ord('a')))
        else:
            decrypted_text.append(part)
            
    return "".join(decrypted_text)


