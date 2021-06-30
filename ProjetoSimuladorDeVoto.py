# Libs usadas no programa
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
    ano = int(input('Ano de Nascimento: '))
    idade = anoAtual - ano
    
    if idade < 16:
        return f'Voto não autorizado.'
    elif idade >= 16 and idade <18:
        return f'Voto é opcional.'
    elif idade > 70:
        return f'Voto é opcional.'
    else:
        return f'Voto é obrigatório'
    

# Função de voto 
def votacao(voto):
    voto = None
    jose = paulo = joao =  nulo = branco = 0
    while voto != 0:
        while True : # Validando se o eleitor é ou não apto para a votação
            if autoriza_voto() == 'Voto não autorizado':
                print(f'Eleitor abaixo da idade necessária para voto válido.')
            else:
                break
        
        print('''
        Escolha sua opção de voto:

        [1] - José
        [2] - Maria
        [3] - João
        [4] - Nulo
        [5] - Branco
        
        OU 

        [0] - Para sair
        [6] - Para cancelar
        ''')
        # Validando o voto
        voto = leiaInt('Vote: ')
        if voto == 1 and voto == '1':
            print('Você votou no José')
            jose += 1
        elif voto == 2 and voto =='2':
            print('Você votou na Maria')
            paulo += 1
        elif voto == 3 and voto =='3':
            print('Você votou no João')
            maria +=1
        elif voto == 4 and voto == '4':
            print('Você votou Nulo')
            nulo += 1
        elif voto == 5 and voto == '5':
            print('Você votou em Branco')
            branco += 1
        elif voto == 6 and voto == '6':
            voto = leiaInt('Vote: ')
        elif voto == 0 and voto == '0':
            break

        


# Programa principal

print(votacao(autoriza_voto))
