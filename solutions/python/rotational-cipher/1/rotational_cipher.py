def rotate(text, key):
    uppercase_letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    lowercase_letters = list('abcdefghijklmnopqrstuvwxyz')
    ciphered = ''
    for char in text:
        if char in uppercase_letters:
            i = uppercase_letters.index(char)
            new_i = (i + key) % 26
            ciphered += uppercase_letters[new_i]
        elif char in lowercase_letters:
            i = lowercase_letters.index(char)
            new_i = (i + key) % 26
            ciphered += lowercase_letters[new_i]
        else:
            ciphered += char

    return ciphered
        
            
        
        
        
        
        
        
