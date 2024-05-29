from time import strftime
from abc import ABC, abstractmethod
from os import system
from time import sleep

class Cliente:
    def __init__(self, endereco: str, contas: list[object] = None) -> None:
        """
        Classe que representa um cliente do banco.

        Args:
            endereco (str): Endereço do cliente.
            contas (list[object], optional): Lista de contas associadas ao cliente. Defaults to None.
        """
        self._endereco = endereco
        self._contas = contas or []

    @property
    def endereco(self) -> str:
        return self._endereco

    @property
    def contas(self) -> list[object]:
        return self._contas

    def realizar_transacao(self, conta: object, transacao: object):
        """
        Registra uma transação para a conta do cliente.

        Args:
            conta (object): Conta associada ao cliente.
            transacao (object): Transação a ser registrada.
        """
        transacao.registrar(conta=conta)

    def adicionar_conta(self, conta: object) -> None:
        """
        Adiciona uma nova conta à lista de contas do cliente.

        Args:
            conta (object): Conta a ser adicionada.
        """
        self._contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome: str, cpf: str, data_nascimento: str, endereco: str) -> None:
        """
        Classe que representa uma pessoa física cliente do banco.

        Args:
            nome (str): Nome da pessoa física.
            cpf (str): CPF da pessoa física.
            data_nascimento (str): Data de nascimento da pessoa física.
            endereco (str): Endereço da pessoa física.
        """
        self._nome = nome
        self._cpf = cpf
        self._data_nascimento = data_nascimento
        super().__init__(endereco)

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def cpf(self) -> str:
        return self._cpf

    @property
    def data_nascimento(self) -> str:
        return self._data_nascimento

    def __str__(self) -> str:
        """
        Retorna uma representação em formato de string com informações relevantes sobre o cliente.

        Returns:
            str: Representação em formato de string.
        """
        string: str = f"""
                    Nome:\t\t{self.nome}
                    Cpf:\t\t{self.cpf}
                    Data de Nascimento:\t{self.data_nascimento}
                    Endereço:\t\t{self.endereco}
                    Contas:\t\t{self.contas}\n
                    """
        return string


class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self) -> float:
        """
        Valor da transação.

        Returns:
            float: Valor da transação.
        """
        ...

    @abstractmethod
    def registrar(self, conta: object) -> bool:
        """
        Registra a transação para a conta especificada.

        Args:
            conta (object): Conta associada à transação.

        Returns:
            bool: True se a transação foi registrada com sucesso, False caso contrário.
        """
        ...


class Historico:
    def __init__(self) -> None:
        self._transacoes = []

    @property
    def transacoes(self) -> list[dict]:
        return self._transacoes

    def adicionar_transacao(self, transacao: Transacao) -> None:
        """
        Adiciona uma transação ao histórico.

        Args:
            transacao (Transacao): Transação a ser adicionada.
        """
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": strftime("%d-%m-%Y '%H:%M:%S'"),
            }
        )
        
class Conta:
    def __init__(self, numero: int, cliente: PessoaFisica) -> None:
        """
        Classe que representa uma conta bancária.

        Args:
            numero (int): Número da conta.
            cliente (PessoaFisica): Cliente associado à conta.
        """
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente: PessoaFisica, numero: int) -> object:
        """
        Cria uma nova instância de Conta.

        Args:
            cliente (PessoaFisica): Cliente associado à conta.
            numero (int): Número da conta.

        Returns:
            object: Nova instância de Conta.
        """
        return cls(numero, cliente)

    @property
    def saldo(self) -> float:
        """
        Saldo atual da conta.

        Returns:
            float: Saldo da conta.
        """
        return self._saldo

    @property
    def numero(self) -> int:
        """
        Número da conta.

        Returns:
            int: Número da conta.
        """
        return self._numero

    @property
    def agencia(self) -> str:
        """
        Agência da conta (fixa como "0001").

        Returns:
            str: Agência da conta.
        """
        return self._agencia

    @property
    def cliente(self) -> PessoaFisica:
        """
        Cliente associado à conta.

        Returns:
            PessoaFisica: Cliente da conta.
        """
        return self._cliente

    @property
    def historico(self) -> Historico:
        """
        Histórico de transações da conta.

        Returns:
            Historico: Objeto de histórico de transações.
        """
        return self._historico

    def sacar(self, valor: float) -> bool:
        """
        Realiza um saque na conta.

        Args:
            valor (float): Valor a ser sacado.

        Returns:
            bool: True se o saque foi bem-sucedido, False caso contrário.
        """
        saldo = self._saldo
        out_saldo = valor > saldo

        if out_saldo:
            print("Valor excedeu o limite do saldo!")
        elif valor > 0:
            self._saldo -= valor
            print("Saque realizado com sucesso!")
            return True
        else:
            print("Ocorreu um erro ao realizar o saque!")

        return False

    def depositar(self, valor: float) -> bool:
        """
        Realiza um depósito na conta.

        Args:
            valor (float): Valor a ser depositado.

        Returns:
            bool: True se o depósito foi bem-sucedido, False caso contrário.
        """
        if valor > 0:
            self._saldo += valor
            print("Sucesso ao realizar o depósito!")
            return True
        else:
            print("Ocorreu um erro ao realizar o depósito!")
            return False
