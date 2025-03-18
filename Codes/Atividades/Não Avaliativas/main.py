# criar um função que mostre o nome de uma receita
 
# desenvolva uma função que alimente um vetor de ingredientes
# adiciona_ingredientes
 
# desenvolva uma função SAIR
 
# mostre na tela os ingredientes da receita 

# Bolo de Maça ==> TORTA DI MELE
import os 

def titulo():
    print("""
▀█▀ █▀█ █▀█ ▀█▀ ▄▀█   █▀▄ █   █▀▄▀█ █▀▀ █░░ █▀▀
░█░ █▄█ █▀▄ ░█░ █▀█   █▄▀ █   █░▀░█ ██▄ █▄▄ ██▄""")
    
def exibir_menu():
    # criar menu
    print("\n")
    print("1. Adicionar Ingredientes")
    print("2. Exibir Ingredientes")
    print("3. Remover Ingrediente")
    print("4. Sair")
    print("\n")

def escolher_menu():
    escolha = int(input("Escola uma opção:"))
    match escolha:
        case 1:
            # função adicionar_ingrediente
            pass
        case 2:
            #função exibir_ingredientes
            pass
        case 3:
            # função remover_ingrediente
            pass
        case 4:
            # função sair()
            pass
        case _:
            pass





def principal():
    os.system("cls")
    titulo()
    exibir_menu()
    escolher_menu()

# ponto de Entrada
if __name__ == "__main__":
    principal()
