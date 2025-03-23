import sys
import time

def sleep(sec):
    time.sleep(sec)

def main():
    print("I can guess what number you are thinking of...")
    sleep(1.5)
    number = input("Enter the number you are thinking of: ")
    if any(char.isalpha() for char in number):
        sleep(1)
        print("\n Your suppose to enter a number, not letters 😞😞")
    else:
        sleep(2)
        for i in range(101):
            sys.stdout.write('\r')
            sys.stdout.write("[%-10s] %d%%" % ('='*i, 1*i))
            sys.stdout.flush()
            sleep(0.1)
    
        print("\n Analysing brainwaves...")
        sleep(4.5)
        print("\n You are thinking of the number " + str(number) + ".")
        sleep(3.5)
        print("\n I'm so smart 🤣🤣")
        sys.exit()

if __name__ == '__main__':
    main()
