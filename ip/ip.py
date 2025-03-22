import random as rand
import sys
import time
import logging
from colorama import Fore

logger = logging.getLogger(__name__)

def sleep(sec):
    time.sleep(sec)

def main():
    print("Starting service...")

    target = input("Input target phone number: ")

    if any(char.isalpha() for char in target):
        print("You have to enter an actual phone number.")
        sys.exit(1)
    else:
        print("Setting target phone number to " + target + "...")

        block = 1
        sleep(3)
        for i in range(6):
            print("Block #" + str(block) + " failed to connect.")
            block = block + 1
            sleep(1.5)
        
        time.sleep(4)
        print("Connection on Block #" + str(block) + " found!")
        sleep(2)
        print("Starting IP finder...")

        delay = rand.choice(
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
            )
        sleep(delay)
        one = str(rand.choice(range(1, 99)))
        two = str(rand.choice(range(1, 99)))
        three = str(rand.choice(range(1, 300)))
        four = str(rand.choice(range(1, 300)))

        str(print(one + "." + two + "." + three + "." + four))


if __name__ == '__main__':
    main()
