from tkinter import *
import tkinter as tk
import pygame as py
import random

# Initialize the Pygame module
py.init()

user_name = ""
computer_wins = 0
master = None  # Store the master window globally
result_label = None  # Define result_label as a global variable
scores_label = None
play_again_button = None  # Define play_again_button as a global variable

# Function for the Rock, Paper, Scissors game
def play_rps(player_choice):
    global user_wins, computer_wins, ties, master, result_label, scores_label, play_again_button
    choices = {1: "Rock 🪨", 2: "Paper 📄", 3: "Scissors ✂️"}
    computer_choice = random.randint(1, 3)  # Randomly generates Python's choice

    result_text = ""

    # Determine the result of the game based on the player's choice and Python's choice
    if player_choice == computer_choice:
        result_text = "Tie game! 🤯"
        ties += 1
    elif (player_choice - computer_choice) % 3 == 1:
        result_text = "You win! 😁"
        user_wins += 1
    else:
        result_text = "Python wins! 🐍"
        # Play hissing sound when the computer wins
        py.mixer.Sound("C:\\Users\\veteran\\Downloads\\snake-hissing-6092.mp3").play()
        computer_wins += 1

    # Update the result label with the game outcome
    result_label.config(text=f"You chose {choices[player_choice]}. Python chose {choices[computer_choice]}.\n{result_text}")
    update_scores()

    # Check if either the user or the computer has reached 15 wins
    if user_wins == 15 or computer_wins == 15:
        end_game()
    else:
        play_again_button.config(state=DISABLED)  # Disable the "Play Again" button

# Function to update the score labels
def update_scores():
    global user_name, computer_wins, scores_label, play_again_button
    user_wins_label = f"{user_name}'s Wins: {user_wins}"
    computer_wins_label = f"{computer_wins} Python Wins"
    ties_label = f"Ties: {ties}"

    scores_label.config(text=f"{user_wins_label} | {computer_wins_label} | {ties_label}")

    # Check if either player has reached 15 wins to enable the "Play Again" button
    if user_wins == 15 or computer_wins == 15:
        play_again_button.config(state=NORMAL)  # Enable the "Play Again" button
        disable_buttons()  # Disable Rock, Paper, Scissors buttons
    else:
        play_again_button.config(state=DISABLED)  # Disable the "Play Again" button
        enable_buttons()  # Enable Rock, Paper, Scissors buttons

# Function to disable Rock, Paper, Scissors buttons
def disable_buttons():
    global rock_button, paper_button, scissors_button
    rock_button.config(state=DISABLED)
    paper_button.config(state=DISABLED)
    scissors_button.config(state=DISABLED)

# Function to enable Rock, Paper, Scissors buttons
def enable_buttons():
    global rock_button, paper_button, scissors_button
    rock_button.config(state=NORMAL)
    paper_button.config(state=NORMAL)
    scissors_button.config(state=NORMAL)

# Function triggered when a button (Rock, Paper, or Scissors) is clicked
def on_button_click(choice):
    play_rps(choice)  # Calls the play_rps function with the chosen value (1, 2, or 3)

# Function to start the Rock, Paper, Scissors game
def start_game(name_entry):
    global user_name, computer_wins, master, result_label, scores_label, play_again_button
    user_name = name_entry.get()
    start_screen.destroy()
    create_main_window()

