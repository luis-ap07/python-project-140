from brain_games.juegos.extras import random_number, prime

from brain_games.index import play


def juego():
    pregunta = random_number()
    correct = 'yes' if prime(pregunta) else 'no'
    return str(pregunta), correct


texto = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def run():
    play(texto, juego)