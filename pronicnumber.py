def is_pronic_number(num):
    for n in range(1, int(num ** .5)+1):
        if n * (n+1) == num:
            return True
    return False
print("Pronic numbers between 1 to 100")
for i in range(1,101):
    if is_pronic_number(i):
        print(i, end='|')