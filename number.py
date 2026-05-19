import random
import tkinter as tk
from tkinter import messagebox

# GAME VARIABLES
secret = random.randint(1, 100)
attempts = 0
max_attempts = 7

def reset_game():
    global secret, attempts
    secret = random.randint(1, 100)
    attempts = 0
    output_label.config(text="Game Reset 🔁\nEnter Level")
    level_entry.delete(0, tk.END)
    entry.delete(0, tk.END)
    level_entry.focus()

def set_level(event=None):
    global max_attempts
    level = level_entry.get().lower()

    if level == "easy":
        max_attempts = 10
    elif level == "medium":
        max_attempts = 7
    elif level == "hard":
        max_attempts = 5
    else:
        max_attempts = 7
        output_label.config(text="Invalid level → medium set")

    output_label.config(text=f"Attempts: {max_attempts}")
    entry.focus()

def check_guess(event=None):
    global attempts

    try:
        guess = int(entry.get())
    except:
        output_label.config(text="Enter numbers only 😑")
        entry.delete(0, tk.END)
        return

    attempts += 1
    diff = abs(secret - guess)

    if guess > secret:
        msg = "Too High 🔴"
    elif guess < secret:
        msg = "Too Low 🔵"
    else:
        messagebox.showinfo("🎉 Win", f"You Win in {attempts}")
        reset_game()
        return

    if diff <= 5:
        hint = "Very Close 🔥"
    elif diff <= 10:
        hint = "Close 🙂"
    else:
        hint = "Far 😅"

    output_label.config(text=f"{msg}\n{hint}\nAttempts: {attempts}/{max_attempts}")

    entry.delete(0, tk.END)  # 🔥 auto clear

    if attempts == max_attempts:
        messagebox.showinfo("💀 Game Over", f"Number was {secret}")
        reset_game()

# WINDOW
root = tk.Tk()
root.title("🎮 Number Guess Game")
root.geometry("300x300")

# LEVEL
tk.Label(root, text="Enter Level", font=("Arial", 12)).pack()
level_entry = tk.Entry(root)
level_entry.pack()
level_entry.bind("<Return>", set_level)

# GUESS
tk.Label(root, text="Enter Number", font=("Arial", 12)).pack()
entry = tk.Entry(root)
entry.pack()
entry.bind("<Return>", check_guess)

# OUTPUT
output_label = tk.Label(root, text="Start Game", font=("Arial", 11))
output_label.pack(pady=10)

# BUTTONS
tk.Button(root, text="Reset 🔁", command=reset_game).pack()

root.mainloop()