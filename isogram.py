def is_isogram(word):
    word = word.lower()
    unique_letters = set()
    for letter in word:
        if letter in unique_letters:
            return False
        unique_letters.add(letter)
    return True
print(is_isogram("Algorism"))