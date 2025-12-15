def resistor_label(colors):
    color_list = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
    tolerance_dict = {'grey': 0.05, 'violet': 0.1, 'blue': 0.25, 'green': 0.5, 'brown': 1, 'red': 2, 'gold': 5, 'silver': 10}
    main_value = 0
    tolerance_value = 0
    exponential_value = 0
    if len(colors) == 5:
        main_value = (color_list.index(colors[0]) * 100) + (color_list.index(colors[1]) * 10) + color_list.index(colors[2])
        tolerance_value = tolerance_dict[(colors[4])]
        exponential_value = color_list.index(colors[3])
        
    elif len(colors) == 4:
        main_value = (color_list.index(colors[0]) * 10) + color_list.index(colors[1])
        tolerance_value = tolerance_dict[(colors[3])]
        exponential_value = color_list.index(colors[2])
    else:
        return '0 ohms'
        
    total_value = main_value * 10 ** exponential_value
    if total_value >= 1000000000:
        return f"{(total_value / 10**9):g} gigaohms ±{tolerance_value}%"
    if total_value >= 1000000:
        return f"{(total_value / 10**6):g} megaohms ±{tolerance_value}%"
    if total_value >= 1000:
        return f"{(total_value / 10**3):g} kiloohms ±{tolerance_value}%"
    return f"{total_value:g} ohms ±{tolerance_value}%"
        
        
        
        
