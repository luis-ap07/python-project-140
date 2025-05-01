import random
from brain_games.juegos.extras import generar_progression
from brain_games.index import play

  def juego():
    progress = generar_progression()
    hidden_index = random.randint(0, len(progress) - 1)
    correct = progress[hidden_index]
    pregunta_lista = [
        '..' if i == hidden_index else str(num)
        for i, num in enumerate(progress)
    ]
    pregunta = ' '.join(pregunta_lista)
    return pregunta, str(correct)

  texto = 'What number is missing in the progression?'

  def run():
    play(texto, juego)