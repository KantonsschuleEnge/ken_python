#!/usr/bin/python3

alph='abcdefghijklmnopqrstuvwxyz'

def verschieben(s):
    encoded=''
    for letter in s:
        if letter in alph:
            encoded += alph[(alph.find(letter)+2)% len(alph)]
        else:
            encoded += letter
    return encoded

def clean(s):
    for letter in s:
        if letter in alph:
            print(letter)
        else:
            pass

def findBodyguard(s):
    for i in range(len(s)):
        if s[i].isupper() and s[i+1].isupper() and s[i+2].isupper() and s[i+3].islower() and s[i+4].isupper() and s[i+5].isupper() and s[i+6].isupper():
            if s[i-1]!=s[i] or s[i+7]!=s[i+8]:
                print(s[i:i+7])


file = open('quelltext4.txt','r')

code = file.read()

findBodyguard(code)

file.close()



