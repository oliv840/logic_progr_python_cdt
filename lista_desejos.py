print("🌟minha lista de Desejos para o futuro🌟\n") 
   
NOME_ARQUIVO = "meus_desejos.txt"  
Desejos = []  

with open(NOME_ARQUIVO, 'r', ecoding='utf-8') as arquivo: 
    for linha in arquivo: 
      Desejos.append(linha.strip())  
      print(f"Meus desejos foram carregados do arquivo '{NOME_ARQUIVO}'!\n")      
    except fileNotfoundError:  
    print("parece que e sua primeira vez! Vamos criar sua lista de desejos.\n")  
   except Exception as e: 
print(f"ocorreu um erro ao carregar os desejos: {e}") 
 
 Def salvar_desejos(lista_de_desejos):   
      try: 
   with open(NOME_ARQUIVO, 'w', encoding='utf-8') as arquivo: 
        for desejos in lista_de_desejos: 
            arquivo.write(desejos + "\n") # Escreva cada desejos seguido de uma nova linha 
        print("\n✅ Seus desejos foram salvos com sucesso!") 
    except Exception as e:   
        print(f"\n❌ Erro ao salvar os desejos: {e}")  
while true: 
print("\n"--- O que voce quer fazer?) 
print("1 - Adicionar um novo desejo")
print("2 - Ver meus desejos")
print("3 - Sair") 
 
opcap = imput("Digite sua opcao (1, 2 ou 3)") 
 
 if opcao == "1": 
  novo_desejo + imput("Quale o seu novo desejo para o futuro?") 
  if novo_desejo.strip(): # Garanta que o desjo nao seja vazio 
   desejos.append(novo_desejo.strip()) 
   salvar_desejos(desejos) # Salvar a lista toda vez que um dewsejo e adicionado 
   else: 
    print("Desejos nao pode ser vazio! tente novamente.") 
     
     elif opcao == "2"  
        print("\n⭐ Seus desejos para o futuro ⭐") 
        


 


 
