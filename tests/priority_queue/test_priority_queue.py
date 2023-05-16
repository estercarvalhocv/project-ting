from ting_file_management.priority_queue import PriorityQueue
import pytest

mock_file = [
    {
        "nome_do_arquivo": "lista_de_compra.txt",
        "qtd_linhas": 3,
        "linhas_do_arquivo": ["Tomate", "Alface", "Arroz"],
    },
    {
        "nome_do_arquivo": "numeros_importantes.txt",
        "qtd_linhas": 30,
        "linhas_do_arquivo": ["3.14", "42"],
    },
]


def test_basic_priority_queueing():
    priority_queue = PriorityQueue()

    priority_queue.enqueue(mock_file[0])
    assert len(priority_queue.regular_priority) == 0

    priority_queue.enqueue(mock_file[1])
    assert len(priority_queue.regular_priority) == 1
    assert priority_queue.search(1) == mock_file[1]

    priority_queue.dequeue()
    assert len(priority_queue.high_priority) == 0

    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        priority_queue.search(15)
