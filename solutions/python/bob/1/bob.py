def response(hey_bob):
    no_whitespace = hey_bob.strip()
    if no_whitespace.endswith("?") and no_whitespace.isupper():
        return "Calm down, I know what I'm doing!"
    if no_whitespace.endswith("?"):
        return "Sure."
    if no_whitespace.isupper() and any(c.isalpha() for c in hey_bob):
        return "Whoa, chill out!"
    if not no_whitespace :
        return "Fine. Be that way!"
    else:
        return "Whatever."