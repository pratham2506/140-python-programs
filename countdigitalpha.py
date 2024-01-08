sentence = input("Enter a sentence : ")
letter_count = 0
digit_count = 0
for char in sentence:
    if char.isalpha():
        letter_count += 1
    elif char.isdigit():
        digit_count += 1
print("Number of letter : ",letter_count)
print("Number of digits : ",digit_count)
