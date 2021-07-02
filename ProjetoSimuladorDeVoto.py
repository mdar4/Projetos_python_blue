# -------------------- Libs usadas no programa -------------------------
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

from time import sleep # Lib para temporizar ações e dar efeito

# --------------------------- Funções ---------------------------------
# Função de linhas para separar blocos de códigos no console
def linhas():
    print('*' * 30)

def apto():
    print('Precisamos saber se você é apto ao voto.')
    print()
    while True:
        if autoriza_voto() == 'Voto não autorizado.':
            print('Voto negado.')
        else:
            break

# Função que valida apenas números inteiros
def leiaInt(m):
    valido = False
    valor = 0
    while True:
        voto = str(input(m))
        if voto.isnumeric():
            valor = int(voto)
            valido = True
        else:
            print('ERRO! Digite apenas números.')
        if valido:
            break
    return valor

# Função  que autoriza ou não o voto de acordo com a idade do eleitor. 
def autoriza_voto():
    from datetime import date # Lib para atualizar a data atual no programa
    anoAtual = date.today().year # Retorna o Ano Atual
    ano = leiaInt('Ano de Nascimento: ')
    idade = anoAtual - ano

    # Valida se o eleitor pode votar
    if idade < 16:
        return f'Voto não autorizado.'
    elif idade >= 16 and idade <18:
        return f'Voto é opcional.'
    elif idade > 70:
        return f'Voto é opcional.'
    else:
        return f'Voto é obrigatório'

# Função de confirmação do voto
def confirmar():
    confirma = ''
    for v in range(1):
        print('''
        [6] - Confirmar    [7] - Cancelar
        
        ''')
        confirma = leiaInt('Escolha: ')
        if confirma <6 or confirma > 7:
            print(('Opção inválida!'))
            confirmar()
        elif confirma == 7 :
            voto = leiaInt('Vote novamente: ')
            confirmar()
        elif confirma == 6 :
            pass

# Função de escolha de candidatos (voto)
def votacao(voto):
    voto = resp = ''
    jose = maria = joao =  nulo = branco = 0
    

    while True : # Validando se o eleitor é ou não apto para a votação
        if autoriza_voto() == 'Voto não autorizado.':
            print('Eleitor abaixo da idade necessária para voto válido.')
            resp = str(input('Deseja votar novamente?[S/N]: ')).strip().upper()[0]
            while True :
                if resp in 'SN':
                    break
                print('Digite apenas S ou N.')
            if resp == 'N':
                break
        else:
            while voto != 0:
                # Possíveis escolhas do usuário
                print('''
                Escolha sua opção de voto:

                [1] - José
                [2] - Maria
                [3] - João
                [4] - Nulo
                [5] - Branco
                
                OU 

                [0] - Para sair
                
                ''')
                # Validando o voto
                voto = leiaInt('Vote: ')
                while True : # Prevenção de erro
                    if  voto >= 0 and voto <= 5:
                        break
                    else:
                        print('Opção inválida.')
                    voto = leiaInt(('Vote: '))
                if voto == 1 :
                    confirmar()
                    print('Você votou no José')
                    sleep(1)
                    jose += 1
                    apto()
                elif voto == 2 :
                    confirmar()
                    print('Você votou na Maria')
                    sleep(1)
                    maria += 1
                    apto()
                elif voto == 3 :
                    confirmar()
                    print('Você votou no João')
                    sleep(1)
                    joao +=1
                    apto()
                elif voto == 4 :
                    confirmar()
                    print('Você votou Nulo')
                    sleep(1)
                    nulo += 1
                    apto()
                elif voto == 5 :
                    confirmar()
                    print('Você votou em Branco')
                    sleep(1)
                    branco += 1
                    apto()
                
            if voto == 0 :
                print( 'Fim da Votação')

                print('''
                Apurando os votos
                ''', end=' ')
                sleep(1)
                print(' .', end=' ')
                sleep(1)
                print('.', end= ' ')
                sleep(1)
                print('.', end=' ')
                print()

                print(f'''
                 _______________________
                |CANDIDATOS  |   VOTOS  |
                |------------|----------|
                | Maria      |  {maria} votos |
                | José       |  {jose} votos |
                | João       |  {joao} votos |
                | Nulos      |  {nulo} votos |
                | Em Branco  |  {branco} votos |
                |------------|----------|
                | Total      | {maria+jose+joao+branco+nulo} votos  |
                |_______________________|
                ''')

                print(f'''
                 ______________________
                |       Percentual     |
                |----------------------|
                |  {(jose+maria+ joao) * nulo/100}% foram Nulos   |
                |{(jose +maria+joao) * branco/100}% foram em Branco |
                |______________________|
            
                ''')

                if maria < jose > joao:
                    return f'José foi o vencedor com {jose} votos.'
                elif jose < maria >joao:
                    return f'Maria foi vencedora com {maria} votos.'
                elif maria< joao > jose:
                    return f'João foi o vencedor com {joao} votos.'
                else:
                    return 'Não houve vencedor, teremos Segundo Turno.'
                    
                print()
                break

# --------------------------- Programa principal ---------------------------------
clear()
linhas()
print('---------- ELEIÇÕES ----------')
linhas()
print()
print('Precisamos saber se você é apto ao voto.')
print()
print(votacao(autoriza_voto))

