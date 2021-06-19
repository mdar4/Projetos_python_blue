import random
from time import sleep
resp = None
jogador = 0
pc = 0
rod = int(input('Número de partidas: '))
pcEsc = ['Pedra', 'Papel', 'Tesoura']
escolha = random.choice(pcEsc)

for c in range(rod):
    print('''
    Faça sua escolha:
    1 - Pedra
    2 - Papel
    3 - Tesoura
    ''')
    resp = int(input('Escolha: '))
    # Pedra
    if resp == 1:
        print('Você escolheu Pedra.')
        sleep(1)
        print('O computador está escolhendo...')
        sleep(2)
        print(f'O computador escolheu {escolha}.') 
        if escolha == 'Papel':
          print('Papel embrulhou Pedra !')
          pc += 1
        if escolha == 'Tesoura':
          print('Pedra quebra Tesoura!')
          jogador += 1
        if escolha == 'Pedra':
          print('Empate.')
    # Papel
    elif resp == 2:
        print('Você escolheu Papel.')
        sleep(1)
        print('O computador está escolhendo...')
        sleep(2)
        print(f'O computador escolheu {escolha}.')
        if escolha == 'Pedra':
          print('Papel embrulhou Pedra !')
          jogador += 1
        if escolha == 'Tesoura':
          print('Tesoura cortou Papel !')
          pc += 1
        if escolha == 'Papel':
          print('Empate.')
    # Tesoura
    elif resp == 3:
        print('Você escolheu Tesoura.')
        sleep(1)
        print('O computador está escolhendo...')
        sleep(2)
        print(f'O computador escolheu {escolha}.')
        if escolha == 'Pedra':
          print('Pedra quebrou Tesoura !')
          pc += 1
        if escolha == 'Papel':
          print('Tesoura cortou Papel !')
          jogador += 1
        if escolha == 'Tesoura':
          print('Empate.')
print(f'O computador venceu {pc} rodadas e o jogador {jogador} rodadas.')
print()
if jogador >= pc:
  print(f'O jogador foi o grande campeão com {jogador} vitórias !')
else:
  print(f'O computador foi o grande campeão com {pc} vitórias !')



