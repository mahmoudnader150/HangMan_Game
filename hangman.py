import tkinter as tk
import random

#define list of random words
words = ['python','programming','computer','algorithm','function','variable','syntax']

#define the ASCII aret for hangman
hangman_art = [
    "   +---+\n   |   |\n       |\n       |\n       |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n       |\n       |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n   |   |\n       |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n  /|   |\n       |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n  /|\\  |\n       |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n  /|\\  |\n  /    |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n  /|\\  |\n  / \\  |\n       |\n========="
]

#define function to choose random word from a list
def choose_word():
    return random.choice(words)

#define func to update hangman ASCII art
def update_hangman(mistakes):
    hangman_label.config(text=hangman_art[mistakes])

root = tk.Tk()
root.title("Hangman")

hangman_label = tk.Label(root,font=("CourierK",16))
hangman_label.grid(row=0, column=0)

word = choose_word()
word_with_blanks = '_' * len(word)
word_label = tk.Label(root,text=word_with_blanks,font=("Arial",24))
word_label.grid(row=1,column=0)

#create guess entry and button
guess_entry = tk.Entry(root,width=3,font=("Arial",24))
guess_entry.grid(row=2,column=0)
guess_button=tk.Button(root,text="Guess",font=("Arial",12))
guess_button.grid(row=2,column=1)



#start event loop
root.mainloop()

      