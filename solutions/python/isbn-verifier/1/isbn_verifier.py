def is_valid(isbn):
    no_hyphen = isbn.replace('-', '')
    if len(no_hyphen) != 10:
        return False
        
    total = 0
    i = 0
    for char in no_hyphen:
        weight = 10 - i
        if char.isdigit():
            value = int(char)
        elif char.upper() == 'X' and i == 9:
            value = 10
        else:
            return False

        total += value * weight
        i += 1
    return total % 11 == 0
                
        
        
        
    