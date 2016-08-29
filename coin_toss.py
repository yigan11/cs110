#This program simulates 10 tosses of a coin
import random

#Constants
HEADS = 1
TALLS = 2
TOSSES = 10

def main():
    for toss in range (TOSSES):
        #Simulate the coin toss.
        if random.randint(HEADS,TALLS) == HEADS:
            print ('Heads')
        else:
            print('Tails')

# Call the main function.
main()
