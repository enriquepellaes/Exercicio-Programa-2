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