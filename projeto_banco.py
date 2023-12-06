# Declação de variavéis
saldo = 0
limite = 500
deposito=[]
saque=[]
numero_saques = 0
numero_depositos = 0
LIMITE_SAQUES = 2
# Loop de menu
while True:
    opcao=input(""" 
    ###### BANCO LION ######
                
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Sair            
=> """)
    if opcao == "1":
        deposito_temp= (float(input("Digite o valor a ser depositado:")))
        if deposito_temp>0:
            deposito.append(deposito_temp)
            saldo=saldo+deposito[numero_depositos]
            print(f"O valor de R$ {deposito[numero_depositos]:.2f} foi depositado com sucesso!")
            numero_depositos += 1
        else:
            print("Valor de deposito inválido!")
    elif opcao == "2":
        if numero_saques<=LIMITE_SAQUES:
            saque_temp = (float(input("Digite o valor a ser sacado (Saque máximo = R$500):")))
            excedeu_saldo = saque_temp>saldo
            excedeu_limite = saque_temp>limite
            if saque_temp<=limite and saldo!=0 and saque_temp<=saldo and saque_temp>0:
                saque.append(saque_temp)
                saldo = saldo-saque[numero_saques]
                print(f"Seu saque de R$ {saque[numero_saques]:.2f} foi realizado com sucesso!")
                numero_saques+= 1
            else:
                if excedeu_limite:
                    print("Operação falhou! O valor excedeu o limite!")
                elif excedeu_saldo:
                    print("Operação falhou! Saldo insuficiente!")
                else:
                    print("Operação falhou! Valor inválido!")
        else:
            print("Operação falhou! O número de saques diários foi atingido.")
    elif opcao == "3":
        if numero_saques==0 and numero_depositos==0:
            print("-------- EXTRATO BANCÁRIO --------" )
            print("Não foram realizadas movimentações.") 
            print(f"Seu saldo atual é: R$ {saldo:.2f} ")
            print("-----------------------------------") 
        else:
            print("-------- EXTRATO BANCÁRIO --------")
            for i in range(numero_saques):
                print(f"Saque {i+1}: R$ {saque[i]:.2f}")
            else:
                for i in range(numero_depositos):
                    print(f"Deposito {i+1}: R$ {deposito[i]:.2f}")
                print(f"Seu saldo atual é: R$ {saldo:.2f} ")
            print("-----------------------------------")   
    elif opcao == "4":
        break
    else:
        print("Opção inválida, tente novamente.")
