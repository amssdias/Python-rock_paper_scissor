import random

def main():
    rps = ["rock", "paper", "scissor"]
    x = random.choice(rps)
    y = str(input("Choose: rock, paper or scissor: ")).lower()

    if y not in rps:
        while y not in rps:
            y = str(input("Choose: rock, paper or scissor: ")).lower()
        
    print(f"I choose {x}")

    if y == "rock":

        if x == "rock":
            print("Tie!")

        elif x == "scissor":
            print("You win!")
        
        elif x == "paper":
            print("You lose!")

    elif y == "paper":

        if x == "rock":
            print("You win!")

        elif x == "scissor":
            print("You lose!")
        
        elif x == "paper":
            print("Tie!")

    elif y == "scissor":

        if x == "rock":
            print("You lose!")

        elif x == "scissor":
            print("Tie!")
        
        elif x == "paper":
            print("You Win!")
    

main()