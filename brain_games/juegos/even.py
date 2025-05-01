from brain_games.juegos.extras import random_number
from brain_games.index import play

  def juego():
    number = random_number()
    pregunta = str(number)
    correct = 'yes' if number % 2 == 0 else 'no'
    return pregunta, correct

  texto = 'Answer "yes" if the number is even, otherwise answer "no".'

  def run():
    play(texto, juego)