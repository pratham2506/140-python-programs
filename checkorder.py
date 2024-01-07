from collections import OrderedDict
def check_order(string,reference):
    string_dict = OrderedDict.fromkeys(string)
    reference_dict = OrderedDict.fromkeys(reference)
    return string_dict == reference_dict
input_string = "hello world"
reference_string = "helo wrd"
if check_order(input_string,reference_string):
    print("The order of characters in the input strings matches the reference")
else:
    print("The order of characters in the input strings does not match the reference")
    