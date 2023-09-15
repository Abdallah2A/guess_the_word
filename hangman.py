import random
import tkinter as tk
from tkinter import messagebox

def guess_letter():
    global x
    letter = entry.get()

    # Check if the input is a single letter
    if len(letter) != 1 or not letter.isalpha():
        messagebox.showwarning("Invalid Input", "Please enter a single letter.")
        entry.delete(0, tk.END)
        return

    if letter not in word:
        x += 1
        lives_label.config(text="Lives remaining: {}".format(5 - x))
        message = "Wrong guess! You have {} life(s) remaining.".format(5 - x)
        messagebox.showinfo("Incorrect Guess", message)
    else:
        for i in range(len(word)):
            if letter == word[i]:
                dash[i] = letter
        guess = "".join(dash)
        label_guess.config(text=guess)

    # Check if the word has been completely guessed
    if "_" not in dash:
        messagebox.showinfo("Congratulations", "You've won the game!")
        root.quit()

    # Check if the player has run out of lives
    if x >= 5:
        messagebox.showinfo("Game Over", "You've run out of lives! The word was '{}'.".format(word))
        root.quit()

words = ["hangman", "fatman", "fitman", "batman", "ironman", "spiderman", "superman"]
word = random.choice(words)
dash = ["_"] * len(word)
x = 0

# Create the main window
root = tk.Tk()
root.title("Guess Game")

# Label for instruction
label_instruction = tk.Label(root, text="Guess a letter:")
label_instruction.pack(pady=(10, 0))

# Entry field for user input
entry = tk.Entry(root, font=('Arial', 16))
entry.pack(pady=(0, 10))

# Button to submit guess
button_guess = tk.Button(root, text="Guess", command=guess_letter)
button_guess.pack()

# Label to display the current state of the word
label_guess = tk.Label(root, text=" ".join(dash), font=('Arial', 16))
label_guess.pack(pady=(10, 0))

# Label to display the remaining lives
lives_label = tk.Label(root, text="Lives remaining: 5", font=('Arial', 12, 'bold'))
lives_label.pack()

# Start the main event loop
root.mainloop()