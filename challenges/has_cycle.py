def has_cycle(graph: dict) -> bool:
    visitados = set()
    pilha_recursao = set()

    def dfs(node) -> bool:
        if node in pilha_recursao:
            return True
        if node in visitados:
            return False

        pilha_recursao.add(node)
        visitados.add(node)

        for vizinho in graph.get(node, []):
            if dfs(vizinho):
                return True

        pilha_recursao.remove(node)
        return False

    for vertex in graph:
        if vertex not in visitados:
            if dfs(vertex):
                return True

    return False
