opcao = -1
saldo = 0
Limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3



while opcao != 4:
    opcao = int(input('''
      _____________________
     |        Menu         |
     |_____________________|
     | Informe uma opção:  |
     |                     |
     | 1 - Sacar           |
     | 2 - Depositar       |
     | 3 - Extrato         |
     | 4 - Sair            |
     |_____________________|
                      
    => '''))

    if opcao == 1:
        print(' ')
        saque = int (input('Informe o valor que deseja sacar: R$ '))
        excedeu_saldo = saque > saldo
        excedeu_limite = saque > Limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
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


    elif opcao == 2: 
        print(' ')
        deposito = int (input('Informe o valor a ser depositado: R$ '))

        if deposito > 0:
            saldo += deposito
            extrato += f'Depósito: R$ {deposito:.2f}\n'
            print(f'Deposito efetuado com sucesso!\nSeu novo saldo é: R$ {saldo:.2f}')

        else:
            print('Valor informado é invalido!')
  
    elif opcao == 3:
        print('\n====================== EXTRATO ==================')
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'\nSeu saldo em conta é: R$ {saldo:.2f}')
        print('===================================================')

    if opcao > 4:
        print(' ')
        print('Opção inválida, por gentileza escolha opção valida!\n')

