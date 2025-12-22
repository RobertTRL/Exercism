lowercase_letters = list('abcdefghijklmnopqrstuvwxyz')
uppercase_letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
numbers = list('0123456789')
def cipher(text):
    ciphered = ''
    for character in text:
        if character in uppercase_letters:
            i = uppercase_letters.index(character)
            complementary_i = 25 - i
            ciphered += lowercase_letters[complementary_i]
        
        if character in lowercase_letters:
            i = lowercase_letters.index(character)
            complementary_i = 25 - i
            ciphered += lowercase_letters[complementary_i]

        if character in numbers:
            ciphered += character

        else:
            ciphered += ''
    return ciphered
    
def encode(plain_text):
    unspaced = cipher(plain_text)
    result = ''
    for index, character in enumerate(unspaced, 1):
        if index % 5 == 0 and character != unspaced[-1]:
            result += character + ' '
        else:
            result += character
        
    return result       
    
def decode(ciphered_text):
    return cipher(ciphered_text)
