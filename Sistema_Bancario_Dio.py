import sys


class Operacoes_caixa:
    
    SAQUES_POR_DIA = 3
    VALOR_DE_SAQUE_DIARIO = 500
    contador_de_saque = 0
    extrato = 0
    deposito = 0
    saque = 0
    

    def sacar(self, valor): 
                

        if valor > self.extrato or valor <= 0: 
            print("\n -- Operação nao permitida ou saldo insuficiente")

        elif valor > self.VALOR_DE_SAQUE_DIARIO: 
                print("\n -- Voce nao pode sacar este valor")

        
        elif self.contador_de_saque >= self.SAQUES_POR_DIA: 
                    print("\n -- Limite de saque atingido. Volte amanha")

        else: 
            valor_restante = self.extrato - valor
            self.extrato = valor_restante
            self.contador_de_saque += 1
            
            print(f"\n -- Valor de {valor} R$ sacado com sucesso")

    
        
    
    def depositar(self, valor):

        if valor <= 0: 
            print("\n -- Valor nao suportado")
        else: 
            self.extrato+= valor
            print(f"\n -- Valor de {valor} R$ depositado em conta")
            
        
    
    
    def mostrar_extrato(self): 
        print(f"\n -- Valor em conta: {self.extrato} R$")
        


    def menu_de_opcoes(self): 


        print("""\n Menu de opcoes: 
                      1-Saque 
                      2-Deposito 
                      3-Extrato 
                      4-Sair \n """)
        opcao = int(input("\n -> Insira a opcao desejada: "))

        while opcao:

           
            if opcao == 1: 
                valor_de_saque = input("-> Insira o valor para saque: ")
                self.sacar(float(valor_de_saque))
                self.menu_de_opcoes()

            if opcao == 2: 
                valor_de_deposito = input("-> Insira o valor para deposito: ") 
                self.depositar(float(valor_de_deposito))
                self.menu_de_opcoes()

            if opcao == 3: 
                self.mostrar_extrato()
                self.menu_de_opcoes()

            if opcao == 4: 
                print("-- Sessao finalizada")
                sys.exit()
            else: 
                 print("-- Opcao invalida")
                 self.menu_de_opcoes()

        

    
 
    
user = Operacoes_caixa()
user.menu_de_opcoes()











