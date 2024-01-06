def passwordCheck(password):
    specialCount = 0
    charCount = 0
    letterCount = 0
    digitCount = 0
    for char in password:
        charCount += 1
        if char.isalpha():
            letterCount += 1
        if char == '@' or '#' or '&':
            specialCount += 1
        if char.isdigit():
            digitCount += 1

    if specialCount >= 1 and letterCount >= 1 and digitCount >= 1 and charCount >= 8:
        return True
    else:
        return False
