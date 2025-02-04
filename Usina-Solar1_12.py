class BD: # verifica se a função já foi criada. Caso, sim, não criará novamente.

    def cria_BD(cliente): # cria banco de dados

        arquivo = open('bancodedados.txt','w')

        arquivo.close()
    

def cadastrar_cliente():

    cliente = input('Nome do cliente: ')

    endereco = input('Endereço: ')

    numero = input('Número: ')
    
    resp_tec = input('Responsál técnico: ')

    cons_anual = float(input('Informe o consumo anual em (Kwh): '))            
   
    med_cons_mensal = round(cons_anual/12,2)# arredonda 2 casas decimais   
   
    print('Média consumo mensal:',med_cons_mensal, 'Kwh.')

    cons_dia = round(med_cons_mensal/24,2)# arredonda 2 casas decimais
    
    print('Média consumo diário:',cons_dia, 'Kwh.')
    
    
    while True: # Tratamento de erro

        try:

            h_sol_pleno = float(input('Informe as horas de sol pleno: '))

        except(ValueError, TypeError):

            print('ERRO !! Digite números com (.) ou inteiro apenas.')

        else:

            break        

    pot_instal = round(cons_dia/h_sol_pleno,2)
              
    print('Potência a ser instalada:',pot_instal, 'Kwp.')

    arquivo = open('bancodedados.txt','a')

    arquivo.write(cliente.title() +':') # grava primeiras letras em maiúscula

    arquivo.write(endereco.title() +':')# grava primeiras letras em maiúscula

    arquivo.write(numero + ':')

    arquivo.write(resp_tec.title() +':')# grava primeiras letras em maiúscula

    arquivo.write(str(cons_anual) + ':')

    arquivo.write(str(med_cons_mensal) + ':')
    
    arquivo.write(str(cons_dia) + ':')
    
    arquivo.write(str(h_sol_pleno) + ':')

    arquivo.write(str(pot_instal) + '\n')

    arquivo.close()

    print()


   
def consulta_cadastro():

    opcao = int(input('  Que tipo de consulta deseja fazer?\n 1) Completa.\n 2) Unica,\n >'))

    if (opcao == 1):

        arquivo = open ('bancodedados.txt').readlines()

        arquivo = [str(x).rstrip() for x in arquivo] # "srt(x)" converte valores dentro do arquivo em valores exatos. "rstrip" remove espaços entre as linhas

        for linha in arquivo:

            print(linha)

        print()

     
    if (opcao == 2):
         
        print('Em fase de desenvolvimento')       
            
             

def main():

    while True:

        print('*'*40)

        print('     Dimensionamento sistema solar')

        print('*'*40)

        print('-'*40)

        print('        Escolha uma das opções:\n 1) Cadastrar cliente,\n 2) Consultar cadastro.\n 3) Sair')

        print('-'*40)

        op = 1000 

        while op != 1 or op !=2 or op !=3: # Tratamento de erro

            try:

                op = int(input(' Opção: '))

                if op == 1 or op ==2 or op ==3:

                    break


                print('ERRO !! Digite apenas 1, 2, ou 3.')
            
            except :

                print('ERRO !! Digite apenas 1, 2, ou 3.')
                

        print('-'*40)    

        if op == 1:

            cadastrar_cliente()

        if op == 2:

            consulta_cadastro()

            
        if op == 3:

            sair = int(input('Deseja realmente sair?\n1)Sim.\n2)Não.'))

            if sair == 1:

                print('Até o próximo cliente !!')

                break

            if sair == 2:

                False
                


main()
    

          
