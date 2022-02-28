#!/usr/bin/env python
# coding: utf-8

# In[29]:


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
    valid=[]
    unvalid=[]
    for i in range(0,5):
        j=intMatcher[i]
        if j=='1' or j=='2':
            if nextGuess[i] not in valid:
                valid.append(nextGuess[i])
        elif j=='3':
            if nextGuess[i] not in unvalid:
                unvalid.append(nextGuess[i])
    Newfiltered=[]        
    for word in filtered:
        for j in unvalid:
            if j in word:
                filtered.remove(word)
                break
    for word in filtered:
        for j in range(len(valid)):
            if valid[j] in word and j==len(valid)-1:
                Newfiltered.append(word)
            elif valid[j] not in word:
                filtered.remove(word)
                break
    
    if len(Newfiltered)<=0 : 
        NewList=[]
        NewList=filtered
    else:
        NewList=Newfiltered
    guess=random.choice(NewList)
              
    
    return guess,NewList
            
            
if __name__=='__main__':
    theWord=input('Enter word of the day: ').upper()
    words=wordList()
    used=wordList()
    while(len(theWord)!=5 or (theWord not in words)):
        theWord=(input('Please input a valid 5 letter word: ')).upper()
    for i in range(19):
        if i==0:
            nextGuess='ADIEU'.upper()
        else:
            if nextGuess in words:
                words.remove(nextGuess)
            nextGuess,used=fn_Wordle_Player(intMatcher,used,nextGuess)
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

