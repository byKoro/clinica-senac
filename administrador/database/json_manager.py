import json
def salvar_json(caminho, dados):
    with open(caminho, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=4)

def carregar_json(caminho):
    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def adicionar_json(caminho, dados):
    adicionar = carregar_json(caminho)
    adicionar.append(dados)
    salvar = salvar_json(caminho,adicionar)
    return