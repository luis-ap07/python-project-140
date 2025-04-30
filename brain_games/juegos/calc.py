from brain_games.juegos.extras import random_number, random_operador
from brain_games.index import play

def juego():
    number1 = random_number()
    number2 = random_number()
    operador = random_operador()

    pregunta = f"{number1} {operador} {number2}"

    if operador == '+':
        correct = number1 + number2
    elif operador == '-':
        correct = number1 - number2
    elif operador == '*':
        correct = number1 * number2

    return pregunta, str(correct)

texto = 'What is the result of the expression?'

def run():
    play(texto, juego)