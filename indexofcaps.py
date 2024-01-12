def index_of_caps(word):
    return [i for i, char in enumerate(word) if char.isupper()] 
print(index_of_caps("eDaBiT"))