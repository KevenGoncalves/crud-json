import json
import uuid


def criar_usuario(usuarios: list):
    nome = input("Qual é o nome:")
    apelido = input("Qual é o apelido:")
    id = uuid.uuid4().__str__()

    usuario = {
        "id": id,
        "nome": nome,
        "apelido": apelido
    }

    usuarios.append(usuario)


def criar_na_base_de_dados():
    dict_db = {}
    with open("./base_de_dados.json", "r") as db:
        dict_db = json.load(db)

        with open("./base_de_dados.json", "w") as db:
            try:
                criar_usuario(dict_db["usuarios"])
                json.dump(dict_db, db)
            except Exception:
                json.dump(dict_db, db)
