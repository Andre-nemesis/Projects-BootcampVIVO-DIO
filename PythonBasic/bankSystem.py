from os import system
from time import sleep

#This program is for testing the news concepts learning about python in the Bootcamp, ->!this program will be updated!-<

#lenguage deleveper Portugues-Brazil

menu:str = '''
    Selecione uma opção!

    [d] -> Deposite
    [s] -> Sacar
    [v] -> Visualizar Extrato
    [q] -> Sair
'''

LIMITE_QTD_SAQUE = 3
saldo:float = 0
deposito:float
saque:float
limiteSaque:int = 500
numSaque:int = 0
extrato:str = ""

while True:
    op = input(menu)

    if op == 'd':
        deposito = float(input('Informe a quantidade e ser depositada: '))
        while deposito < 0:
            print('Valor inválido, insira um novo valor!')
            deposito = float(input('Informe a quantidade e ser depositada: '))
            if deposito > 0:
                break
        print('Valor depositado com sucesso!')
        
        sleep(2)
        system('cls')

        saldo += deposito
        extrato += f"Deposito no valor de: R$ {deposito:.2f}\nSalto total: R$ {saldo:.2f}\n"
    
    elif op == 's':
        if numSaque<LIMITE_QTD_SAQUE:
            saque = float(input('Informe a quantidade e ser retirada: '))
            
            while saque > limiteSaque or saldo - saque < 0 or saque < 0:
                print('Valor a cima do limite, por favor insira um valor dentro do limite de saque ou do valor do seu Saldo!')
                saque = float(input('Informe a quantidade e ser retirada: '))
                if saque <= limiteSaque and saque > 0 and saldo - saque > 0:
                    break

            print('Valor sacado com sucesso!')
            numSaque +=1
            saldo -= saque
            extrato += f"Saque no valor de: R$ {saque:.2f}\nSalto total: R$ {saldo:.2f}\n"
            sleep(2)
            system('cls')

        else:
            print('Número máximo de saques realizados!')
            sleep(2)
            system('cls')

    elif op == 'v':
        if extrato == '':
            print('Não foram realizadas movimentações!')
        else: 
            print(extrato)
        sleep(2)
        system('cls')

    elif op == 'q':
        print('Até Breve!')
        sleep(2)
        system('cls')
        break
    
                