import tkinter as tk
import random

# Game window
window = tk.Tk()
window.title("Stone Paper Scissors")
window.geometry("500x500")

player_score = 0
computer_score = 0


def play(player_choice):
    global player_score, computer_score

    choices = ["Stone", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    # Decide winner
    if player_choice == computer_choice:
        result = "Draw!"
    elif (
        (player_choice == "Stone" and computer_choice == "Scissors")
        or
        (player_choice == "Paper" and computer_choice == "Stone")
        or
        (player_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "You Win!"
        player_score += 1
    else:
        result = "Computer Wins!"
        computer_score += 1

    computer_label.config(
        text=f"Computer chose: {computer_choice}"
    )

    result_label.config(text=result)

    score_label.config(
        text=f"You: {player_score}    Computer: {computer_score}"
    )


# Heading
title = tk.Label(
    window,
    text="STONE PAPER SCISSORS",
    font=("Arial", 22, "bold")
)
title.pack(pady=30)

# Computer choice
computer_label = tk.Label(
    window,
    text="Computer chose: ---",
    font=("Arial", 14)
)
computer_label.pack(pady=10)

# Result
result_label = tk.Label(
    window,
    text="Choose your move!",
    font=("Arial", 18, "bold")
)
result_label.pack(pady=20)

# Buttons
button_frame = tk.Frame(window)
button_frame.pack(pady=20)

stone_button = tk.Button(
    button_frame,
    text="🪨 Stone",
    font=("Arial", 14),
    width=10,
    command=lambda: play("Stone")
)
stone_button.grid(row=0, column=0, padx=5)

paper_button = tk.Button(
    button_frame,
    text="📄 Paper",
    font=("Arial", 14),
    width=10,
    command=lambda: play("Paper")
)
paper_button.grid(row=0, column=1, padx=5)

scissors_button = tk.Button(
    button_frame,
    text="✂️ Scissors",
    font=("Arial", 14),
    width=10,
    command=lambda: play("Scissors")
)
scissors_button.grid(row=0, column=2, padx=5)

# Score
score_label = tk.Label(
    window,
    text="You: 0    Computer: 0",
    font=("Arial", 16, "bold")
)
score_label.pack(pady=30)

window.mainloop()