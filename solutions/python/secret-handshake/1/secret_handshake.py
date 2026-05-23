def commands(binary_str):
    if not int(binary_str):
        return []
    
    result_list = ['wink' * int(binary_str[4]), 'double blink' * int(binary_str[3]) , 'close your eyes' * int(binary_str[2]) , 'jump' * int(binary_str[1]) ,'reverse' * int(binary_str[0])]
    cleaned_up = []
    for value in result_list:
        if value:
            cleaned_up.append(value)

    
    return cleaned_up[::-1][1:] if cleaned_up[-1] == 'reverse' else cleaned_up
    

    
        

    
        
