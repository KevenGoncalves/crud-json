import os
from functions import criar
from functions import ver_todos
from functions import ver_um
from functions import apagar
from functions import atualizar


while True:
    print("""
          1 - Criar
          2 - Ver Todos
          3 - Ver Um
          4 - Apagar
          5 - Atualizar
          6 - Sair
          """)

    opcao = input(":")
    if opcao == "1":
        os.system("clear")
        criar.criar_na_base_de_dados()
        os.system("clear")

    elif opcao == "2":
        os.system("clear")
        ver_todos.ver_usuarios_da_base_de_dados()

    elif opcao == "3":
        os.system("clear")
        ver_um.ver_usuario_da_base_de_dados()

    elif opcao == "4":
        os.system("clear")
        apagar.apagar_usuario_da_base_de_dados()
        os.system("clear")

    elif opcao == "5":
        os.system("clear")
        atualizar.atualizar_usuario_na_base_de_dados()
        os.system("clear")

    elif opcao == "6":
        break
