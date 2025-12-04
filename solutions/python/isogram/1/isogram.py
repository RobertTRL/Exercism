def is_isogram(string):
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    letters =  list(c for c in (string.lower()) if c in alphabet)
    return len(set(letters)) == len(letters)