import textwrap


def menu():
    menu = """\n
    =================== MENU ===================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\tListar Contas
    [nu]\tNovo Usuario
    [q]\tSair
    ==> """
    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f'Deposito:\tR$ {valor:.2f}\n'
        print('\n======= Deposito realizado com sucesso! =======')
    else:
        print('\n@@@@@@@ Operação falou ! Valor informado invalido. @@@@@@@')

    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    escedeu_saques = numero_saques > limite_saques

    if excedeu_saldo:
        print('\n@@@@@@@ Operaçao falhou! nao possui limite. @@@@@@@')

    elif excedeu_limite:
        print('\n@@@@@@@ Operaçao falou! valor do saque excede o limite. @@@@@@@')

    elif excedeu_saques:
        print('\n@@@@@@@ Operaçao falhou! Numero de saques excedidos. @@@@@@@')

    elif valor > 0:
        saldo -= valor
        extrato += f'saque:\t\tR$ {valor:.2f}\n'
        numero_saques += 1
        print('\n ======= Saque realizado com sucesso! =======')

    else:
        print('\n@@@@@@@ Operação Falhou! O valor informado é invalido. @@@@@@@')

    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print('\n =================== EXTRATO ==================')
    print('Não foram realizadas movimentaçoes.' if not extrato else extrato)
    print(f'\nSaldo:\t\tR$ {saldo:.2f}')
    print('================================================')


def criar_usuario(usuarios):
    cpf = input('Informe o CPF (SOMENTE NUMEROS): ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('\n@@@@@@@ Já existe usuario com esse CPF! @@@@@@@')
        return
    nome = input('Informe nome completo: ')
    data_nascimento = input('Informe a data de nascimento (dd-mm-aaaa): ')
    endereco = input('Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ')

    usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})

    print('======= Usuario criado com sucesso! =======')


def filtrar_usuario(cpf, usuario):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario ['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('informe o CPF do usuario: ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('\n=======  Conta criada com sucesso!   =======')
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}
    
    print('\n@@@@@@@ Usuario não encontrado, fluxo de criação de conta incorreto! @@@@@@@')


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print('=' * 100)
        print(textwrap.dedent(linha))


def main():
    LIMITE_SAQUES = 3
    AGENCIA = '0001'

    saldo = 0
    limite = 500
    extrato = ''
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == 'd':
            valor = float(input('Informe o valor do deposito: '))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == 's':
            valor = float(input('Informe o valor do saque: '))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == 'e':
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == 'nu':
            criar_usuario(usuarios)

        elif opcao == 'nc':
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == 'lc':
            listar_contas(contas)

        elif opcao == 'q':
            break

        else:
            print('Operação invalida, por favor selecione novamente a operaçao desejada.')



main()