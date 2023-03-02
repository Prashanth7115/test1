
userNum = 0

import random

def main():

    # initialization
    high = 0
    low = 0
    win = 0
    number = random.randint(1, 100)
    userNum = 0

    while (userNum != number):
        # input
        userNum = int(input("Please guess a number between 1 and 100: "))

        # if/else check
        if userNum > number:
            message = "Too high, try again."
            high += 1
        elif userNum == number:


            message = "You got it correct! Congratulations!"
            win += 1
        else:
            message = "Too low, try again."
            low += 1
    print()
    print(message)

    # loop
   # while message != "You got it correct! Congratulations!":

    # display total
    print()
    print("Number of times too high: ", high)
    print("Number of times too low: ", low)
    print("Total number of guesses: ", (high + low + win))


    print("You win")

main()




#Source: https://stackoverflow.com/questions/53038112


