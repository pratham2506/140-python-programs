numbers = [10,20,30,70,5,3,100]
numbers.sort(reverse=True)
if len(numbers) >= 2:
    second_largest = numbers[1]
    print("The second largest number in the list is ",second_largest)