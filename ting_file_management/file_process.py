import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    """Aqui irá sua implementação"""
    OK = True
    for i in range(len(instance)):
        search_data = instance.search(i)
        print(search_data)
        if search_data["nome_do_arquivo"] == path_file:
            OK = False
    lines = txt_importer(path_file)
    if OK:
        data = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(lines),
            "linhas_do_arquivo": lines,
        }
        instance.enqueue(data)
        print(data)


def remove(instance):
    """Aqui irá sua implementação"""
    if len(instance) == 0:
        print("Não há elementos")
    else:
        object = instance.dequeue()
        print(f"Arquivo {object['nome_do_arquivo']} removido com sucesso")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
    try:
        object = instance.search(position)
        print(object)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
