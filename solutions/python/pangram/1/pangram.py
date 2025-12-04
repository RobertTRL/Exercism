def is_pangram(sentence):
    letters = list('abcdefghijklmnopqrstuvwxyz')
    lowercase = sentence.lower()
    found_letters = {character for character in lowercase if character in letters}
    return len(found_letters) == len(letters)    