def square_root(number):
    number_of_subtractions = 0
    odd_number = 1
    while number > 0:
        number -= odd_number
        odd_number += 2
        number_of_subtractions += 1

    return number_of_subtractions
    
