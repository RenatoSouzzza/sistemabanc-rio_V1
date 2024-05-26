menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

# variáveis
saldo = 0
numero_saques = 0
limite_diario = 500
limite_saques = 3
extrato = ''

while True:
    
    opcoes = int(input(menu)) 
    
    if opcoes == 1: 
        dep = float(input('Informe o Valor a ser depositado: R$ '))
    
        if dep > 0: # - somente números positivos
            saldo += dep
            extrato += f'Depósito no valor de R${dep:.2f}\n' # - operações devem ser armazenadas na variável extrato
            print(f'Depósito no valor de R$ {dep:.2f} realizado com sucesso!')
            
        else:
            print('Valor inválido. Tente novamente!')
    
    elif opcoes == 2:
        if numero_saques >= limite_saques: # - limite de 3 saques diários
                print('Limite de saques diários (3) excedido. Contate seu banco para maiores informações')
                
        else:
            saq = float(input('Informe o Valor do Saque: R$ '))
            while saq > 500: # - limite de 500 reais por saque
                print(f'Valor de saque excede limite diário (R$ {limite_diario:.2f})')
                saq = float(input('Informe o Valor do Saque: R$ '))

            else:
                       
                if saq < saldo:
                    saldo -= saq
                    numero_saques += 1
                
                    extrato += f'Saque no valor de R${saq:.2f}\n' # - operações devem ser armazenadas na variável extrato
                    print(f'Saque no valor de R$ {saq:.2f} realizado com sucesso')
                        
                else: # - se saldo negativo, deve ocorrer mensagem informando
                    print('Saldo Insuficiente')
            
    elif opcoes == 3: # - listar todas as operações realizadas na execução do programa 
        print('=' * 6, 'EXTRATO', '=' * 6 )
        print()
        print('Não houveram movimentações.' if extrato == '' else extrato) # - se não houver operações, informar que não houveram movimentações
        print(f'Saldo atualizado: R$ {saldo:.2f}')
        print('=' * 21)
        
    elif opcoes == 0:
        print('Sistema bancário encerrado! Volte Sempre!')
        break

    else:
        print('Operação Inválida. Informe a opção desejada!')
       
    
                
        