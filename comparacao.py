###Criando uma lista
##Ivan, tarso, ustavo, Victor, Gabriel, Rafael, Fabricio




#Qual seria o print e 
# Imput para pedir os nomes?
print("*** lista de nomes***/n")


nomes= input("Digite seu nomes separados por virgulas: ").split(", ")

#Nomes = [nome.split() for nome in nomes]

#print(nomes)

print("\nQuais operacoes voce quer fazer:")
print("1 - adicionar nomes ")
print("2 - remover nomes ")
print("3 - listas de nomes")
print("4 - sair")
 

while True: 
    opcao = input("\ndigite a opcao desejada (1-4):")

    if opcao == "1":
        #novo_nome = imput("digite o nome a ser adicionado: ")
        #nomes.append(novo_nome)
        #print(f"{novo_nome} foi adicionado a lista.")
        print(f"foi adicionado a lista.")

    elif opcao == "2":
        #nome_remover in nomes:
        #   nomes.remover(nome_remover)
        #   print(f"{nome_remover}) foi removido da lista.")
        #else:
            #print(f"{nome_remover}) nao esta na lista.")
        print(f"nao esta na lista.") 

    elif opcao == "3":
        print ("\nlista de nomes") 
        


def main(): 
    while True:
        mostrar_menu()
        opcao = input("escolher uma opcao: ") 
        if opcao == "1":
            num1, num2 = obter_numeros()
            resultado = num1 + num2 
            print(f"resultado da adicao: {resultado}")

        elif opcao == "2":
            num1, num2 = obter_numeros()
            resultado= num1 - num2
            print(f"resultado da subtracao:{resultado}")

        elif opcao == "5":
            print("saindo...")
            break
        else:
            print("opcao invalida. tente novamente as seguintes opcoes: 1, 2 ou 5.")
if_name_== "_main_":
main() 











