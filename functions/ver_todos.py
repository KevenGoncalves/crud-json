import json


def ver_usuarios(usuarios: list):
    for usuario in usuarios:
        print(usuario)


def ver_usuarios_da_base_de_dados():
    with open("./base_de_dados.json", "r") as db:
        dict_db = json.load(db)
        ver_usuarios(dict_db["usuarios"])
