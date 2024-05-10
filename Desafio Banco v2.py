opcao = -1
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
usuario =[]
contas = []

LIMITE_SAQUES = 3
AGENCIA = '0001'


while opcao != 8:
    opcao = int(input('''
      _____________________
     |        Menu         |
     |_____________________|
     | Informe uma opção:  |
     |                     |
     | 1 - Sacar           |
     | 2 - Depositar       |
     | 3 - Extrato         |
     | 4 - Nova Conta      |         
     | 5 - Novo Usuário    |
     | 6 - Listar Contas   |
     | 7 - Listar Usuário  |                     
     | 8 - Sair            |
     |_____________________|
                      
    => '''))

    def saques(*, saldo, saque, extrato, limite, numero_saques, limite_saques):
        excedeu_saldo = saque > saldo
        excedeu_limite = saque > limite
        excedeu_saques = numero_saques >= limite_saques
        
        if excedeu_saldo:
            print('Você não possui saldo suficiente para concluir essa translação!')
            print(f'Seu saldo em conta é: R$ {saldo:.2f}')

        elif excedeu_limite:
            print('Limite de saques excedido!')

        elif excedeu_saques:
            print('Número máximo de saques excedido!')
        
        elif saque > 0: 
            saldo -= saque
            extrato += f'Saque: R$ {saque:.2f}\n'
            numero_saques += 1
            print(f'Saque efetuado com sucesso!\nSeu saldo restante em conta é: R$ {saldo:.2f}')

        else:
            print('Valor informado é invalido, tente novamente!')


        return saldo, extrato
    
    def depositos(saldo, deposito, extrato, /):
        if deposito > 0:
            saldo += deposito
            extrato += f'Depósito: R$ {deposito:.2f}\n'
            print(f'Deposito efetuado com sucesso!\nSeu novo saldo é: R$ {saldo:.2f}')

        else:
            print('Valor informado é invalido!')

        return saldo, extrato

    def mostrar_extrato(saldo, /, *, extrato):
        print('\n====================== EXTRATO ==================')
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'\nSeu saldo em conta é: R$ {saldo:.2f}')
        print('===================================================')

    def nova_conta(agencia, numero_conta, usuario):
        cpf = input('Informe o CPF: ')
        usuario = filtrar_usuario(cpf, usuario)

        if usuario:
            print('Conta criada com sucesso!')
            return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}
            
        print('Conta não localizada, para criacao da conta é preciso primeiro criar um usuário')

    def novo_usuario(usuarios):
        cpf = input('Informe o CPF, apenas com numeros: ')
        usuario = filtrar_usuario(cpf, usuarios)

        if usuario:
            print('Usuário já existente com esse CPF!')
            return    
        
        nome = input('Informe o nome completo: ')
        nascimento = input('informe a data de nascimento dia/mes/ano: ')
        endereco = input('Informe o endereco Logradouro, numero, bairro, cidade/estado abreviado: ')

        usuarios.append({'nome': nome, 'data_nascimento': nascimento, 'cpf': cpf, 'endereco': endereco})

        print('Usuário cadastrado com sucesso!')

    def filtrar_usuario(cpf, usuarios):
        usuario_filtrado = [usuario for usuario in usuarios if usuario['cpf'] == cpf ]
        return usuario_filtrado[0] if usuario_filtrado else None
    
    def listar_contas(contas):
     
        for conta in contas:
            linha = f'''
            ------------------------------------------
            | Agência: {conta['agencia']}                                     
            | CC: {conta['numero_conta']}                                   
            | Titular: {conta['usuario']['nome']}                             
            |                                                                  
            ------------------------------------------
            '''
            print(linha)

    def listar_usuarios(usuarios):
        for usuario in usuarios:

            linha = f'''
            ---------------------------------------------------------------------
            | Nome: {usuario['nome']}
            | Data Nascimento: {usuario['data_nascimento']}
            | Endereço: {usuario['endereco']}
            ---------------------------------------------------------------------
            '''
            print(linha)



    if opcao == 1:
        print(' ')
        saque = float (input('Informe o valor que deseja sacar: R$ '))
        
        saldo, extrato = saques(
            saldo=saldo,
            saque=saque,
            extrato=extrato,
            limite=limite,
            numero_saques=numero_saques,
            limite_saques=LIMITE_SAQUES
            
        )


    elif opcao == 2: 
        print(' ')
        deposito = float (input('Informe o valor a ser depositado: R$ '))

        saldo, extrato = depositos(saldo, deposito, extrato)
        
    elif opcao == 3:
        mostrar_extrato(saldo, extrato = extrato)

    elif opcao == 4:
        numero_conta = len(contas) + 1
        conta = nova_conta(AGENCIA, numero_conta, usuario)

        if conta:
            contas.append(conta)

    elif opcao == 5:
        novo_usuario(usuario)

    elif opcao == 6:
        listar_contas(contas)
    
    elif opcao == 7:
        listar_usuarios(usuario)
          
    elif opcao > 8:
        print(' ')
        print('Opção inválida, por gentileza escolha opção valida!\n')