class Saque(Transacao):
    def __init__(self, valor: float) -> None:
        """
        Classe que representa uma transação de saque em uma conta bancária.

        Args:
            valor (float): Valor do saque.
        """
        self._valor = valor

    @property
    def valor(self) -> float:
        """
        Valor do saque.

        Returns:
            float: Valor do saque.
        """
        return self._valor

    def registrar(self, conta: Conta) -> None:
        """
        Registra a transação de saque no histórico da conta.

        Args:
            conta (Conta): Conta associada à transação.
        """
        resultado = conta.sacar(self._valor)

        if resultado:
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor: float) -> None:
        """
        Classe que representa uma transação de depósito em uma conta bancária.

        Args:
            valor (float): Valor do depósito.
        """
        self._valor = valor

    @property
    def valor(self) -> float:
        """
        Valor do depósito.

        Returns:
            float: Valor do depósito.
        """
        return self._valor

    def registrar(self, conta: Conta) -> bool:
        """
        Registra a transação de depósito no histórico da conta.

        Args:
            conta (Conta): Conta associada à transação.

        Returns:
            bool: True se o depósito foi bem-sucedido, False caso contrário.
        """
        resultado = conta.depositar(self._valor)
        if resultado:
            conta.historico.adicionar_transacao(self)


class ContaCorrente(Conta):
    def __init__(self, numero: int, cliente: PessoaFisica,
                 limite: float = 500, limite_saque: int = 3) -> None:
        """
        Classe que representa uma conta corrente.

        Args:
            numero (int): Número da conta.
            cliente (PessoaFisica): Cliente associado à conta.
            limite (float, optional): Limite de saque da conta. Defaults to 500.
            limite_saque (int, optional): Número máximo de saques permitidos. Defaults to 3.
        """
        self._limite = limite
        self._limite_saque = limite_saque
        super().__init__(numero=numero, cliente=cliente)

    def sacar(self, valor) -> bool:
        """
        Realiza um saque na conta corrente, verificando limites e número máximo de saques.

        Args:
            valor: Valor a ser sacado.

        Returns:
            bool: True se o saque foi bem-sucedido, False caso contrário.
        """
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes
             if transacao["tipo"] == Saque.__name__]
        )

        excedeu_limite = valor > self._limite
        excedeu_saques = numero_saques >= self._limite_saque

        if excedeu_limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")
        elif excedeu_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
        else:
            return super().sacar(valor)

        return False

    def __str__(self) -> str:
        """
        Retorna uma representação em formato de string com informações relevantes sobre a conta corrente.

        Returns:
            str: Representação em formato de string.
        """
        string: str = f"""
                Agência:\t{self.agencia}
                C/C:\t\t{self.numero}
                Titular:\t{self.cliente.nome}\n
        """
        return string

class Menu:
    def __init__(self, cliente: PessoaFisica = None) -> None:
        """
        Classe que representa um menu de opções para um sistema bancário.

        Args:
            cliente (PessoaFisica, optional): Cliente associado ao menu. Defaults to None.
        """
        if cliente is not None:
            self._menu = f"""
        Bem-vindo {cliente.nome}!
        
        Selecione uma opção:
    
        [c] -> Criar Usuário
        [cc] -> Criar Conta Corrente
        [l] -> Listar Usuários
        [lc] -> Listar Contas
        [d] -> Depositar
        [s] -> Sacar
        [v] -> Visualizar Extrato
        [q] -> Sair
        
        ->
            """
        else:
            self._menu = """
        Selecione uma opção:
    
        [c] -> Criar Usuário
        [cc] -> Criar Conta Corrente
        [l] -> Listar Usuários
        [lc] -> Listar Contas
        [d] -> Depositar
        [s] -> Sacar
        [v] -> Visualizar Extrato
        [q] -> Sair
        
        ->
            """

    @property
    def menu(self) -> str:
        """
        Retorna o menu de opções.

        Returns:
            str: Menu de opções.
        """
        return self._menu

