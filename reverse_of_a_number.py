#Write a function that reverses the user defined value.

#function
def rev(a):
    r=0
    while(a>0):
        rem=a%10
        r=r*10+rem
        a//=10
    return(r)

#main part

num=int(input("Enter a 3-Digit Number : "))
r=rev(num)
print("Reverse of the Number is : ",r)
