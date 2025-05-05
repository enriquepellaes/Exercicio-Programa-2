import random

def rolar_dados(qtd_dados: int) -> list[int]:
    return [random.randint(1, 6) for _ in range(qtd_dados)]

def guardar_dado(dados_rolados: list[int], dados_no_estoque: list[int], indice: int) -> list[list[int]]:
    novos_rolados = dados_rolados.copy()
    novos_estoque = dados_no_estoque.copy()
    valor = novos_rolados.pop(indice)
    novos_estoque.append(valor)
    return [novos_rolados, novos_estoque]