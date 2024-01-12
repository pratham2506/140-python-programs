def amplify(num):
    return [n * 10 if n % 4 == 0 else n for n in range(1,num+1)]
print(amplify(4))