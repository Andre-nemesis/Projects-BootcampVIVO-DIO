from os import system
from time import sleep

#This program is for testing the news concepts learning about python in the Bootcamp
# ->!this program will is the second version for the project <-

#language developer Portuguese-Brazil
menuBanco:str = f'''
    Selecione uma opção
    
    [c] -> Criar Usuário
    [cc] -> Criar Conta Corrente
    [l] -> Listar Usuários
    [lc] -> Listar Contas
    [d] -> Deposite
    [s] -> Sacar
    [v] -> Visualizar Extrato
    [q] -> Sair
    
    ->
'''

def Saque (*,saldo:float,valor:float,extrato:str, limite:float, numero_saques:int) -> tuple[float,str,int]:
    """
    Realiza o saque do dinheiro da conta do usuário e adiciona a movimentação ao extrato.

    Args:
        saldo (float): Saldo atual da conta.
        valor (float): Valor a ser sacado (deve ser positivo).
        extrato (str): Extrato atual da conta.
        limite (float): Limite máximo de saque.
        numero_saques (int): Número de saques já realizados.

    Returns:
        tuple[float, str, int]: Uma tupla contendo o novo saldo, o extrato atualizado e o número de saques.
    """
    while valor > limite or saldo - valor < 0 or valor < 0:
        print('Valor a cima do limite, por favor insira um valor dentro do limite de saque ou do valor do seu Saldo!')
        valor = float(input('Informe a quantidade e ser retirada: '))
        if valor <= limite and valor > 0 and saldo - valor > 0:
            break

    print('Valor sacado com sucesso!')
    numero_saques +=1
    saldo -= valor
    extrato += f"Saque no valor de:\t\t\t R$ {valor:.2f}\n"
    sleep(2)
    system('cls')
        
    return saldo,extrato,numero_saques

def Deposito(saldo:float,valor:float,extrato:str,/) -> tuple[float,str]:
    """
    Realiza o depósito de dinheiro na conta do usuário e adiciona a movimentação ao extrato.

    Args:
        saldo (float): Saldo atual da conta.
        valor (float): Valor a ser depositado (deve ser positivo).
        extrato (str): Extrato atual da conta.

    Returns:
        tuple[float, str]: Uma tupla contendo o novo saldo e o extrato atualizado.
    """
    while valor < 0:
        print('Valor inválido, insira um novo valor!')
        valor = float(input('Informe a quantidade e ser depositada: '))
        if valor > 0:
            break
    print('Valor depositado com sucesso!')
        
    sleep(2)
    system('cls')

    saldo += valor
    if extrato == 'EXTRATO':
        extrato = extrato.center(50,"=")
        extrato += f"\nDeposito no valor de:\t\t\t R$ {valor:.2f}\n"
    else:
        extrato += f"Deposito no valor de:\t\t\t R$ {valor:.2f}\n"
    
    return saldo,extrato  

def Extrato (saldo:float,/,*,extrato:str):
    """
    Atualiza o extrato bancário de acordo com os movimentos realizados pelo usuário.

    Args:
        saldo (float): Saldo atual da conta.
        extrato (str): Extrato atual da conta.

    Returns:
        None: A função não retorna valores, apenas atualiza o extrato.
    """
    if extrato == 'EXTRATO':
            print('Não foram realizadas movimentações!')
    else:
        extrato += f"SALDO:\t\t\t\t\t R$ {saldo:.2f}"
        print(extrato)
        
    sleep(5)
    system('cls')

def VerificarCPF(cpf:int,/,*,lista_usuarios:list) -> bool:
    """Verifica se existe uma conta com o cpf informado, caso o usuário exista return True, caso contrário False

    Args:
        cpf (int): CPF do usuário
        lista_usuarios (list): Lista de usuários que ja estão cadastrados no sistema

    Returns:
        bool: False caso o usuário não exista na lista e True caso sim
    """    
    for i,v in enumerate(lista_usuarios):
        if v["CPF"] == cpf:
            return False
    return True

def FiltrarUsusario(lista_usuarios:list,cpf:int) -> dict:
    """Realiza o filtro do usuário para criar a sua conta corrente

    Args:
        lista_usuarios (list): Lista de usuários do sistema
        cpf (int): Chave indicativa para filtrar usuário

    Returns:
        dict: Dicionário contendo as informações do usuário
    """    
    usuario_filtrado = [usuario for usuario in lista_usuarios if usuario["CPF"] == cpf]
    return usuario_filtrado[0] if usuario_filtrado else None

