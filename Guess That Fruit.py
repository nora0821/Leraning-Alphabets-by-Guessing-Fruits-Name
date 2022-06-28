#!/usr/bin/env python

import random

def main():
    """ Learning Alphabet with Game !."""
    print("Guess that fruit! You will be given an alphabet and you have to guess the fruit that start with that alphabet ")

    print( "\nPlease Start writing your answer with a CAPITAL letter" )

    fruit = [
        "cranberry",
       "cherry",
        "coconut"
       ]

    x = random.choice(fruit)
    
    guess = None

    while x != guess:

        guess = str(input("\nState a fruit that start with alphabet C ? "))
        
        if x == guess:
            print("You guessed {}. Cheers !! Correct!\U0001F601".format(guess))
            break
        else:
            print("You guessed {}. Oh No!. Try Again!\U0001F605".format(guess))


    fruit = [
        "Apple",
        "Avocado",
        "Apricot"
        ]

    x = random.choice(fruit)
    
    guess = None

    while x != guess:

        guess = str(input("State a fruit that start with alphabet A ? "))
        
        if x == guess:
            print("You guessed {}. Hurray! Correct!\U0001F602".format(guess))
            break
        else:
            print("You guessed {}. Haiyaa~!. Try Again!\U0001F600".format(guess))

    fruit = [
        "Banana",
        "Blueberry",
        "Blackcurrent"]

    x = random.choice(fruit)
    
    guess = None

    while x != guess:

        guess = str(input("State a fruit that start with alphabet B ? "))
        
        if x == guess:
            print("You guessed {}. Hurray! Correct!\U0001F607".format(guess))
            break
        else:
            print("You guessed {}. We Can Do This! Another One \U0001F923".format(guess))

    fruit = [
        "Dragonfruit",
        "Durian",
        "Date"]

    x = random.choice(fruit)
    
    guess = None

    while x != guess:

        guess = str(input("State a fruit that start with alphabet D ? "))
        
        if x == guess:
            print("You guessed {}. Hurray! Correct!\U0001F60D".format(guess))
            break
        else:
            print("You guessed {}. Never Give Up!. Try Again!:angry_face:".format(guess))

    fruit = [
        "Mango",
        "Mangosteen",
        "Melon"
        ]

    x = random.choice(fruit)
    
    guess = None

    while x != guess:

        guess = str(input("State a fruit that start with alphabet M ? "))
        
        if x == guess:
            print("You guessed {}. Hurray! Correct! \U0001F601".format(guess))
            break
        else:
            print("You guessed {}. Come On! !\U0001F612".format(guess))

    


        

main()
       

