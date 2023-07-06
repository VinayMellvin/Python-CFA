#!|usr|bin|env python

import random 

def main():
    """Start a music guessing genre between hip hop,jazz,pop music,electronic music,country song,rock."""
    print("Guess the music Genre.")
 
    genre =("hip hop","jazz","pop music","electronic music","country song","rock")
    x = random.choice(genre)
    guess = None
    
    while x != guess:
        
        guess = str(input("Pick a music genre. "))
        
        if x == guess:
            print("Correct.")
        else:
            print("Wrong.")
main()            
