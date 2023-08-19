"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Anastassiya Manakova
email: anastassiyamanakova@gmail.com
discord: Anastassiya M.#8059
"""

# import random library
import random
import time


# main function
def main():
    start = time.time()

    # 'hello' text
    print(
        '\n'
        'Hi there!\n'+
        '-'*47+
        '\nI\'ve generated a random 4 digit number for you.\n'
        'Let\'s play a bulls and cows game.\n'+
        '-'*47
    )

    # get number from computer
    computer_num = get_random_num()
    attempts = 0

    # the game
    while True:
        user_num = get_num_user()
        bull, cow = compare_numbers(user_num, computer_num)
        print(
            '-'*15+
            f'\n{bull} bulls, {cow} cows\n'+
            '-'*15
        )
        attempts += 1

        if bull == 4:
            end = time.time()
            seconds = int(end - start)
            seconds = seconds % (24 * 3600)
            minutes = seconds // 60
            seconds %= 60

            print(
                '-'*54+
                f"\nCorrect, you've guessed the right number in {attempts} guesses!\n"
                f"It took {minutes} minutes {seconds} seconds.\n"+
                '-'*54
            )
            break


# how many bulls and cows - function
def compare_numbers(guess, answer):
    bull = 0
    cow = 0

    for i in range(len(guess)):
        if guess[i] == answer[i]:
            bull += 1
        if guess[i] in answer:
            cow += 1
    cow = cow - bull
    return bull, cow


# get random 4digits number from computer - function
def get_random_num():
    while True:
        random_num = random.randint(1000, 9999)

        # all different digits
        if len(str(random_num)) != len(set(str(random_num))):
            continue
        else:
            random_num = str(random_num)
            return random_num


# get right answer from user - function
def get_num_user():
    while True:
        guess_num = (input('Please enter a 4 digit number: ')).strip()

        # if 4 digits
        if len(guess_num) != 4:
            print(
                '-' * 42+
                '\nYou don\'t have 4 digits, please try again.\n'+
                '-' * 42
            )
            continue

        # is digit
        if not guess_num.isnumeric():
            print(
                '-'*37+
                'It\'s not a number, please try again.\n'+
                '-'*37
            )
            continue

        # all different digits
        if len(guess_num) != len(set(guess_num)):
            print(
                '-'*44+
                '\nYou have duplicate digits, please try again.\n'+
                '-'*44
            )
            continue

        # if not starts with 0
        if guess_num[0] == '0':
            print(
                '-'*44+
                'Your number starts with 0, please try again.'+
                '-'*44
            )
            continue

        else:
            return guess_num


main()
