# importing random lib
import random


# initializing game function
def guess_number_computer(x):

    print('\n========================================')
    print('   Welcome to Guess Number Computer!   ')
    print('========================================\n')
    print(f'Your computer will have to guess the number between 1 and {x} \n')

    # declaring variable for range of numbers
    l_max = x
    l_min = 1

    # variable to ask use if continue process
    answer = ''

    # start while loop for guessing number
    while (answer != 'c'):

        # verify if limits are different
        if (l_min != l_max):
            # variable for computer's prediction
            prediction = random.randint(l_min, l_max)

        else:

            prediction = l_min

       # get answer from user
        answer = input(
            f'\nMy prediction is: {prediction}. If it is too high, input (A). If it is too low, input (B). Is it is correct or you want to cancel the process, input (C): \n').lower()

        # verify user's answer
        if (answer == 'a'):
            l_max = prediction - 1
        elif (answer == 'b'):
            l_min = prediction + 1

    print(
        f'\nCongratulations!! Your computer have guessed your number: {prediction}')


z = int(input('Input the maximum number for the range your computer will have to guess: '))

guess_number_computer(z)