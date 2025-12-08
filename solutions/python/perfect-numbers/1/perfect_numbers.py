def classify(number):
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    def get_aliquot_sum(n):
        total_sum = 0
        for i in range(1, number):
            if n % i == 0:
                total_sum += i        
        return total_sum
    
    aliquot_sum = get_aliquot_sum(number)
    if number == aliquot_sum:
        return "perfect"
    if number < aliquot_sum:
        return "abundant"
    if number > aliquot_sum or aliquot_sum == 1:
        return "deficient"