def reverse(value):
    if isinstance(value,bool):
        return not value
    else:
        return "Boolean expected!"
print(reverse(True))