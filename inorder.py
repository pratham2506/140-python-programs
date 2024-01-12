def is_in_order(s):
    return s == ''.join(sorted(s))
print(is_in_order("abc"))