import math
import random
print('Pick rock, paper or scissors!')
player_pick = input()
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


def rock_paper_scissors(player, computer):
    input
    if player == computer:
        return 'tie'
    elif(player == "rock" and computer == "scissors"):
        return 'player wins!'
    elif(player == 'scissors' and computer == 'paper'):
        return 'player wins!'
    elif(player == 'paper' and computer == 'rock'):
        return 'player wins!'
    else: return 'computer wins!'

def computer_pick():
    computer_picked = ''
    random_number = random.randint(1, 3)
    if random_number is 1:
        computer_picked = 'rock'
        print(f'computer picked {computer_picked}')
        return computer_picked
    elif random_number is 2:
        computer_picked = 'paper'
        print(f'computer picked {computer_picked}')
        return computer_picked
    else:
        computer_picked = 'scissors'
        print(f'computer picked {computer_picked}')
        return computer_picked
    

print(rock_paper_scissors(player_pick, computer_pick()))
# print(rock_paper_scissors('paper', 'rock'))