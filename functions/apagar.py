import json


def apagar_usuario(usuarios: list):
    id = input("Qual o id:")
    for usuario in usuarios:
        if usuario["id"] == id:
            usuarios.remove(usuario)


def apagar_usuario_da_base_de_dados():
    dict_db = {}

    with open("./base_de_dados.json", "r") as db:
        dict_db = json.load(db)

        with open("./base_de_dados.json", "w") as db:
            try:
                apagar_usuario(dict_db["usuarios"])
                json.dump(dict_db, db)
            except Exception:
                json.dump(dict_db, db)
