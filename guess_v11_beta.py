import random
import tkinter as tk

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
        else:
            result_label.config(text=f"The range is {range1} through {range2}. The amount of guesses is {amount}.")
            play_game()

    def play_game():
        def check_guess():
            guess = int(guess_entry.get())

            if guess > range2:
                result_label.config(text="Number is too high.")
            elif guess < range1:
                result_label.config(text="Number is too low.")
            elif guess == target_number:
                result_label.config(text="Great guess! You got it!")
            elif abs(guess - target_number) == 1 or abs(guess - target_number) == 2:
                result_label.config(text="So close! You almost had it!")
                correct_number_label.config(text=f"The correct number was {target_number}")
            elif abs(guess - target_number) == 3 or abs(guess - target_number) == 4:
                result_label.config(text="Close!")
                correct_number_label.config(text=f"The correct number was {target_number}")
            elif abs(guess - target_number) >= 5:
                result_label.config(text="Better luck next time!")
                correct_number_label.config(text=f"The correct number was {target_number}")
        target_number = random.randint(range1, range2)

        guess_window = tk.Toplevel()
        guess_window.geometry("200x150")
        guess_window.title("Guess the Number")

        guess_label = tk.Label(guess_window, text="Guess a number:")
        guess_entry = tk.Entry(guess_window)
        check_button = tk.Button(guess_window, text="Check", command=check_guess)
        result_label = tk.Label(guess_window, text="", wraplength=180)
        correct_number_label = tk.Label(guess_window, text="", wraplength=180)

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
