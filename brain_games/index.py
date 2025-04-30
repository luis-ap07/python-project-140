from brain_games.cli import welcome_user

def play(texto, juego_func):
    name = welcome_user()
    print(texto)
    corrects = 0

    while corrects < 3:
        pregunta, correct = juego_func()
        print(f'Question: {pregunta}')
        answer = input('Your answer: ')

        if answer == correct:
            print('Correct!')
            corrects += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct}'.")
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')