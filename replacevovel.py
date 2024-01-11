def replace_vowel(string,char):
    vowels = "AEIOUaeiou"
    for vowel in vowels:
        string = string.replace(vowel,char)
    return string
print(replace_vowel("the aardvark", "#"))
print(replace_vowel("minnie mouse", "?"))
print(replace_vowel("shakespeare", "*"))