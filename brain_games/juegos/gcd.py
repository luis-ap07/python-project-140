from brain_games.juegos.extras import random_number, mcd
from brain_games.index import play

def juego():
    number1 = random_number()
    number2 = random_number()
    pregunta = f"{number1} {number2}"
    correct = mcd(number1, number2)
    return pregunta, str(correct)

texto = 'Find the greatest common divisor of given numbers.'

def run():
    play(texto, juego)