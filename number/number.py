import tkinter as tk
import random
from tkinter import messagebox

# Generate a random number between 1 and 100
LOWER = 1
UPPER = 100
computer_guess = random.randint(LOWER, UPPER)

window = tk.Tk()

# Function to toggle fullscreen
def toggle_fullscreen(event=None):
    state = not window.attributes('-fullscreen')
    window.attributes('-fullscreen', state)
    if state:
        window.attributes('-zoomed', True)  # For Windows systems to maximize window
    else:
        window.attributes('-zoomed', False)

# Function to minimize window
def minimize_window(event=None):
    window.iconify()

# Bind keys to functions
window.bind('<F11>', toggle_fullscreen)  # Bind F11 key to toggle fullscreen
window.bind('<Escape>', toggle_fullscreen)  # Bind Escape key to exit fullscreen
window.bind('<F10>', minimize_window)  # Bind F10 key to minimize window

window.title('Number Guessing Game')
window.config(bg='#BFCFE7')

# Define colors
background_color = '#BFCFE7'
button_color = '#4A90E2'
button_hover_color = '#0072E3'
text_color = '#1A1A1A'
win_color = '#28A745'
lose_color = '#DC3545'

def attempts_check():
    global attempts
    attempts = scale_attempts.get()
    attempts_btn.config(state=tk.DISABLED)
    guess_btn.config(state=tk.NORMAL)

def showexit():
    result = messagebox.askquestion('Exit', 'Do you want to exit the program?')
    if result == "yes":
        window.destroy()

def restart():
    global computer_guess
    global attempts

    computer_guess = random.randint(LOWER, UPPER)
    guess_btn.config(state=tk.DISABLED)
    attempts_btn.config(state=tk.NORMAL)
    win_lose_label.set("")
    user_guess_label.set("")

def guessnumber():
    global user
    global attempts
    attempts -= 1

    try:
        user_guess = int(user.get())
        if user_guess > UPPER or user_guess < LOWER:
            messagebox.showwarning('Warning', f'Please enter a number between {LOWER} and {UPPER}')
            attempts += 1
        elif user_guess == computer_guess:
            win_lose_label.set("Congratulations! You won!")
            user_guess_label.set('')
            label_win_lose_.config(fg=win_color, font=('Times New Roman', 17, 'bold'))
            label_win_lose_.place(x=200, y=250)
            guess_btn.config(state=tk.DISABLED)
        elif attempts == 0:
            win_lose_label.set(f"You lost! The correct number was {computer_guess}")
            user_guess_label.set('')
            label_win_lose_.config(fg=lose_color, font=('Times New Roman', 17, 'bold'))
            label_win_lose_.place(x=175, y=250)
            guess_btn.config(state=tk.DISABLED)
        elif user_guess < computer_guess:
            user_guess_label.set(f'Your guess is too low.\n\nYou have {attempts} attempts left.')
        else:
            user_guess_label.set(f'Your guess is too high.\n\nYou have {attempts} attempts left.')

    except ValueError:
        messagebox.showwarning('Warning', 'Please enter a valid number between 1 and 100')
        attempts += 1

label = tk.Label(window, text=f"Please guess a number between {LOWER} and {UPPER}:", font=('Times New Roman', 13, 'bold'), anchor="center", bg=background_color, fg=text_color)
label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

user_variable = tk.StringVar()
user = tk.Entry(window, textvariable=user_variable, font=('Times New Roman', 14), borderwidth=5, bg='#FFFFFF', fg=text_color)
user.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

user_guess_label = tk.StringVar()
label_user_guess = tk.Label(window, textvariable=user_guess_label, font=('Times New Roman', 17), bg=background_color, fg=text_color)
label_user_guess.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

win_lose_label = tk.StringVar()
label_win_lose_ = tk.Label(window, textvariable=win_lose_label, font=('Times New Roman', 14), bg=background_color, fg=text_color)

guess_btn = tk.Button(window, text="Guess", font=('Times New Roman', 14), command=guessnumber, bg=button_color, fg='#FFFFFF', activebackground=button_hover_color, borderwidth=5)
guess_btn.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
guess_btn.config(state=tk.DISABLED)

restart_btn = tk.Button(window, text="Restart", font=('Times New Roman', 14), command=restart, bg=button_color, fg='#FFFFFF', activebackground=button_hover_color, borderwidth=5)
restart_btn.place(relx=0.3, rely=0.6, anchor=tk.CENTER)

exit_btn = tk.Button(window, text="Exit", font=('Times New Roman', 14), command=showexit, bg=button_color, fg='#FFFFFF', activebackground=button_hover_color, borderwidth=5)
exit_btn.place(relx=0.7, rely=0.6, anchor=tk.CENTER)

scale_attempts = tk.Scale(window, from_=5, to=10, orient=tk.HORIZONTAL, bg=background_color, fg=text_color, troughcolor=button_color, borderwidth=5)
scale_attempts.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

label_attempts = tk.Label(window, text="Please select your number of attempts:", font=('Times New Roman', 11, 'bold'), bg=background_color, fg=text_color)
label_attempts.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

attempts_btn = tk.Button(window, text='Select', font=('Times New Roman', 12, 'bold'), command=attempts_check, bg=button_color, fg='#FFFFFF', activebackground=button_hover_color, borderwidth=5)
attempts_btn.place(relx=0.5, rely=0.85, anchor=tk.CENTER)

window.mainloop()
