def mapping(letters):
    result = {}
    for letter in letters:
        result[letter] = letter.upper()
    return result
print(mapping(["a", "v", "y", "z"]))