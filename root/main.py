import random

def get_cpu_choice():
    choices = ["rock", "paper", "scissors"]
    cpu_choice = random.choice(choices)
    return cpu_choice

def get_player_choice():
    while True:
        player_choice = input("Enter rock, paper, or scissors: ")
        if player_choice == "rock" or player_choice == "paper" or player_choice == "scissors":
            return player_choice

def check_winner(cpu_choice, player_choice):
    if player_choice == cpu_choice:
        winner = "Tie"
    elif cpu_choice == "rock":
        if player_choice == "paper":
            winner = "PLAYER"
        else:
            winner = "CPU"
    elif cpu_choice == "paper":
        if player_choice == "scissors":
            winner = "PLAYER"
        else:
            winner = "CPU"
    elif player_choice == "paper":
        winner = "CPU"
    else:
        winner = "PLAYER"
    return winner

cpu_choice = get_cpu_choice()
player_choice = get_player_choice()
winner = check_winner(cpu_choice, player_choice)
print(winner)