input_sentence = input("Enter a sentence: ")
words = input_sentence.split()
word_freq = {}
for word in words:
    word = word.strip('.,?')
    word = word.lower()
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1
sorted_words = sorted(word_freq.items())
for word, frequency in sorted_words:
    print(f"{word} : {frequency}")