print("🌟minha lista de Desejos para o futuro🌟\n") 
   
NOME_ARQUIVO = "meus_desejos.txt"  
desejos = []  

with open(NOME_ARQUIVO, 'r', ecoding='utf-8') as arquivo: 
    for linha in arquivo: 
      desejos.append(linha.strip())  
      print(f"Meus desejos foram carregados do arquivo '{NOME_ARQUIVO}'!\n")      
    except FileNotFoundError:  
    # se o arquivo nao exixtir, e a primeira vezque o programa esta rodando. 
    print("parece que e sua primeira vez! Vamos criar sua lista de desejos.\n")  
   except Exception as e: 
# captura outros erros inesperados.
print(f"ocorreu um erro ao carregar os desejos: {e}") 

#--- funcao para salvar ops desejos no arquivo---
def salvar_desejos(lista_de_desejos):
      Try: 
         # 'w' significado modo de escrito (white). Ele cria arquivo se nao existir 
         # e apaga o conteudo exitente se o arquivo ja existir.
         # 'encoding="utf-8"' e importante para caracteres especiais (acentos, emojis).
      with open(NOME_ARQUIVO, 'w', encoding='utf-8') as arquivo: 
        for desejos in lista_de_desejos: 
            arquivo.write(desejos + "\n") # Escreva cada desejos seguido de uma nova linha 
        print("\n✅ Seus desejos foram salvos com sucesso!")  
    except Exception as e:   
print(f"\n❌ Erro ao salvar os desejos: {e}")  

# --- loop principal do programa ---
while True: 
 print("\n--- O que voce quer fazer? ---") 
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
     
elif opcao == "2":
print("\n✨ Seus desejos para o futuro ✨") 
if not desejos:
      print("Ainda nao ha desejos na sua lista. Que tal adicionar um?")
else:
      for i, desejos in enumerate(desejos):
         print ("------------------")

elif opcao == "3":
print("Ate a proxima! Continue sonhando alto!👋") 
Break # sai do loop, encerrando o programa  
else:
print("opcao invalida. Por favor, digite 1, 2 ou 3.")