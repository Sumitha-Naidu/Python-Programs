#Write a function to check the input value is Armstrong

def arm(a):
    arm=0
    temp=a
    leng = len(str(a))
    while(a>0):
        rem=a%10
        arm=arm+rem**leng
        a//=10
    if(temp==arm):
        print(temp," is an Armstrong Number")
    else:
        print(temp," is not an Armstrong Number")

num=int(input("Enter a Number : "))
arm(num)
