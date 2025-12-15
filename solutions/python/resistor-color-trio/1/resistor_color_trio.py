def label(colors):
    color_list = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
    main_value = (color_list.index(colors[0])) * 10 + color_list.index(colors[1])
    exponential_value = color_list.index(colors[2])
    total_value = main_value * 10 ** exponential_value
    if total_value >= 1000000000:
        return str(int(total_value/ 10 ** 9)) + ' gigaohms'
    if total_value >= 1000000:
        return str(int(total_value/ 10 ** 6)) + ' megaohms'
    if total_value >= 1000:
        return str(int(total_value/ 10 ** 3)) + ' kiloohms'
    return str(total_value) + ' ohms'
    
        