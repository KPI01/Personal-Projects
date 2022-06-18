import random
import string


# import list of words from file words.py
from words import words_list
from draws import live_draws

# define function to obtain words


def obtain_valid_word(words_list):

    # select a random word from list
    word = random.choice(words_list)

    while '-' in word or ' ' in word:
        word = random.choice(words_list)

    return word.upper()


# game code
def game():

    print('\n=====================================')
    print('       Welcome to Hangman Game       ')
    print('=====================================\n')

    valid_word = obtain_valid_word(words_list)

    letters = set(string.ascii_uppercase)  # all available letter
    letters_to_guess = set(valid_word)  # Missing letters to guess
    guessed_letters = set()  # letters that user has guessed

    lives = 7  # amount of lives

    # loop while letters to guess is more than 0 and lives are more tha 0
    while (len(letters_to_guess) > 0) and (lives > 0):
        print(
            f'\nLives left: {lives} and you have used this letters : {" ".join(guessed_letters)}')

        # variable to save the current word on a variable and printing it with missing letters
        current_word = [
            letter if letter in guessed_letters else '-' for letter in valid_word]
        print(current_word)
        print(live_draws[lives])

        # Users input a letter
        users_letter = input('\nChoose a letter: ').upper()
        while (len(users_letter) > 1):
            users_letter = input('\nTry Again: ... ')

        # iteration for letter in letters and is missing in guessed letters
        if users_letter in letters - guessed_letters:
            guessed_letters.add(users_letter)

            # If users letters in guessed letters, that letter will have to be removed from letters to guess
            if users_letter in letters_to_guess:
                letters_to_guess.remove(users_letter)

            else:
                lives = lives - 1
                print(f"\nYour letter: {users_letter} isn't in the word")
        elif users_letter in letters_to_guess:
            print("\n You have already chosen this one. Try again...")
        else:
            print("\nThis letter isn't valid")

    if (lives == 0):
        print(live_draws[lives])
        print(f"You loooosee. The word was: {valid_word}")
    else:
        print(f"Congratulations!! You have guessed the word: {valid_word}")


if __name__ == '__main__':
    game()
