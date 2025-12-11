SUBLIST = 3
SUPERLIST = 2
EQUAL = 1
UNEQUAL = 0

def is_sub_sequence(list_a, list_b):
    if not list_a:
        return True
        
    length_of_a = len(list_a)
    length_of_b = len(list_b)

    for i in range((length_of_b - length_of_a) + 1):
        if list_b[i : i + length_of_a] == list_a:
            return True
    return False

def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
    if is_sub_sequence(list_one, list_two):
        return SUBLIST
    if is_sub_sequence(list_two, list_one):
        return SUPERLIST
    return UNEQUAL
