def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
n=int(input("Enter the n value:"))
if n<=0:
    print("n should be greater than 0")
print("The factorial of n number is:",fact(n))
