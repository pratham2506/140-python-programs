class Divisiblebyseven:
    def __init__(self,n):
        self.n = n
    def generate_divisible_by_seven(self):
        for num in range(self.n + 1):
            if num % 7 == 0:
                yield num
n = int(input("Enter your desired range : "))
divisible_byseven_generator = Divisiblebyseven(n).generate_divisible_by_seven()
for num in divisible_byseven_generator:
    print(num)