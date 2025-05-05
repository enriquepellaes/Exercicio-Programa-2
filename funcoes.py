import random

def rolar_dados(qtd_dados: int) -> list[int]:
    return [random.randint(1, 6) for _ in range(qtd_dados)]

def guardar_dado(dados_rolados: list[int], dados_no_estoque: list[int], indice: int) -> list[list[int]]:
    novos_rolados = dados_rolados.copy()
    novos_estoque = dados_no_estoque.copy()
    valor = novos_rolados.pop(indice)
    novos_estoque.append(valor)
    return [novos_rolados, novos_estoque]

def remover_dado(dados_rolados: list[int], dados_no_estoque: list[int], indice: int) -> list[list[int]]:
    novos_rolados = dados_rolados.copy()
    novos_estoque = dados_no_estoque.copy()
    valor = novos_estoque.pop(indice)
    novos_rolados.append(valor)
    return [novos_rolados, novos_estoque]

def calcula_pontos_regra_simples(dados: list[int]) -> dict[int, int]:
    pontos = {}
    for face in range(1, 7):
        pontos[face] = dados.count(face) * face
    return pontos

def calcula_pontos_soma(dados: list[int]) -> int:
    total = 0
    for valor in dados:
        total += valor
    return total

def calcula_pontos_sequencia_baixa(dados: list[int]) -> int:
    faces = set(dados)
    for start in range(1, 4):
        if all(n in faces for n in range(start, start + 4)):
            return 15
    return 0