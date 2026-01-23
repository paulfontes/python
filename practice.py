import math
import random
# def sum_nums(num_1, num_2):
#     print(f'The sum of {num_1} + {num_2} is {num_1 + num_2} ')
#     return num_1 + num_2

# print(sum_nums(3, 4))

# def power_nums(num1, num2):
#     return num1 ** num2
# print(power_nums(2, 4))

# def combine_words(word_1, word_2):
#     return word_1 + word_2

# print(combine_words('Howdy', 'Partner What is going on here!!'))

# def divide_nums(num1, num2):
#     if num1 % num2 == 0:
#         return num1 % num2
#     else: return 'num1 needs to be divisable by num2!'

# print(divide_nums(10,5))

print('Pick rock, paper or scissors!')
player_pick = input().lower()
player_score = 0
computer_score = 0

def rock_paper_scissors(player, computer):
    if player not in ['rock', 'paper', 'scissors']:
        return 'invalid choice!'
    if player == computer:
        return 'tie'
    elif(player == "rock" and computer == "scissors"):
        player_score += 1
        return f'player wins! Player Score: {player_score} Computer Score: {computer_score} first to 5 wins!'
    elif(player == 'scissors' and computer == 'paper'):
        player_score += 1
        return f'player wins! Player Score: {player_score} Computer Score: {computer_score} first to 5 wins!'
    elif(player == 'paper' and computer == 'rock'):
        player_score += 1
        return f'player wins! Player Score: {player_score} Computer Score: {computer_score} first to 5 wins!'
    else: 
        computer_score += 1
        return f'computer wins! Player Score: {player_score} Computer Score: {computer_score} first to 5 wins!'

def computer_pick():
    computer_picked = ''
    random_number = random.randint(1, 3)
    if random_number == 1:
        computer_picked = 'rock'
        print(f'computer picked {computer_picked}')
        return computer_picked
    elif random_number == 2:
        computer_picked = 'paper'
        print(f'computer picked {computer_picked}')
        return computer_picked
    else:
        computer_picked = 'scissors'
        print(f'computer picked {computer_picked}')
        return computer_picked
    


print(rock_paper_scissors(player_pick, computer_pick()))
# print(rock_paper_scissors('paper', 'rock'))