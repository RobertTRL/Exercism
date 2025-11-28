def is_armstrong_number(number)-> bool:
    string = str(number)
    power = len(string)
    sum_of_digits = 0
    for digit_char in string:
        digit = int(digit_char)
        sum_of_digits = sum_of_digits + digit ** power
    return sum_of_digits == number