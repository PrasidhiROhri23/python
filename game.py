import random
# gives random choice
def get_choice():
    player_choice = input("Enter youre choice (Rock, Paper, Scissors):  ");
    options = ["rock", "paper","scissors"];
    computer_choice = random.choice(options);
    choices = {"Player": player_choice,"Computer": computer_choice};
    return choices;
#passing in two arguments
def check_win(player,computer):
    print(f'You chose {player} and the computer chose {computer}');
    # or print(f'You choese {player} and the computer chose {computer});
    if(player==computer):
        return "Its a tie"; 

    elif(player=="rock"):
        if(computer=="scissors"):
          return "Rock smashes scissors. You win!";

        else:
            return "Paper covers rock. You lose.";

    elif(player=="paper"):
        if(computer=="rock"):
          return "Paper covers rock. You win!";

        else:
            return "Scissors cuts paper. You lose.";

    elif(player=="scissors"):
        if(computer=="paper"):
          return "Scissors cuts paper. You win!";

        else:
            return "Rock smashes scissors. You lose.";

choices = get_choice();
result = check_win(choices["Player"],choices["Computer"]);
print('Result: '+ result);
# choices = {"Player": "rock","Computer": "paper"};
#p_choice = choices["Player"]