def CriarUsuario(lista_de_usuarios:list) -> list:
    """Essa função irá cadastrar o usuário em uma lista contendo um dicinário de suas informações
    
    Args:
        lista_usuarios: (list): Lista de usuários cadastrados
        
    Returns:
        list[dict]: Lista atualizada com o novo usuário cadastrado
    """    
    
    print("INFORMAÇÔES PARA CADASTRO:")
    nome:str = input('Informe o seu Nome: ')
    cpf:int = int(input('Informe o seu CPF: '))
    
    resutlado_Verificacao:bool = VerificarCPF(cpf,lista_usuarios=lista_de_usuarios)
    
    while not resutlado_Verificacao:
        print("CPF Inválido! Ja existe uma conta com esse CPF")
        cpf:int = input('Informe um CPF válido: ')
        resutlado_Verificacao:bool = VerificarCPF(cpf,lista_usuarios=lista_de_usuarios)
        
    data_nascimento:str = input('Informe sua Data de Nacimento (D/M/A): ')
    endereco:str = input('Informe seu endereço (Logradouro, N° - Bairro - Cidade/Sigla Estado): ')
    
    lista_de_usuarios.append({"Nome":nome, "Data de Nacimento":data_nascimento,"CPF":cpf, "Endereco":endereco})
    
    print("\nUsuario criado com sucesso!")

    sleep(2)
    system('cls')
    return lista_de_usuarios
    
def ListarUsuarios(lista_usuarios:list[dict]) -> str:
    """Está função irá listar todos os usuários cadastrados no banco

    Args:
        lista_usuarios (list[dict]): Lista contendo as informações de todos os usuários

    Returns:
        str: Uma String contendo a listagem de todos os usuários
    """    
    
    str_usuarios:str = 'LISTA DE USUÁRIOS'.center(50,"=") + "\n"
    for i,v in enumerate(lista_usuarios):
        str_usuarios += f"{i+1} - {v["Nome"]}\n"
    return str_usuarios

def CriarContaCorrente(agencia:str,numero_conta:int,usuarios:list[dict]) -> dict:
    """Essa função irá criar a conta corrente do banco para cada usuário

    Args:
        agencia (str): Númerio da agência do banco
        numero_conta (int): Número sequência da conta
        usuarios (list[dict]): Lista de usuarios para realizar o filtro posteriormente

    Returns:
        dict: Dicionario contendo a nova conta corrente com as informações do usuário
    """    
    
    cpf = int(input("Informe o cpf do usuário: "))
    usuario = FiltrarUsusario(usuarios,cpf)
    if usuario:
        print("Conta criada com sucesso!")
        sleep(2)
        system("cls")
        return {"Agencia": agencia, "N° Conta": numero_conta, "usuario":usuario}
        
    print("Usuário não encontrado!")
    
def ListarContas(Contas:list[dict]):
    """Lista todas ad contas correntes criadas no banco

    Args:
        Contas (list[dict]): Lista contendo todos os dicionários de conta 
    """    
    linha =""
    print("="*50)
    for conta in Contas:
        linha += f"""
            Agência:\t{conta["Agencia"]}
            C/C:\t\t{conta["N° Conta"]}
            Titular:\t{conta["usuario"]["Nome"]}\n
        """
    print(linha)
    print("="*50)
    sleep(5)
    system("cls")
    
def main():
    # variaveis constantes utilizadas
    LIMITE_QTD_SAQUE = 3
    SALDO:float = 0
    DEPOSITO:float = 0
    SAQUE:float = 0
    LIMITE_SAQUE:int = 500
    NUM_SAQUE:int = 0
    EXTRATO:str = "EXTRATO"
    LISTA_DE_USUARIOS = []
    LISTA_DE_CONTAS = []
    AGENCIA = "0001"
    while True:
        op = input(menuBanco)

        if op == 'c':
            LISTA_DE_USUARIOS = CriarUsuario(LISTA_DE_USUARIOS)
        
        elif op == 'cc':
            num_conta = len(LISTA_DE_USUARIOS) + 1
            conta = CriarContaCorrente(AGENCIA,num_conta,LISTA_DE_USUARIOS)
            if conta:
                LISTA_DE_CONTAS.append(conta)
            
        elif op == "l":
            print(ListarUsuarios(LISTA_DE_USUARIOS))
            sleep(5)
            system('cls')
        
        elif op == 'lc':
            ListarContas(LISTA_DE_CONTAS)
        
        elif op == 'd':
            DEPOSITO = float(input('Informe a quantidade e ser depositada: '))
            SALDO,EXTRATO = Deposito(SALDO,DEPOSITO,EXTRATO)
        
        elif op == 's':
            if NUM_SAQUE<LIMITE_QTD_SAQUE:
                SAQUE = float(input('Informe a quantidade e ser retirada: '))
                resultado_saque = Saque(saldo=SALDO, valor=SAQUE, extrato=EXTRATO, limite=LIMITE_SAQUE, numero_saques=NUM_SAQUE)
                if resultado_saque is not None:
                    SALDO, EXTRATO, NUM_SAQUE = resultado_saque
                else:
                    print("Erro ao realizar saque.")
            else:
                print('Número máximo de saques realizados!')
                sleep(2)
                system('cls')       

        elif op == 'v':
            Extrato(SALDO,extrato=EXTRATO)
        
        elif op == 'q':
            print('Até Breve!')
            sleep(2)
            system('cls')
            break
        
main()