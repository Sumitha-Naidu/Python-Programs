#Write a function that takes a character and checks whether it is a Consonant or Vowel

vowel_list = ['A','a','E','e','I','i','O','o','U','u']
ch=input("Enter a character : ")
if ch in vowel_list:
    print(ch," is a Vowel")
else:
    print(ch," is a Consonant")
