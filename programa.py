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
        todas_preenchidas = all(v != -1 for v in cartela['regra_simples'].values()) and all(v != -1 for v in cartela['regra_avancada'].values())
        if todas_preenchidas:
            break
        dados_rolados = rolar_dados(5)
        dados_guardados = []
        rerolls = 0
        while True:
            print(f"Dados rolados: {dados_rolados}", flush=True)
            print(f"Dados guardados: {dados_guardados}", flush=True)
            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:", flush=True)
            escolha = input().strip()
            if escolha == "1":
                print("Digite o índice do dado a ser guardado (0 a 4):", flush=True)
                idx = int(input().strip())
                dados_rolados, dados_guardados = guardar_dado(dados_rolados, dados_guardados, idx)
            elif escolha == "2":
                print("Digite o índice do dado a ser removido (0 a 4):", flush=True)
                idx = int(input().strip())
                dados_rolados, dados_guardados = remover_dado(dados_rolados, dados_guardados, idx)
            elif escolha == "3":
                if rerolls >= 2:
                    print("Você já usou todas as rerrolagens.", flush=True)
                else:
                    rerolls += 1
                    dados_rolados = rolar_dados(len(dados_rolados))
            elif escolha == "4":
                imprime_cartela(cartela)
            elif escolha == "0":
                print("Digite a combinação desejada:", flush=True)
                categoria = input().strip()
                if categoria.isdigit():
                    chave = int(categoria)
                    if chave in cartela['regra_simples']:
                        if cartela['regra_simples'][chave] == -1:
                            faz_jogada(dados_rolados + dados_guardados, categoria, cartela)
                            break
                        else:
                            print("Essa combinação já foi utilizada.", flush=True)
                    else:
                        print("Combinação inválida. Tente novamente.", flush=True)
                else:
                    if categoria in cartela['regra_avancada']:
                        if cartela['regra_avancada'][categoria] == -1:
                            faz_jogada(dados_rolados + dados_guardados, categoria, cartela)
                            break
                        else:
                            print("Essa combinação já foi utilizada.", flush=True)
                    else:
                        print("Combinação inválida. Tente novamente.", flush=True)
            else:
                print("Opção inválida. Tente novamente.", flush=True)
    total_simples = sum(cartela['regra_simples'].values())
    bonus = 35 if total_simples >= 63 else 0
    total = total_simples + bonus + sum(cartela['regra_avancada'].values())
    imprime_cartela(cartela)
    print(f"Pontuação total: {total}", flush=True)

main()