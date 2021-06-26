import os
import sys
if sys.platform.startswith('win32') or sys.platform.startswith('cigwin'):
    #Limpando a tela do Interpretador no Windows
    clear = lambda: os.system('cls')
    clear()
else:
    #Limpando a tela do Interpretador no Linux
    clear = lambda: os.system('clear')
    clear()

# Programa principal

from time import sleep #Lib para realizar temporizar tarefas
import random #Lib para realizar sorteio de números aleatórios
from operator import itemgetter # lib para organizar items da list()

print('''
    VAMOS JOGAR DADOS ?
    
   _______
 /\ o o o \ ______
<  o >------>   o /|
 \ o/  o   /o____/o|
  \/______/     |oo|
        |   o   |o /
        |_______|/
''')
sleep(2)
rod = int(input('Número de rodadas: ')) # Declarando o número de rodadas.

jogo = {'Player1': randint(1,6),
        'Player2': randint(1,6),
        'Player3' : randint(1,6),
        'Player4': randint(1,6)}
placar = list()    
print('Valores sorteados: ')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)

placar = sorted(jogo.items(), key=itemgetter(1), reverse = True)
print('-*' * 40)
print('   ==== Ranking ===')
for i, v in enumerate(placar):
    print(f'{i+1}° lugar: {v[0]} com {v[1]}.') 
    sleep(1)