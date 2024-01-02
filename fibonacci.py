nterm = int(input("Enter the number : "))
n1,n2 = 0,1
count = 1
if nterm <= 0:
    print("Enter a positive number")
elif nterm == 1:
    print("Fibonnaci sequence upto", nterm, ":")
    print(n1)
else:
    print("Fibonnaci Series")
    while count < nterm:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1