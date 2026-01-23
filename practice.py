print('Hello World')

def sum_nums(num_1, num_2):
    print(f'The sum of {num_1} + {num_2} is {num_1 + num_2} ')
    return num_1 + num_2

print(sum_nums(3, 4))

def power_nums(num1, num2):
    return num1 ** num2
print(power_nums(2, 4))

def combine_words(word_1, word_2):
    return word_1 + word_2

print(combine_words('Howdy', 'Partner What is going on here!!'))

def divide_nums(num1, num2):
    if num1 % num2 == 0:
        return num1 % num2
    else: return 'num1 needs to be divisable by num2!'

print(divide_nums(10,5))