# Function to create the main window for the game
def create_main_window():
    global user_wins, computer_wins, ties, master, result_label, scores_label, play_again_button

    # Create the main window
    master = Tk()
    master.title("Rock Paper Scissors")

    # Initialize scores
    user_wins = 0
    computer_wins = 0
    ties = 0

    intro_label = Label(master, text=f"\n🐍 First to 15 wins, Let's go {user_name}! Rock, paper, scissorsss shoot!\n", font=("Arial", 14))
    intro_label.pack()

    global button_frame
    button_frame = Frame(master)
    button_frame.pack()

    # Create buttons for Rock, Paper, and Scissors
    global rock_button, paper_button, scissors_button
    rock_button = Button(button_frame, text="Rock 🪨", command=lambda: on_button_click(1))
    rock_button.grid(row=0, column=0, padx=10, pady=5)

    paper_button = Button(button_frame, text="Paper 📄", command=lambda: on_button_click(2))
    paper_button.grid(row=0, column=1, padx=10, pady=5)

    scissors_button = Button(button_frame, text="Scissors ✂️", command=lambda: on_button_click(3))
    scissors_button.grid(row=0, column=2, padx=10, pady=5)

    global result_label
    result_label = Label(master, text="", font=("Arial", 12))
    result_label.pack()

    global scores_label
    scores_label = Label(master, text="User Wins: 0 | Computer Wins: 0 | Ties: 0", font=("Arial", 12))
    scores_label.pack()

    global winner_label
    winner_label = Label(master, text="", font=("Arial", 14))
    winner_label.pack()

    global play_again_button
    play_again_button = Button(master, text="Play Again", command=restart_game, state=DISABLED)
    play_again_button.pack()

    quit_button = Button(master, text="Quit", command=master.destroy)
    quit_button.pack()

    # Start the main event loop for the GUI

    # Load and play background music on a loop
    py.mixer.music.load(r'C:\Users\veteran\Downloads\Monkeys-Spinning-Monkeys(chosic.com).mp3')
    py.mixer.music.play(-1)  # -1 makes the music loop indefinitely

    master.mainloop()

# Function to end the game and ask the user if they want to play again
def end_game():
    global user_wins, computer_wins, master, result_label, scores_label, play_again_button
    winner = ""
    if user_wins == 15:
        winner = f"{user_name} wins the game!\n {user_name} is now the new venom free champion! 🎉"
        # Play the MP3 file when the user wins
        py.mixer.music.load(r"C:\Users\veteran\Downloads\short-crowd-cheer-6713.mp3")
        py.mixer.music.play()
    else:
       winner = f"Python wins the game!\n Wait watch out {user_name}, Python is about to strike! 😨"
        # Check if the computer has won and play the additional MP3 file
    if computer_wins == 15:
            py.mixer.music.load(r'C:\Users\veteran\Downloads\Snake Strike - QuickSounds.com.mp3')
            py.mixer.music.play()

    winner_label.config(text=winner)
    winner_label.pack()



# Function to restart the game
def restart_game():
    global user_wins, computer_wins, ties, master, result_label, scores_label, play_again_button, rock_button, paper_button, scissors_button  # Add play_again_button to global variables
    user_wins = 0
    computer_wins = 0
    ties = 0
    result_label.config(text="")  # Clear the result label
    scores_label.config(text="User Wins: 0 | Computer Wins: 0 | Ties: 0")
    winner_label.config(text="")
    play_again_button.config(state=NORMAL)  # Enable the "Play Again" button
    enable_buttons()  # Enable Rock, Paper, Scissors buttons
    show_buttons()  # Show the buttons

    # Load and play background music on a loop after restarting the game
    py.mixer.music.load(r'C:\Users\veteran\Downloads\Monkeys-Spinning-Monkeys(chosic.com).mp3')
    py.mixer.music.play(-1)  # -1 makes the music loop indefinitely



# Function to hide Rock, Paper, and Scissors buttons
def hide_buttons():
    global rock_button, paper_button, scissors_button
    rock_button.destroy()
    paper_button.destroy()
    scissors_button.destroy()

# Function to show Rock, Paper, and Scissors buttons
def show_buttons():
    global rock_button, paper_button, scissors_button
    rock_button.grid(row=0, column=0, padx=10, pady=5)
    paper_button.grid(row=0, column=1, padx=10, pady=5)
    scissors_button.grid(row=0, column=2, padx=10, pady=5)


# Create the start screen
start_screen = Tk()
start_screen.title("Rock Paper Scissors - Start Screen")

name_label = Label(start_screen, text="What's your name?")
name_label.pack()

name_entry = Entry(start_screen)
name_entry.pack()

start_button = Button(start_screen, text="Start Game", command=lambda: start_game(name_entry))
start_button.pack()

start_screen.mainloop()
