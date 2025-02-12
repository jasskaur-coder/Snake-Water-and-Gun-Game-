import random
import time
try:
    from colorama import Fore, Style
except ImportError:
    print("Installing required module...")
    import os
    os.system("pip install colorama")
    from colorama import Fore, Style

youDict = {"Snake": 1, "Water": -1, "Gun": 0}
reverseDict = {1: "🐍 Snake", -1: "💧 Water", 0: "🔫 Gun"}

win_messages = [
    "🔥 What a move! You won this round!",
    "🎯 Bullseye! You're on fire!",
    "🎉 Victory is yours! Well played!"
]
lose_messages = [
    "😢 Oof! You lost this round. Try again!",
    "💀 Ouch! That was a tough one.",
    "😨 The computer outplayed you this time!"
]

# Score Tracking
player_score = 0
computer_score = 0
rounds_to_win = 3  # First to 3 wins

while True:
    print("\n----------------------------------------")
    print(Fore.CYAN + f"🎮 Score: You [{player_score}] - Computer [{computer_score}]" + Style.RESET_ALL)
    print("----------------------------------------\n")

    youstr = input(Fore.YELLOW + "Enter your choice (Snake/Water/Gun) or type 'Quit' to exit: " + Style.RESET_ALL).capitalize()

    if youstr == "Quit":
        print(Fore.GREEN + "\nThanks for playing! 🎉 See you next time! ✨" + Style.RESET_ALL)
        break 

    if youstr not in youDict:
        print(Fore.RED + "❌ Invalid choice! Please choose from Snake, Water, or Gun." + Style.RESET_ALL)
        continue 

    you = youDict[youstr]

    computer = random.choice([-1, 0, 1])

    print(Fore.MAGENTA + f"\nYou chose: {reverseDict[you]}")
    print(Fore.BLUE + f"Computer chose: {reverseDict[computer]}" + Style.RESET_ALL)

    if computer == you:
        print(Fore.YELLOW + "🤝 It's a tie!" + Style.RESET_ALL)

    else:
        if (computer == -1 and you == 1) or (computer == 1 and you == 0) or (computer == 0 and you == -1):
            print(Fore.GREEN + random.choice(win_messages) + Style.RESET_ALL)
            player_score += 1
        else:
            print(Fore.RED + random.choice(lose_messages) + Style.RESET_ALL)
            computer_score += 1

    if player_score == rounds_to_win:
        print(Fore.GREEN + "\n🏆 CONGRATULATIONS! You won the match! 🏆" + Style.RESET_ALL)
        break
    elif computer_score == rounds_to_win:
        print(Fore.RED + "\n💀 The computer won the match! Better luck next time! 💀" + Style.RESET_ALL)
        break

    # Small delay(Good User Experience)
    time.sleep(1.5)
