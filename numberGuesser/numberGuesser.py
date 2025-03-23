import sys
import time



def sleep(sec):
    time.sleep(sec)

def display_progress_bar(duration):
    for i in range(101):
        sys.stdout.write('\r')
        sys.stdout.write("[%-10s] %d%%" % ('='*(i//10), i))
        sys.stdout.flush()
        sleep(duration / 100)
    print()

def main():
    know = False
    print("I can guess what number you are thinking of...")
    while True:
        know = True
        sleep(1.5)
        try:
            number = int(input("Enter the number you are thinking of: "))
        except ValueError:
            sleep(1)
            print("\nYou are supposed to enter a number, not letters 😞😞")
            continue

        sleep(2)
        display_progress_bar(10)
        
        print("\nAnalyzing brainwaves...")
        sleep(4.5)
        print("\nYou are thinking of the number " + str(number) + ".")
        sleep(3.5)
        print("\nI'm so smart 🤣🤣")

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            break

if __name__ == '__main__':
    main()
