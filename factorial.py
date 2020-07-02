#Write a recursive function to print the factorial for a given number

def facto(n):
    if(n==0):
        return 1
    else:
        return(n*facto(n-1))

num=int(input("Enter a Number : "))
x=facto(num)
print("Factorial of ",num," is ",x)
