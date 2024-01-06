numbers = [10,50,100,-10,70]
minimum = numbers[0]
for i in numbers:
    if i < minimum:
        minimum =  i
print("The smallest number in the list is ",minimum)