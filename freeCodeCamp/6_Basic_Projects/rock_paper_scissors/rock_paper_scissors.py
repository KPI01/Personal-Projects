# rock paper scissor game

# needed module
import random


# game code
def game():

    # user's input
    user = input("\nInput Rock(R), Paper(P) or Scissor(S): \n").upper()

    # computer's input
    computer = random.choice(['R', 'P', 'S'])
    print(f'\nComputer chose: {computer}\n')\

    print(f'You have chosen \'{user}\' and computer chosen \'{computer}\' sooo.... ** suspense ** ....\n')

    if (user == computer):
        return "There's a tie! :o\n"
    
    if user_wins(user, computer):
     return "You win!! :)\n"

    return "You have lost :'(\n"


def user_wins(player, rival):
   #Return true in case user wins

   if (((player == 'R') and (rival == 'S'))
    or ((player == 'S') and (rival == 'P'))
    or ((player == 'P') and (rival == 'R')) 
        ):
        return True

   else:
        return False


print(game())