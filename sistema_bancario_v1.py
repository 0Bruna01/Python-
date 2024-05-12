limite_saque = 1
saldo = 0 
saques = 0 
depositos = 0
menu = f'''
          Olá, espero que esteja bem! 
          Qual operação deseja reliazar em sua conta hoje?
          selecione abaixo qual ação deseja realizar:

          1- Sacar
          2- Depositar 
          3- Extrato 
          4- Sair 
'''     
while True :
    print(menu)
    opcao = int(input("A opção desejada é:"))

    if opcao == 1 :
        if limite_saque > 3 :
            print ("Você excedeu seu limite de saque hoje, retorne amanhã!")
        else:
            valor = int(input("Digite o valor que deseja sacar hoje:"))
            if saldo == 0 :
                print ("Sinto muito, sua conta não possui saldo")
            elif valor <= 0:
                print("sinto muito ! Você não pode sacar um valor menor que 0")
            elif valor > 500:
                print ("sinto muito você só pode realizar saques maior que 500 reais")
            elif saldo < valor :
                print ("oh não , saldo insuficiente, verifique seu extrato!")   
            else:
                print (f"Seu saque de {valor} foi realizado com sucesso!")
                limite_saque += 1
                saques += valor
                saldo - valor 
        
    elif opcao == 2:
        deposito= int(input("Qual valor deseja depositar em sua conta hoje?"))
        if deposito > 0 :
            saldo += deposito
            depositos += deposito
            print(f"Seu saldo atual é: {saldo} , Depósito realizado com sucesso!")      
        else :
            print ("sinto muito, Não aceitamos valores abaixo de zero no depósito")

    elif opcao == 3:
        print (f'''            seu saldo é :R${saldo:.2F}
            Valor total de depositos:R${depositos:.2F}
            Valor total de saques:R${saques:.2F}
                 
            Obrigado por nos escolher como sua agência!!!
                 ''' )    
    elif opcao == 4:
        break

    else:
        print("Opção selecionada não conhecida , selecione a opção desejada novamente!")



        

            





