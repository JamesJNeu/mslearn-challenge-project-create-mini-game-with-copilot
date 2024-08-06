
# import the random module
import random

# create a list of options that has rock, paper, and scissors
options = ['rock', 'paper', 'scissors']

# create a score variable and set it to 0
score = 0
# create a variable to count the number of loses
loses = 0

# create a variable to count the number of rounds
rounds = 0

# create a variable to count the number of ties
ties = 0

# print the rules of the game
print('Welcome to Rock, Paper, Scissors!')
print('The rules are simple:')
print('Rock beats scissors')
print('Scissors beats paper')
print('Paper beats rock')

# print the options the user can choose from
print('');
print('You can choose from the following options:')
print('Rock')
print('Paper')
print('Scissors')

# print the options the computer can choose from
print('');
print('The computer will choose from the following options:')
print('Rock')
print('Paper')
print('Scissors')

# print the instructions for the user
print('');
print('Enter your choice and see if you can beat the computer!')
print('');

# create a while loop that runs as long as the user wants to play
while True:
    # increment the rounds variable
    rounds += 1
  
    valid = True;

    # get the user's choice
    user_choice = input('Enter rock, paper, or scissors: ')
    # convert the user's choice to lowercase
    user_choice = user_choice.lower()

    # get the computer's choice
    computer_choice = random.choice(options)

    # print the computer's choice
    print('Computer chose:', computer_choice)

    # check if the user and computer chose the same option
    if user_choice == computer_choice:
        print('It\'s a tie!')
        ties += 1
    # check if the user chose rock
    elif user_choice == 'rock':
        if computer_choice == 'paper':
            loses += 1
            print('Computer wins!')
        else:
            print('You win!')
            score += 1
    # check if the user chose paper
    elif user_choice == 'paper':
        if computer_choice == 'scissors':
            print('Computer wins!')
            loses += 1
        else:
            print('You win!')
            score += 1
    # check if the user chose scissors
    elif user_choice == 'scissors':
        if computer_choice == 'rock':
            print('Computer wins!')
            loses += 1
        else:
            print('You win!')
            score += 1
    # check if the user entered an invalid option
    else:
        valid = False
        print('Invalid option!');
        
    # check if the user wants to play again
    if not valid:
        rounds -= 1
        continue;

    play_again = input('Do you want to play again? (yes/no): ')
    if play_again == 'no':
        break

# print the final score and number of rounds
# print the final score 
# change the final score to the number of wins and the number of loses
print('Score ->  You:', score, "  Computer:", loses, '  ties:', ties)

# print the number of rounds
print('Number of rounds:', rounds)

