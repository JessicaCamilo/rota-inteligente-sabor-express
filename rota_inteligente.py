
# Rota Inteligente - Sabor Express
# Projeto de Inteligência Artificial
# Algoritmos: A* e K-Means

import math
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans

pontos_entrega = {
    "Centro": (2, 8),
    "Jardim Primavera": (4, 7),
    "Vila Nova": (6, 8),
    "Jardim América": (8, 6),
    "Vila Esperança": (7, 3),
    "Jardim São Paulo": (4, 3),
    "Vila União": (2, 4),
    "Jardim das Flores": (6, 1)
}

grafo = {
    "Centro": {"Jardim Primavera": 2, "Vila União": 3},
    "Jardim Primavera": {"Centro": 2, "Vila Nova": 2, "Jardim São Paulo": 4},
    "Vila Nova": {"Jardim Primavera": 2, "Jardim América": 3},
    "Jardim América": {"Vila Nova": 3, "Vila Esperança": 4},
    "Vila Esperança": {"Jardim América": 4, "Jardim das Flores": 3, "Jardim São Paulo": 3},
    "Jardim São Paulo": {"Jardim Primavera": 4, "Vila Esperança": 3, "Vila União": 2},
    "Vila União": {"Centro": 3, "Jardim São Paulo": 2},
    "Jardim das Flores": {"Vila Esperança": 3}
}

def distancia_entre_pontos(ponto1, ponto2):
    x1, y1 = pontos_entrega[ponto1]
    x2, y2 = pontos_entrega[ponto2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def heuristica(atual, destino):
    return distancia_entre_pontos(atual, destino)

def a_estrela(inicio, destino):
    abertos = [inicio]
    custo = {inicio: 0}
    anterior = {}

    while abertos:
        atual = min(
            abertos,
            key=lambda local: custo[local] + heuristica(local, destino)
        )

        if atual == destino:
            caminho = []
            while atual in anterior:
                caminho.append(atual)
                atual = anterior[atual]
            caminho.append(inicio)
            caminho.reverse()
            return caminho, custo[destino]

        abertos.remove(atual)

        for vizinho, distancia in grafo[atual].items():
            novo_custo = custo[atual] + distancia

            if vizinho not in custo or novo_custo < custo[vizinho]:
                custo[vizinho] = novo_custo
                anterior[vizinho] = atual

                if vizinho not in abertos:
                    abertos.append(vizinho)

    return None, float("inf")

inicio = "Centro"
destino = "Jardim das Flores"

rota, distancia = a_estrela(inicio, destino)

locais = list(pontos_entrega.keys())
coordenadas = np.array([pontos_entrega[local] for local in locais])

kmeans = KMeans(
    n_clusters=2,
    random_state=42,
    n_init=10
)

grupos = kmeans.fit_predict(coordenadas)

contagem_grupos = pd.Series(grupos + 1).value_counts().sort_index()

print("===== RESULTADOS =====")
print("Locais analisados:", len(locais))
print("Grupos criados:", len(contagem_grupos))
print("Rota:", " → ".join(rota))
print("Distância total:", distancia, "km")

for grupo, quantidade in contagem_grupos.items():
    print(f"Locais no Grupo {grupo}: {quantidade}")
