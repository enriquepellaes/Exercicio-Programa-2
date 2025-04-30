import random

def rolar_dados(qtd_dados: int) -> list[int]:
    return [random.randint(1, 6) for _ in range(qtd_dados)]

