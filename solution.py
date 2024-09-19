def find_missing_letter(chars):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    beginning = False
    for letter in alpha:
        if letter == chars[0].lower():
            beginning = True
        if beginning:
            if letter not in [x.lower() for x in chars]:
                if chars[0].isupper():
                    return letter.upper()
                return letter
