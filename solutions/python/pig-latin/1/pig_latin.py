def translate(text):
    vowels = ("a", "e", "i", "o", "u")

    def translate_word(word):
        i = 0
        if word.startswith(vowels) or word.startswith("xr") or word.startswith("yt"):
            return word + "ay"
        split_point_found = False         
        while i < len(word) and not split_point_found:
            if word[i] == "q" and i + 1 < len(word) and word[i + 1] == "u":
                i += 2
                split_point_found = True

            elif word[i]  == "y" and i > 0:
                split_point_found = True

            elif word[i] in vowels:
                split_point_found = True

            else:
                i += 1
        consonants = word[:i]
        remaining_word = word[i:]
        return remaining_word + consonants + "ay"

    return " ".join(translate_word(specific_word) for specific_word in text.split())
    


     
    