import random

def get_computer_choice():
    choices = ["rock","paper","scissors"]
    return random.choice(choices)

def determine_winner(user,computer):
    if user == computer:
        return "tie"
    elif(user == "rock" and computer == "scissors") or \
        (user == "scissors" and computer == "paper") or \
        (user == "paper" and computer == "rock"): 
        return "win"
    else:
        return "lose"
    
def play_game():
    user_score = 0
    computer_score = 0

    print("\n🎮 Welcome to Rock-Paper-Scissors Game!")
    print("------------------------")

    while True:
        user = input("\n👉Enter your choice (rock/paper/scissors):").lower()

        if user not in ["rock","paper","scissors"]:
            print("❌ Invalid choice! Please try again.")
            continue

        computer = get_computer_choice()

        print(f"\n🧍 You chose:{user}")
        print(f"💻Computer chose: {computer}")

        result = determine_winner(user, computer)


        if result == "win":
            print("🎉You WIN!")
            user_score += 1
        elif result == "lose":
            print("😞You LOSE!")
            computer_score += 1
        else:
            print("🤝It's a TIE!")

        print(f"\n📊Score -> You: {user_score} | Computer:{computer_score}")
 
        play_again = input("\n🔁Do you want to play again? (yes/no):").lower()
        if play_again != "yes":
            print("\n👋Thanks for playing! Final Score:")
            print(f"➡You: {user_score} | Computer:{computer_score}")
            break

# Start the game
play_game()               
