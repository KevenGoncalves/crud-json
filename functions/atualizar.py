import json


def atualizar_usuario(usuarios: list):
    id = input("Qual é o id:")

    for usuario in usuarios:
        if usuario["id"] == id:
            nome = input("Qual é o nome:")
            apelido = input("Qual é o apelido:")

            usuario["nome"] = nome if nome != "" else usuario["nome"]
            usuario["apelido"] = apelido if apelido != "" else usuario["apelido"]


def atualizar_usuario_na_base_de_dados():
    dict_db = {}
    with open("./base_de_dados.json", "r") as db:
        dict_db = json.load(db)

        with open("./base_de_dados.json", "w") as db:
            try:
                atualizar_usuario(dict_db["usuarios"])
                json.dump(dict_db, db)
            except Exception:
                json.dump(dict_db, db)
