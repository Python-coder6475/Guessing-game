import random

mode = input("Would you like a timed run or a customizable run?\n")
mode = mode.lower()
amount = 0
range2 = 0
range1 = 0

if mode == "customizable" or mode == "custom":
    def game_input():
        global amount, range1, range2
        amount = int(input("How many guesses would you like?\n"))
        range1 = int(input("What is the bottom range of the numbers that can be chosen?\n"))
        range2 = int(input("What is the top range of the numbers that can be chosen?\n"))
    game_input()

    def check():
        try:
            range1 = int(range1)
            range2 = int(range2)
        except ValueError:
            print("Please input numbers.\n")
            game_input()
    def range_input():
        global range1, range2
        range1 = int(input("What is the bottom range of the numbers that can be chosen?\n"))
        range2 = int(input("What is the top range of the numbers that can be chosen?\n"))
        range_check()
    def range_check():
            if range1 > range2:
                print("The bottom range is more than the top range. Please fix this.")
                range_input()
            elif range2 < range1:
                print("The top range is less than the bottom range. Please fix this.")
                range_input()
            elif range2 == range1:
                print("Both ranges  equal each other. Please fix this.")
                range_input()
    range_check()
    print("The range is", range1, "through", range2, ". The amount of guesses is", amount, ".")
    y = input("Please look over what you have inputted. If it is all correct type 'Y'\n")
    if y == "Y":
        for counter in range(amount):
            print("Guess a number between", range1, "and", range2,".")
            guess = input("What is your guess?\n")
            guess = int(guess)
            rand = random.randint(int(range1),int(range2))
            rand = str(rand)
            rand2 = rand.replace(" ", "", 100)
            guess = str(guess)
            guess2 = guess.replace(" ", "", 100)
            guess2 = int(guess)
            rand2 = int(rand2)
            guess2 = float(guess2)
            rand2 = float(rand2)
            print()
            def check_num():
                if guess2 > range2:
                    print("Number is too high.")
                elif guess2 < range1:
                    print("Number is too low")
                else:
                    print("Great guess!")
            if guess2 == rand2:
                print("Great job!")
                print("The number was ", rand2, "!")
            else:
                check_num()
                print("Better luck next time!")
                print("The number was ", rand2, ".")
elif mode == "timed" or mode == "timer":
    quit()