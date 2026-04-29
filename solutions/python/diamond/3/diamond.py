def rows(letter):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if letter == 'A':
        return [letter]
    
    position = alphabet.index(letter) + 1
    length = (2 * position) - 1
    storage_array = []
    
    for i in range(1, position + 1):
        if i == 1:
            storage_array.append(('A'.center(length, ' ')))
        else: 
            spacing = ' '* (((2 * i) - 1) - 2)
            specific_letter = alphabet[(i - 1)]
            storage_array.append((f"{specific_letter}{spacing}{specific_letter}".center(length, ' ')))

    bottom_half = storage_array[:-1][::-1]
    storage_array.extend(bottom_half)
    return storage_array
    
