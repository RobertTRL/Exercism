def value(colors):
    i = 0
    total_band_value = ''
    for specific_color in colors:
        if i < 2:
            color_list = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
            band_value = str(color_list.index(specific_color))
            total_band_value = total_band_value + band_value
            i += 1
            
    return int(''.join(total_band_value))
        
