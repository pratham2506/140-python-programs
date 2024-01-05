def recurssion_fibonnaci(n):
    if n <= 1:
        return n
    else:
        return(recurssion_fibonnaci(n-1) + recurssion_fibonnaci(n-2))
nterms = int(input("Enter the number of temrs (greater than 0) : "))
if nterms <= 0:
    print("Please enter a positive integer")
else:
    print("Fibonacci Series : ")
    for i in range(nterms):
        print(recurssion_fibonnaci(i))