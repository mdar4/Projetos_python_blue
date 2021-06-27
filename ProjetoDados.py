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

vit1 = vit2 = vit3 = vit4 = empates = 0  # Declarando vitórias e empates

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
print()
clear()
# Cada Jogador terá um valor sorteado através da lib Random
for c in range(rod):
    jogo = {'Player1': random.randint(1,6),
            'Player2': random.randint(1,6),
            'Player3' : random.randint(1,6),
            'Player4': random.randint(1,6)}
    placar = list()
    print('Valores sorteados: ')
    for k, v in jogo.items():
     print(f'{k} tirou {v} no dado.')
    sleep(1)
    # Validando o vencedor de cada Rodada
    if (jogo['Player3'] < jogo['Player1'] > jogo['Player2']) and jogo['Player1'] > jogo['Player4'] :
        vit1 +=1
    elif (jogo['Player3'] < jogo['Player2'] > jogo['Player1']) and jogo['Player2'] > jogo['Player4'] :
        vit2 +=1
    elif (jogo['Player2'] < jogo['Player3'] > jogo['Player1']) and jogo['Player3'] > jogo['Player4'] :
        vit3 +=1
    elif (jogo['Player3'] < jogo['Player4'] > jogo['Player2']) and jogo['Player4'] > jogo['Player1'] :
        vit4 += 1
    else:
      empates = jogo - (vit1,vit2,vit3,vit4) # Contador de empates
    placar = sorted(jogo.items(), key=itemgetter(1), reverse = True) # Para ordenar do maior resultado para o menor

    print('-*' * 40)
    print('   ==== Ranking ===')
    for i, v in enumerate(placar): 
        print(f'{i+1}° lugar: {v[0]} com {v[1]}.') 
        sleep(1)
    print()
    print('*' * 40)
    clear()

print('E O GRANDE VENCEDOR FOI ...')
sleep(2)
# Validando o vencedor
if vit3 < vit1 > vit2 and vit1 > vit4:
  print(f'O Player 1 venceu com {vit1} vitórias.')
elif vit3 < vit2 > vit1 and vit2 > vit4:
  print(f'O Player 2 venceu com {vit2} vitórias.')
elif vit2 < vit3 > vit1 and vit3 > vit4:
  print(f'O Player 3 venceu com {vit3} vitórias.')
elif vit3 < vit4 > vit1 and vit4 > vit2:
  print(f'O Player 4 venceu com {vit4} vitórias.')
print()
# Validando o número de vitórias de cada Jogador
print(f'''
O Player 1 teve {vit1} vitórias.
O Player 2 teve {vit2} vitórias.
O Player 3 teve {vit3} vitórias.
O Player 4 teve {vit4} vitórias.
\n
Tivemos {empates} empates.

''')