class Main:
    def __init__(self):
        """
        Classe principal que gerencia um sistema bancário simples.

        Atributos:
            _menu (Menu): Menu de opções.
            _LISTA_USUARIOS (list[PessoaFisica]): Lista de usuários cadastrados.
            _LISTA_CONTAS (list[ContaCorrente]): Lista de contas correntes criadas.
            _usuario_ativo (PessoaFisica): Usuário ativo no sistema.
            _conta_ativa (ContaCorrente): Conta corrente ativa no sistema.
        """
        self._menu = Menu()
        self._LISTA_USUARIOS: list[PessoaFisica] = []
        self._LISTA_CONTAS: list[ContaCorrente] = []
        self._usuario_ativo: PessoaFisica = None
        self._conta_ativa: ContaCorrente = None

        while True:
            op = input(self._menu.menu)

            if op == 'c':
                usuario = self.Cadastrar_Usuario()
                if usuario:
                    self._LISTA_USUARIOS.append(usuario)
                    self._usuario_ativo = usuario
                    self._menu = Menu(self._usuario_ativo)
                    print("Usuário cadastrado com sucesso!")
                sleep(2)
                system("cls")

            elif op == 'cc':
                num_conta = len(self.Lista_Usuarios)
                conta = self.CriarContaCorrente(cliente=self._usuario_ativo, numero_conta=num_conta)
                if conta:
                    self._LISTA_CONTAS.append(conta)
                    self._conta_ativa = conta
                    print("Conta Corrente criada com sucesso!")
                sleep(2)
                system("cls")

            elif op == "l":
                print("=======================USUÁRIOS=======================")
                for usuario in self.Lista_Usuarios:
                    print(f"- {usuario.nome}")
                sleep(5)
                system('cls')

            elif op == 'lc':
                print("=======================CONTAS=======================")
                for conta in self.Lista_Contas:
                    print(conta)
                sleep(5)
                system('cls')

            elif op == 'd':
                valor_deposito = float(input('Informe a quantidade a ser depositada: '))
                deposito = Deposito(valor_deposito)
                deposito.registrar(self.Lista_Contas[self.Lista_Contas.index(self._conta_ativa)])

                sleep(2)
                system('cls')

            elif op == 's':
                valor_saque = float(input('Informe a quantidade a ser retirada: '))
                saque = Saque(valor_saque)
                saque.registrar(self.Lista_Contas[self.Lista_Contas.index(self._conta_ativa)])

                sleep(2)
                system('cls')

            elif op == 'v':
                print("=========================================EXTRATO=========================================")
                for i, v in enumerate(self._conta_ativa.historico.transacoes):
                    for chave, valor in enumerate(v.items()):
                        print(f"\t\t\t\t{valor[0]}:\t\t{valor[1]}")
                    print()

                sleep(5)
                system("cls")

            elif op == 'q':
                print('Até Breve!')
                sleep(2)
                system('cls')
                break
            else:
                print("Opção inválida!")
                sleep(2)
                system('cls')

    @property
    def Lista_Usuarios(self) -> list[PessoaFisica]:
        """
        Lista de usuários cadastrados.

        Returns:
            list[PessoaFisica]: Lista de usuários.
        """
        return self._LISTA_USUARIOS

    @property
    def Lista_Contas(self) -> list[ContaCorrente]:
        """
        Lista de contas correntes criadas.

        Returns:
            list[ContaCorrente]: Lista de contas correntes.
        """
        return self._LISTA_CONTAS

def Cadastrar_Usuario(self) -> PessoaFisica:
    """
    Realiza o cadastro de um novo usuário.

    Returns:
        PessoaFisica: Instância da classe PessoaFisica criada com os dados informados.
    """
    print("=========================Informações para Cadastro=========================")
    nome = input("Digite seu Nome: ")
    cpf = input("Informe seu CPF: ")

    verificacao_cpf = self.Verificar_CPF(cpf)
    while verificacao_cpf:
        print("Já existe um usuário com este CPF!")
        cpf = input("Informe um novo CPF: ")
        verificacao_cpf = self.Verificar_CPF(cpf)
        if not verificacao_cpf:
            break

    data_nascimento = input("Informe sua Data de Nascimento (dd/mm/aaaa): ")
    endereco = input("Informe seu Endereço (Logradouro, N° - Bairro - Cidade/Sigla Estado): ")

    try:
        return PessoaFisica(nome=nome, cpf=cpf,
                            data_nascimento=data_nascimento,
                            endereco=endereco)
    except Exception as e:
        print(f"Ocorreu o erro: {e} - Ao criar a Conta do Usuário")

def Verificar_CPF(self, cpf: str) -> bool:
    """
    Verifica se já existe um usuário com o mesmo CPF.

    Args:
        cpf (str): CPF a ser verificado.

    Returns:
        bool: True se já existe um usuário com o mesmo CPF, False caso contrário.
    """
    for i, v in enumerate(self.Lista_Usuarios):
        if v.cpf == cpf:
            return True
    return False

def CriarContaCorrente(self, numero_conta: int, cliente) -> ContaCorrente:
    """
    Cria uma nova conta corrente.

    Args:
        numero_conta (int): Número da conta.
        cliente: Cliente associado à conta.

    Returns:
        ContaCorrente: Instância da classe ContaCorrente criada.
    """
    try:
        return ContaCorrente(numero_conta, cliente)
    except Exception as e:
        print(f"Ocorreu o erro: {e} - Ao Criar a Conta Corrente")

main = Main()