sample_dict = {'apple': 3, 'banana': 1, 'cherry': 2, 'date': 4}
sorted_dict_bykeys = dict(sorted(sample_dict.items()))
print("Sorted Dictionary")
for key, value in sorted_dict_bykeys.items():
    print(f"{key} : {value}")