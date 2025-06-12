import random
chosen_list = ['many', 'something', 'playing', 'birds']
chosen_word = random.choice(chosen_list)
print(chosen_word)
lives = 6

display = []
for i in range(len(chosen_word)):
    display += '_'
print(display)

game_over = False
while not game_over:
    guess_letter = input("enter your chosen letter: ")
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess_letter:
            display[position] = guess_letter
    print(display)
    if guess_letter not in chosen_word:
        lives-=1
        print(f"Incorrect guess. You have {lives} lives remaining.")
        if lives == 0:
            game_over = True
            print('you lose')
    if '_' not in display:
        game_over = True
        print('you win')

