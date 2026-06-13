from data_structures.node import Node


def lowest_common_ancestor(
    root: Node | None,
    value1: int,
    value2: int,
) -> int:
    atual = root

    while atual is not None:
        if value1 < atual.value and value2 < atual.value:
            atual = atual.left
        elif value1 > atual.value and value2 > atual.value:
            atual = atual.right
        else:
            return atual.value

    return -1
