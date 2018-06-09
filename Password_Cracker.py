#!/usr/bin/env python
# -*- coding: utf-8 -*-

import string
ALLOWED_CHARACTERS = string.ascii_lowercase+string.digits
NUMBER_OF_CHARACTERS = len(ALLOWED_CHARACTERS)
#w = open("rezults.txt", "a")
def characterToIndex(char):
    return ALLOWED_CHARACTERS.index(char)

def indexToCharacter(index):
    if NUMBER_OF_CHARACTERS <= index:
        raise ValueError("Index out of range.")
    else:
        return ALLOWED_CHARACTERS[index]

def next(string):
    if len(string) <= 0:
        string.append(indexToCharacter(0))
    else:
        string[0] = indexToCharacter((characterToIndex(string[0]) + 1) % NUMBER_OF_CHARACTERS)
        if characterToIndex(string[0]) is 0:
            return list(string[0]) + next(string[1:])
    return string
import time
import datetime

def test_for_dictionary(password):
    with open("english.txt","r") as f:
        w=open("rezults.txt","a")
        x=f.readline()
        x=x.strip()
        x=x.lower()
        while(x):
            #print( "Testing if ",password," equals ",x)
            if(x==password):
                print("Dictionary attack password is ",x)
                w.write (" -> Discoverd with Dictionary ")
                w.write(x)
                return 1
            x=f.readline()
            x = x.strip()
            x = x.lower()
        w.close()
        return 0

def brute_force(x):
    sequence = list()
    cur_len = 1
    start=datetime.datetime.now()
    time_break=time.time()+60*5
    w=open("rezults.txt","a")
    #print(ALLOWED_CHARACTERS)
    '''
    Digit=0
    Alfa=1
    Digit+alpha=2
    '''
    mode=0
    global ALLOWED_CHARACTERS
    global NUMBER_OF_CHARACTERS
    ALLOWED_CHARACTERS=string.digits
    NUMBER_OF_CHARACTERS=len(ALLOWED_CHARACTERS)
    mode=0
    '''
    0 -> digits
    1 -> alfa
    2 -> hybrid
    '''
    while True:
        sequence = next(sequence)
        test = "".join(sequence)
        if (len(test) > cur_len):
            sequence=list()
            if mode == 0:
                ALLOWED_CHARACTERS=string.ascii_lowercase
                mode=1
            else:
                if mode==1:
                    ALLOWED_CHARACTERS=string.ascii_lowercase+string.digits
                    mode=2
                else:
                    if mode==2:
                        ALLOWED_CHARACTERS=string.digits
                        mode=0
                        cur_len = len(test)
                        print(cur_len)
            NUMBER_OF_CHARACTERS=len(ALLOWED_CHARACTERS)
        if(cur_len > 6 or time.time()>time_break):
            w.write(" ##This takes too long, ignoring##")
            w.close()
            return 0


            #print(ALLOWED_CHARACTERS)

        #print(test)
        #from time import sleep
        #sleep(0.05)
        if (    test == x):
            print("Brute Force attack Password is ", test)
            w.write(" -> Found with brute force ")
            w.write(test)
            finish = datetime.datetime.now()
            print("it took ", finish - start, " seconds")
            sequence = list()
            w.close()
            return 1





def main():
    all_program_start=datetime.datetime.now()
    nr_pass_found=0
    f = open("passwords.txt", "r")
    x="s"
    while(x):
        w=open("rezults.txt","a")
        x = f.readline()
        start=datetime.datetime.now()
        print("Password to find", x)
        w.write("Passwrod to find is ")
        w.write(x)
        w.close()
        x=x.strip()
        found=test_for_dictionary(x)
        if found==0:
            if brute_force(x):
                nr_pass_found+=1

        finish = datetime.datetime.now()
        w=open("rezults.txt","a")
        w.write(" And it took ")
        w.write(str(finish -start))
        w.write(" seconds \n")
        w.close()
    all_program_finish=datetime.datetime.now()
    w= open("rezults.txt","a")
    w.write("\n Found ")
    w.write(nr_pass_found)
    w.write(" in ")
    w.write(str(all_program_finish-all_program_start))
    w.close()
if __name__ == "__main__":
    main()