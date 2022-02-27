#!/usr/bin/env python
# coding: utf-8

# In[2]:


import re
import random
def wordList():
    file = open('words.txt', 'r')
    words = list(file.read().split())
    filtered = []
    for word in words:
        if len(word) == 5:
            filtered.append(word)
    return filtered

def fn_Matcher(theWord,nextGuess):
    match=''
    for i in range(5):
        if nextGuess[i]==theWord[i]:
            match+='1'
        elif nextGuess[i] in theWord:
            match+='2'
        else:
            match+='3'
    return match

def fn_Wordle_Player(intMatcher,words,nextGuess):
    
    a=''
    for i in range(0,5):
        
        j=intMatcher[i]
        if j=='1':
            a+=nextGuess[i]
        else:
            a+='.'
    x = re.compile(a)
    filtered = [i for i in words if  x.match(i)]
    b=''
   
    word=[]
    for i in range(0,5):
        
        j=intMatcher[i]
        if j=='3':
            b=nextGuess[i]
            
            count=0
            for k in filtered:
                count=0
                for l in range(0,5):
                    if k[l]==b:
                        count+=1
                if count>0:
                    continue
                else:
                    word.append(k)
        
              
    u=random.choice(word)
    return u,word
            
            
if __name__=='__main__':
    theWord=input('Enter word of the day: ').upper()
    words=wordList()
    while(len(theWord)!=5 or (theWord not in words)):
        theWord=(input('Please input a valid 5 letter word: ')).upper()
    for i in range(19):
        if i==0:
            nextGuess='ADIEU'.upper()
        else:
            nextGuess,words=fn_Wordle_Player(intMatcher,words,nextGuess)
        if nextGuess in words and len(nextGuess)==5:
            if nextGuess ==theWord:
                print(nextGuess)
                print("Word found on attempt",i+1)
                break
            else:
                intMatcher=fn_Matcher(theWord,nextGuess)
                print(nextGuess)
                print("Word does not match, Feedback pattern returned: ",intMatcher)
                continue
        else:
            print(nextGuess,"Not a valid word")
            break
            
    else:
        print("Word not found. Correct word is",theWord)

