#Import needed library
import random


#Defining function for the game
def guess_number(x):

 print('\n==============================')
 print('   Welcome to Guess Number!   ')
 print('==============================\n')
 print('You will have to guess the number that your computer generates\n')

 random_num = random.randint(1, x) #random number between 1 & x

 prediction = 0  #starting variable for prediction

#starting while loop
 while (prediction != random_num):

  #user inputs a number
  prediction = int(input(f'Enter a number between 1 and {x}: '))

  #verify if prediction is high or minor to random_num
  if (prediction > random_num):
   print("\nTry Again. Number is too high")
   print('.......\n')
  elif (prediction < random_num):
   print("\nTry Again. Number is too low")
   print('.......\n')

 #Congratulations message
 print(f'\nCongratulations! You have guess the number: {random_num}')
  

limit = int(input('Input the top limit number: '))

guess_number(limit)