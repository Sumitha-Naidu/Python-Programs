#A pangram is a sentence that contains all the letters of the English alphabet at
#least once, for example: The quick brown fox jumps over the lazy dog. Your task
#here is to write a function to check a sentence to see if it is a pangram or not.

import re

def panagram(sentence):
    alphalist='abcdefghijklmnopqrstuvwxyz'
    alphacount=0
    if(len(sentence)<26):
        return False
    else:
        sentence=re.sub('[^a-z]','',sentence)
    sentence=sentence.lower()
    for i in range(len(alphalist)):
        if(alphalist[i] in sentence):
            alphacount+=1
    if(alphacount==26):
        return True
    else:
        return False


sentence="The quick brown fox jumps over the lazy dog"
sentence=input("Enter a Sentence : ")
if(panagram(sentence)):
    print("Sentence is a Panagram")
else:
    print("Sentence is not a Panagram")
    
