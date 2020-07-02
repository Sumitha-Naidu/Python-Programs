#Create a program that asks the user to enter their name and their age. Print out a
#message addressed to them that tells them the year that they will turn 100 years
#old.


import datetime

name=input("Enter your Name : ")
age=int(input("Enter your Age : "))
d=datetime.datetime.today()
print(d.year)
r=100-age
year=d.year+r
print("Very Glad to say you that "+name+" you will be 100 years old in the Year ",year)
