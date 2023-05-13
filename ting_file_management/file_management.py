import sys


def txt_importer(path_file):
    """Aqui irá sua implementação"""
    if path_file.split(".")[-1] != "txt":
        print("Formato inválido", file=sys.stderr)
    try:
        with open(path_file, "r") as file:
            return file.read().split("\n")
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
