import random
print('*** WELCOME TO NUMBER GUESS GAME ***')

HARD_LEVEL_ATTEMPTS = 5
EASY_LEVEL_ATTEMPTS = 10

def game_level(level):
    if level == 'hard':
        return HARD_LEVEL_ATTEMPTS
    else:
        return EASY_LEVEL_ATTEMPTS

def attempt(guessed_answer,  answer, attempts,):
    if guessed_answer > answer:
        print('your guess is too high')
        return attempts - 1
    elif guessed_answer < answer:
        print('your guess is too low')
        return attempts - 1
    else:
        print(f"your guess is right...... answer is {answer}")
        return 0

def game():
    print('please guess a number from 1 to 50')
    answer = random.randint(1,50)
    #print(answer)
    chosen_level = input('enter the level you want to play\n')
    attempts = game_level(chosen_level)
    while True:
        print(f"you have {attempts} attempts remaining")
        guessed_answer = int(input("enter your your guess\n"))
        if guessed_answer == answer:
            print('congs you have won......')
            break
        else:
            attempts = attempt(guessed_answer, answer, attempts)
            if attempts > 0:
              print('wrong guess')
            else:
                print('your out of your moves')
                print(f"the correct answer was {answer}")
                break
    more = input("do u want to try again. enter 'yes' to continue of 'no' to exit\n")
    if more == 'yes':
        game()
    elif more =='no':
        print("thank you for participating")
    else:
        print("invalid input. please try again")
game()



