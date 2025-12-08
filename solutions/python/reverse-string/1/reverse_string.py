def reverse(text):
    new_text = ''
    i = 0
    while i < len(text):
        char = text[i]
        new_text = char + new_text
        i += 1
    return new_text
        

        
