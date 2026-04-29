def is_paired(input_string):
    bracket_dict = {'}' : '{', ']' : '[', ')' : '('}
    stack = []
    for char in input_string:
        if char in bracket_dict.values():
            stack.append(char)
        elif char in bracket_dict:
            if not stack:
                return False

            top_stack_value = stack.pop()
            if top_stack_value != bracket_dict[char]:
                return False

    return len(stack) == 0
    
            
    
    
    
