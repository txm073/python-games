import random
import time

score, cpu_score = 0, 0 

try:
    while True:
        choices = ["rock", "paper", "scissors"]

        choice = input("Choose rock, paper or scissors: ").lower().strip()
        while choice not in choices:
            choice = input("You must choose either rock, paper or scissors: ")

        tie = False

        cpu_choice = random.choice(choices)
        players_choices = [choice, cpu_choice]

        if "rock" in players_choices and "paper" in players_choices:
            winner = players_choices.index("paper")

        if "rock" in players_choices and "scissors" in players_choices:
            winner = players_choices.index("rock")

        if "scissors" in players_choices and "paper" in players_choices:
            winner = players_choices.index("scissors")

        elif len(set(players_choices)) == 1:
            tie = True

        if tie:
            print("Tie!")
        else:
            if winner == 0:
                print("You win!")
                score += 1
            else:
                print("Computer wins!")
                cpu_score += 1

except KeyboardInterrupt:
    print("\nGame Over!")
    time.sleep(1)
    print(f"You scored {score} points!")
    print(f"The computer scored {cpu_score} points!")
    
