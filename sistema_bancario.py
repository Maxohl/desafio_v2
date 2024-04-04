#variaveis
LIMITE_SAQUE_VALOR = 500.0
numero_saques = 0
LIMITE_SAQUES = 3
usuarios = []
conta_corrente = []
extrato = ""
menu_entrada = f"""\n==================MENU=====================\n
1- Entrar
2- Novo usuário
3- Nova conta corrente
4- Sair \n
==========================================="""

menu_principal = f"""\n==================MENU=====================\n
1 - Saldo
2 - Saque
3 - Depósito
4 - Extrato
5 - Sair\n
==========================================="""



#funções
#formata os dados para serem guardados na lista
def preencher_campos_usuarios():
    novo_usuario = []
    novo_usuario.append(input("Nome: "))
    novo_usuario.append(input("Data Nascimento: "))

    #Verifica se CPF contém apenas números
    while True:
        novo_cpf = input("CPF: ")
        if novo_cpf.isdigit():
            novo_usuario.append(novo_cpf)
            break
        else:
            print("\bCPF deve conter apenas números.\b")

    novo_usuario.append(input("Logradouro: "))
    novo_usuario.append(input("N°: "))
    novo_usuario.append(input("Bairro: "))
    novo_usuario.append(input("Cidade: "))
    novo_usuario.append(input("Estado Sigla: "))

    endereco_formatado = f"{novo_usuario[3]}, {novo_usuario[4]} - {novo_usuario[5]} - {novo_usuario[6]}/{novo_usuario[7]}" 
    criar_usuario(nome=novo_usuario[0],data_nascimento=novo_usuario[1],cpf=novo_usuario[2],endereco=endereco_formatado,usuarios=usuarios)

#Cadastra o usuario se o CPF ainda não existe na lista
def criar_usuario(nome, data_nascimento, cpf, endereco, usuarios):
    #primeiro verifica se o cpf existe na lista
    procura_cpf = procura_usuario(nome, cpf, usuarios)
    if procura_cpf:
        print("Já existe um usuário com esse CPF!")
        return None
    else:
        usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
        print("\nUsuário cadastrado com sucesso!\n")
        print("\nPressione Enter para voltar.\n")        
        input()
        return usuarios

#prepare os dados para criar a conta corrente, verifica se o cpf realmente é daquela pessoa  
def criar_conta_corrente(nome_usuario, cpf_usuario, usuarios, conta_corrente):

    AGENCIA = "0001"
    if conta_corrente:
        numero_conta = len(conta_corrente) +1
    else:
        numero_conta = 1
    
    procura_cpf = procura_usuario(nome_usuario, cpf_usuario, usuarios) #[usuario for usuario in usuarios if usuario["cpf"] == cpf_usuario]
    if (procura_cpf) and (procura_cpf[0]['cpf'] == cpf_usuario) and (procura_cpf[0]['nome'] == nome_usuario):
        nova_conta = {"AGENCIA" : AGENCIA, "Nome": nome_usuario, "CPF": cpf_usuario, "Saldo": 0}
        return nova_conta
    else:
        print("CPF não encontrado ou esse nome de usuário já está cadastrado com esse CPF.")
        return

#procura o usuario e retorna seus dados
def procura_usuario(nome_usuario, cpf_usuario, usuarios):
    procura_cpf = [usuario for usuario in usuarios if usuario["cpf"] == cpf_usuario]
    return procura_cpf

# Perfoma um login usando nome de usuario e CPF, 
def entrar(nome_usuario, cpf_usuario, usuarios):
    procura_cpf = procura_usuario(nome_usuario, cpf_usuario, usuarios)
    if (procura_cpf) and (procura_cpf[0]['cpf'] == cpf_usuario) and (procura_cpf[0]['nome'] == nome_usuario):
        return True
    else:
        return False

#Retorna o saldo do usuario de acordo com o CPF   
def verificar_saldo(cpf, conta_corrente):
    procura_cpf = [conta for conta in conta_corrente if conta["CPF"] == cpf]
    if procura_cpf:
        saldo_formatado = f"{procura_cpf[0]["Saldo"]:.2f}"
        return saldo_formatado
    else:
        return 0
    
# Puxa o saldo para visualização 
def puxar_saldo(cpf, conta_corrente):
    saldo = verificar_saldo(cpf, conta_corrente)
    print("saldo: ", saldo)
    if (saldo != "") and (saldo != False):
        print("\n==================Saldo=====================\n")
        print(f"""Saldo:\t\tR$ {saldo}\n""")
        print("============================================")
        print("\nPressione Enter para Voltar.\n")
        input()
        
    else:
        print("Conta corrente não encontrada.")

