from random import randint


def play_guess_game():
    num = 0
    guessed = False
    while not guessed:
        num = randint(1, 10)
        guess = input('Oya na, guess the number, the number dey change oo, shine ya eyes (1 - 10): ')

        try:
            guess = int(guess)
            if guess == num:
                guessed = True

            print(f'Mehn bros, {guess} no correct oo, the number na {num}!')
        except ValueError:
            print('Oga enter beta thing na ... lol')

    if guessed:
        print(f'Eeyyyyy, as you guess the number {num} correct so, you don win!')


if __name__ == '__main__':
    play_guess_game()
