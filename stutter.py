def stutter(word):
    if len(word) < 2:
        return "The length of the word must be more than 2."
    stuttered_word = f"{word[:2]}... {word[:2]}... {word}"
    return stuttered_word
print(stutter("incredible")) 
print(stutter("enthusiastic")) 
print(stutter("outstanding"))
