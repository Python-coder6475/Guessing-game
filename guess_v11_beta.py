import random
import tkinter as tk

target_number = None
guess_count = 0
done = 0

if done == 0:
    def custom():
        def game_input():
            global amount, range1, range2
            amount = int(amount_entry.get())
            range1 = int(range1_entry.get())
            range2 = int(range2_entry.get())
            range_check()

        def range_check():
            if range1 > range2:
                result_label.config(text="The bottom range is more than the top range. Please fix this.")
            elif range2 < range1:
                result_label.config(text="The top range is less than the bottom range. Please fix this.")
            elif range1 == range2:
                result_label.config(text="Both ranges equal each other. Please fix this.")
            else:
                result_label.config(text=f"The range is {range1} through {range2}. The amount of guesses is {amount}.")
                play_game()

        def play_game():
            global target_number
            target_number = random.randint(range1, range2)

            def check_guess():
                global target_number, guess_count, done
                guess = int(guess_entry.get())

                if guess > range2:
                    result_label.config(text="Number is too high.")
                    guess_count = guess_count + 1
                elif guess < range1:
                    result_label.config(text="Number is too low.")
                    guess_count = guess_count + 1
                elif guess == target_number:
                    result_label.config(text="Great guess! You got it!")
                    guess_count = guess_count + 1
                    target_number = random.randint(range1, range2)
                elif abs(guess - target_number) <= 2:
                    result_label.config(text="So close! You almost had it!")
                    guess_count = guess_count + 1
                elif abs(guess - target_number) <= 4:
                    result_label.config(text="Close!")
                    guess_count = guess_count + 1
                elif guess_count > amount:
                    result_label.config(text="You've run out of guesses. If you want more just restart the program.")
                    done = 1
                else:
                    result_label.config(text="Better luck next time!")
                    guess_count = guess_count + 1

            instruction_window = tk.Toplevel()
            instruction_window.geometry("300x250")
            instruction_window.title("Instructions")
            guess_window = tk.Toplevel()
            guess_window.geometry("200x150")
            guess_window.title("Guess the Number")

            instruction_label = tk.Label(instruction_window, text="""1. Put a guess in the text box.
                                                                 2. Check your guess by pressing the check button.
                                                                 3. Keep guessing until you get the number.
                                                                 4. If you guess the number correctly it will change.
                                                                 5. Repeat.
                                                                 6. Have fun!""", wraplength=180)
            guess_label = tk.Label(guess_window, text="Guess a number:")
            guess_entry = tk.Entry(guess_window)
            check_button = tk.Button(guess_window, text="Check", command=check_guess)
            result_label = tk.Label(guess_window, text="", wraplength=180)
            correct_number_label = tk.Label(guess_window, text="", wraplength=180)

            instruction_label.pack()
            guess_label.pack()
            guess_entry.pack()
            check_button.pack()
            result_label.pack()
            correct_number_label.pack()

        custom_window = tk.Toplevel()
        custom_window.geometry("300x200")
        custom_window.title("Customized Mode")

        amount_label = tk.Label(custom_window, text="Enter the number of guesses:")
        amount_entry = tk.Entry(custom_window)
        range1_label = tk.Label(custom_window, text="Enter the bottom range:")
        range1_entry = tk.Entry(custom_window)
        range2_label = tk.Label(custom_window, text="Enter the top range:")
        range2_entry = tk.Entry(custom_window)
        result_label = tk.Label(custom_window, text="", wraplength=250)

        play_button = tk.Button(custom_window, text="Play", command=game_input)

        amount_label.pack()
        amount_entry.pack()
        range1_label.pack()
        range1_entry.pack()
        range2_label.pack()
        range2_entry.pack()
        play_button.pack()
        result_label.pack()

    def timed():
        pass

    def start_custom():
        window.withdraw()
        custom()

    def start_timed():
        window.withdraw()
        timed()

    window = tk.Tk()
    window.geometry("200x150")
    window.title("Guessing Game")

    label = tk.Label(window, text="Guessing Game")
    label.pack()

    custom_button = tk.Button(window, text="Customized", command=start_custom)
    timed_button = tk.Button(window, text="Timed", command=start_timed)
    custom_button.pack()
    timed_button.pack()

    window.mainloop()
