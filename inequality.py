def correct_inequality(expression):
    try:
        return eval(expression)
    except:
        return False
print(correct_inequality("3 < 7 < 11"))
print(correct_inequality("13 > 44 > 33 < 1"))
print(correct_inequality("1 < 2 < 6 < 9 > 3"))