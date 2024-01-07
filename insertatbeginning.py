from collections import OrderedDict
ordered_dict = OrderedDict([('b', 2), ('c', 3), ('d', 4)])
new_item = ('a',1)
new_ordered_dict = OrderedDict([new_item])
new_ordered_dict.update(ordered_dict)
print("Update OrderedDict : ",new_ordered_dict)