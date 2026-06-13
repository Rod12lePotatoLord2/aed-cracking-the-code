def group_anagrams(words: list[str]) -> list[list[str]]:
    anagramas = {}

    for palavra in words:
        chave = "".join(sorted(palavra))

        if chave not in anagramas:
            anagramas[chave] = []

        anagramas[chave].append(palavra)

    return list(anagramas.values())