#Realiza depoisto na conta do usuario
def fazer_deposito(valor, cpf, conta_corrente, extrato, /):
    achou_conta = False
    #verifica se usuário tem conta criada e atualiza o saldo
    for conta in conta_corrente:
        #se tiver conta corrente e o valor informado for maior que zero, realiza o deposito
        if (conta["CPF"] == cpf) and (valor > 0):
            conta["Saldo"] += valor
            extrato += f"Depósito:\tR$ {valor:.2f}\n"
            print("\nDepósito feito com sucesso!\n")           
            print("\nPressione Enter para voltar.\n")
            input()
            achou_conta = True
            break
    if achou_conta == False:
        print("Ocorreu um erro, favor certifica-se que o valor seja acima de zero e que você tenha uma conta corrente ativa.")
    return extrato

#Realiza o saque da conta do usuario
def fazer_saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    #Verifica se valor é valido
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\nSaldo insuficiente.")
        print("\nPressione Enter para voltar.\n")
        input()
    
    elif excedeu_limite:
        print("\nValor do saque excede o limite.")
        print("\nPressione Enter para voltar.\n")
        input()

    elif excedeu_saques:
        print("\nNúmero máximo de saques excedido.")
        print("\nPressione Enter para voltar.\n")
        input()

    #se valor for valido, realiza o saque 
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n Saque realizado com sucesso! ")
        print("\nPressione Enter para voltar\n")
        input()
    else:
        print("Erro, valor informado é inválido.")
    return saldo, numero_saques, extrato

#Mostra o extrato para o usuário.
def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo}\n")
    print("===========================================\n")
    print("\nPressione Enter para voltar\n")
    input()
    
# principal

# Mostra o menu inicial, onde usuario pode entrar na parte principal do programa, criar novo usuario ou conta corrente
while True:
    print(menu_entrada)
    opcao = int(input("Escolha a opção que deseja realizar: "))

    #Pede para o usuario entrar com Nome e CPF para verificar se ele ja tem cadastro, se sim ele entra no menu principal.
    if opcao == 1:
        print("\nInforme Nome de Usuário e CPF para entrar.\n\n")
        entrada_usuario=input("Nome de Usuário: ")
        entrada_cpf = input("CPF: ")
        usuario_existe = entrar(entrada_usuario, entrada_cpf, usuarios)

        if usuario_existe == True:
            #Mostra o menu principal para o usuário.
            while True:
                print(menu_principal)
                
                #Pede ao usuario para escolher a operação
                opcao_principal = int(input("Escolha a operação que deseja realizar: "))

                #Mostrar Saldo
                if opcao_principal == 1:
                    puxar_saldo(entrada_cpf,conta_corrente)
                
                #Sacar
                elif opcao_principal == 2:
                    valor_saque = float(input("Valor a sacar: "))
                    saldo_atual = float(verificar_saldo(entrada_cpf, conta_corrente))

                    if saldo_atual:
                        novo_saldo, numero_saques, extrato = fazer_saque(
                            saldo = saldo_atual,
                            valor = valor_saque,
                            extrato = extrato,
                            limite = LIMITE_SAQUE_VALOR,
                            numero_saques = numero_saques,
                            limite_saques = LIMITE_SAQUES,
                        )

                    for conta in conta_corrente:
                        if (conta["Nome"] == entrada_usuario) and (conta["CPF"] == entrada_cpf) and (novo_saldo):
                            conta["Saldo"] = novo_saldo
                
                #Depositar
                elif opcao_principal == 3:
                    print("\nInforme o valor que você deseja depositar.\n")
                    valor_deposito = float(input("R$ "))
                    extrato = fazer_deposito(valor_deposito, entrada_cpf, conta_corrente, extrato)

                #Extrato
                elif opcao_principal == 4:
                    saldo_atual = verificar_saldo(entrada_cpf, conta_corrente)
                    exibir_extrato(saldo_atual, extrato = extrato)
                    
                #Sair do menu principal e voltar pro menu inicial
                elif opcao_principal == 5:
                    #reseta variaveis 
                    numero_saques = 0
                    extrato = ""
                    break

                else:
                    print("Operação inválida.")


        else:
            print("Usuário ou senha inválidos") 

    #Cadastro de novo usuario
    elif opcao ==2:
        print("\nPreencha os dados com suas informações. \n\n")
        preencher_campos_usuarios()

    #Cadastro de nova conta corrente
    elif opcao == 3:
        print("\nFavor informar nome de usuário e CPF \n")
        usuario = input("Nome de usuário: ")
        cpf = input("CPF: ")
        nova_conta = criar_conta_corrente(usuario, cpf, usuarios, conta_corrente)
        if nova_conta:
            conta_corrente.append(nova_conta)
            print("\nConta corrente criada com sucesso!")
            print("\nPressione Enter para voltar.\n")
            input()
        else:
            print("Ocorreu um erro")

    #Sair do programa
    elif opcao == 4:
        print("Obrigado por usar nosso programa, tenha um bom dia!")
        break

    else:
        print("Opção inválida!")