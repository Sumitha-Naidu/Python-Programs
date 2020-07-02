#Write a function to check whether the input value is Pallindrome

def pallin(a):
    r=0
    temp=a
    while(a>0):
        rem=a%10
        r=r*10+rem
        a//=10
    if(temp==r):
        print(temp," is a Pallindrome Number")
    else:
        print(temp," is a not a Pallindrome Number")

num=int(input("Enter a 3-Digit Number : "))
pallin(num)
