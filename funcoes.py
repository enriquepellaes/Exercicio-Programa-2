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

def calcula_pontos_sequencia_alta(dados: list[int]) -> int:
    faces = set(dados)
    for start in range(1, 3):
        if all(n in faces for n in range(start, start + 5)):
            return 30
    return 0

def calcula_pontos_full_house(dados: list[int]) -> int:
    cont = {}
    for v in dados:
        cont[v] = cont.get(v, 0) + 1
    vals = sorted(cont.values())
    if vals == [2, 3]:
        total = 0
        for v in dados:
            total += v
        return total
    return 0

def calcula_pontos_quadra(dados: list[int]) -> int:
    cont = {}
    for v in dados:
        cont[v] = cont.get(v, 0) + 1
    for c in cont.values():
        if c >= 4:
            total = 0
            for x in dados:
                total += x
            return total
    return 0

def calcula_pontos_quina(dados: list[int]) -> int:
    cont = {}
    for v in dados:
        cont[v] = cont.get(v, 0) + 1
    for c in cont.values():
        if c >= 5:
            return 50
    return 0

def calcula_pontos_regra_avancada(dados: list[int]) -> dict[str, int]:
    return {
        'cinco_iguais': calcula_pontos_quina(dados),
        'full_house': calcula_pontos_full_house(dados),
        'quadra': calcula_pontos_quadra(dados),
        'sem_combinacao': calcula_pontos_soma(dados),
        'sequencia_alta': calcula_pontos_sequencia_alta(dados),
        'sequencia_baixa': calcula_pontos_sequencia_baixa(dados),
    }

def faz_jogada(dados: list[int], categoria: str, cartela_de_pontos: dict) -> dict:
    pontos_simples = calcula_pontos_regra_simples(dados)
    pontos_avancada = calcula_pontos_regra_avancada(dados)
    if categoria.isdigit():
        chave = int(categoria)
        cartela_de_pontos['regra_simples'][chave] = pontos_simples[chave]
    else:
        cartela_de_pontos['regra_avancada'][categoria] = pontos_avancada[categoria]
    return cartela_de_pontos

def imprime_cartela(cartela):
    print("Cartela de Pontos:")
    print("-"*25)    
    for i in range(1, 7):
        filler = " " * (15 - len(str(i)))
        if cartela['regra_simples'][i] != -1:
            print(f"| {i}: {filler}| {cartela['regra_simples'][i]:02} |")
        else:
            print(f"| {i}: {filler}|    |")
    for i in cartela['regra_avancada'].keys():
        filler = " " * (15 - len(str(i)))
        if cartela['regra_avancada'][i] != -1:
            print(f"| {i}: {filler}| {cartela['regra_avancada'][i]:02} |")
        else:
            print(f"| {i}: {filler}|    |")
    print("-"*25)

from funcoes import (
    rolar_dados, guardar_dado, remover_dado,
    calcula_pontos_regra_simples, calcula_pontos_regra_avancada,
    faz_jogada, imprime_cartela
)

def main():
    cartela = {
        'regra_simples': {i: -1 for i in range(1, 7)},
        'regra_avancada': {
            'sem_combinacao': -1,
            'quadra': -1,
            'full_house': -1,
            'sequencia_baixa': -1,
            'sequencia_alta': -1,
            'cinco_iguais': -1
        }
    }

    while True:
        todas_preenchidas = all(
            v != -1 for v in cartela['regra_simples'].values()
        ) and all(
            v != -1 for v in cartela['regra_avancada'].values()
        )
        if todas_preenchidas:
            break

        dados_rolados = rolar_dados(5)
        dados_guardados = []
        rerolls = 0

        while True:
            print(f"Dados rolados: {dados_rolados}")
            print(f"Dados guardados: {dados_guardados}")
            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
            escolha = input().strip()