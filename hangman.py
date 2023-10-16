import tkinter as tk
import random

# Define list of random words
words = [
    'python', 'programming', 'computer', 'algorithm', 'function', 'variable', 'syntax',
    'hangman', 'language', 'learning', 'development', 'challenge', 'application', 'knowledge',
    'data', 'machine', 'intelligence', 'interface', 'graphics', 'network', 'security', 'authentication',
    'encryption', 'database', 'framework', 'opensource', 'repository', 'version', 'control', 'library',
    'education', 'platform', 'operating', 'system', 'communication', 'hardware', 'software', 'internet',
    'browser', 'website', 'protocol', 'responsive', 'design', 'responsive', 'optimization', 'performance'
]

# Define the ASCII art for hangman
hangman_art = [
    "   +---+\n   |   |\n       |\n       |\n       |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n       |\n       |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n   |   |\n       |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n  /|   |\n       |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n  /|\\  |\n       |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n  /|\\  |\n  /    |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n  /|\\  |\n  / \\  |\n       |\n========="
]

# Define function to choose a random word from a list
def choose_word():
    return random.choice(words)

# Define function to update hangman ASCII art
def update_hangman(mistakes):
    hangman_label.config(text=hangman_art[mistakes])

# Define a function to check if the guess is correct
def check_guess(guess):
    global word
    global word_with_blanks
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                word_with_blanks = word_with_blanks[:i] + guess + word_with_blanks[i+1:]
        word_label.config(text=word_with_blanks)
        if '_' not in word_with_blanks:
            end_game("Win")
    else:
        global mistakes
        mistakes += 1
        update_hangman(mistakes)
        if mistakes == 6:
            end_game("Lose")


root = tk.Tk()
root.title("Hangman")
# Define a function to reset the game
def reset_game():
    global word, word_with_blanks, mistakes
    word = choose_word()
    word_with_blanks = '_' * len(word)
    word_label.config(text=word_with_blanks)
    mistakes = 0
    update_hangman(mistakes)
    result_label.config(text="")
    guess_entry.config(state="normal")
    guess_button.config(state="normal")
    play_again_button.config(state="disabled")
    
# Create a "Play again" button
play_again_button = tk.Button(root, text="Play again", font=("Arial", 12), state="disabled", command=reset_game)
play_again_button.grid(row=3, column=1)    

#define end game function
def end_game(result):
    guess_entry.config(state="disabled")
    guess_button.config(state="disabled")
    play_again_button.config(state="normal")

    if result == "Win":
        result_text = "You Win!"
    else:
        result_text = "You Lose, The Word was " + word
    result_label.config(text=result_text)



hangman_label = tk.Label(root, font=("Courier", 16))

hangman_label.grid(row=0, column=0)

word = choose_word()
word_with_blanks = '_' * len(word)
word_label = tk.Label(root, text=word_with_blanks, font=("Arial", 24))
word_label.grid(row=1, column=0)

# Create guess entry and button
guess_entry = tk.Entry(root, width=3, font=("Arial", 24))
guess_entry.grid(row=2, column=0)
guess_button = tk.Button(root, text="Guess", font=("Arial", 12), command=lambda: check_guess(guess_entry.get()))
guess_button.grid(row=2, column=1)

# Create a result label
result_label = tk.Label(root, font=("Arial", 24))
result_label.grid(row=3, column=0)

# Initialize the game
mistakes = 0
update_hangman(mistakes)

# Start event loop
root.mainloop()
