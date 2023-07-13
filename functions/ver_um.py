import json


def ver_usuario(usuarios: list):
    id = input("Qual o id:")
    for usuario in usuarios:
        if usuario["id"] == id:
            print(usuario)


def ver_usuario_da_base_de_dados():
    with open("./base_de_dados.json", "r") as db:
        dict_db = json.load(db)
        ver_usuario(dict_db["usuarios"])
