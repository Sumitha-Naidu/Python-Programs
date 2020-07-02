#Write a program to generate the Fibonacci series.

num=int(input("Enter the range for Fibonacci Series : "))
a=0
b=1
print(a,end = "\t")
print(b,end = "\t")
for i in range(b,num-1):
    c=a+b
    print(c,end = "\t")
    a=b
    b=c
