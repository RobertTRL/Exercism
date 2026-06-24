def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")

    def get_base_10_value(base, digits):
        total_value_base_10 = 0
        power = (len(digits)) - 1
        for n in digits:
            if n >= base or n < 0:
                raise ValueError("all digits must satisfy 0 <= d < input base")
            
            base_value = n * (base ** power)
            total_value_base_10 += base_value
            power -= 1
        return total_value_base_10

    def get_output_base_list(number, base):
        if number == 0:
            return [0]
        modulus_list = []
        divided_number = number
        while divided_number > 0:
            modulus = divided_number % base
            modulus_list.insert(0, modulus)
            divided_number = divided_number // base   
        return modulus_list
    
    def get_single_digit(list):
        total_value = 0
        power = len(list) - 1
        for item in list:
            place_value = item * (10 ** power)
            total_value += place_value
        return total_value
        
    denary_value = get_base_10_value(input_base, digits)
    output_base_list = get_output_base_list(denary_value, output_base)
    output_number = get_single_digit(output_base_list)
    return output_base_list
    
    
