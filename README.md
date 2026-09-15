# Rota Inteligente: Otimização de Entregas com Algoritmos de IA

## 1. Sobre o projeto

O projeto Rota Inteligente foi desenvolvido para a empresa fictícia Sabor Express, uma pequena empresa de delivery de alimentos.

A empresa enfrenta dificuldades para organizar suas entregas, principalmente em horários de maior movimento. O planejamento manual das rotas pode aumentar as distâncias percorridas, o tempo de entrega e os custos com combustível.

A proposta deste projeto é utilizar técnicas de Inteligência Artificial e estruturas de dados para auxiliar na organização das entregas.

## 2. Objetivos

- Encontrar rotas mais eficientes entre pontos de entrega.
- Representar os locais de entrega por meio de um grafo.
- Utilizar o algoritmo A* para encontrar caminhos de menor custo.
- Agrupar pontos de entrega próximos utilizando K-Means.
- Demonstrar como a Inteligência Artificial pode apoiar decisões logísticas.

## 3. Tecnologias utilizadas

- Python
- Google Colab
- NumPy
- Pandas
- Matplotlib
- NetworkX
- Scikit-learn
- GitHub

## 4. Modelagem do problema

Os locais de entrega foram representados como nós de um grafo.

As conexões entre os locais representam as possíveis rotas, enquanto os valores das conexões representam as distâncias em quilômetros.

Foram utilizados 8 pontos de entrega.

## 5. Algoritmo A*

O algoritmo A* foi utilizado para encontrar uma rota de menor custo entre o ponto de origem e o destino.

A distância total encontrada no experimento foi de 11 km.

## 6. Algoritmo K-Means

O algoritmo K-Means foi utilizado para agrupar os pontos de entrega de acordo com suas posições.

Foram definidos 2 grupos.

O resultado apresentou 4 locais no Grupo 1 e 4 locais no Grupo 2.

## 7. Resultados

Foram analisados 8 locais de entrega.

O algoritmo A* encontrou uma rota de 11 km entre o Centro e o Jardim das Flores.

O K-Means dividiu os 8 locais em 2 grupos, com 4 locais em cada grupo.

## 8. Limitações

O projeto utiliza dados simulados e coordenadas fictícias.

As distâncias representam um modelo simplificado e não consideram trânsito em tempo real, acidentes, obras ou condições das ruas.

O algoritmo A* foi aplicado a uma rota entre origem e destino, não sendo uma solução completa para múltiplas entregas com restrições reais.

O K-Means depende da quantidade de grupos definida previamente.

## 9. Possíveis melhorias

- Utilizar dados reais de mapas e GPS.
- Considerar trânsito em tempo real.
- Considerar capacidade dos veículos.
- Considerar horários de entrega.
- Utilizar vários veículos e entregadores.
- Integrar o sistema com serviços de mapas.

## 10. Estrutura do projeto

src/
    rota_inteligente.py

data/
    entregas.csv

docs/
    mapa_entregas.png
    agrupamento_kmeans.png

requirements.txt
README.md

## 11. Conclusão

O projeto demonstra uma aplicação prática de Inteligência Artificial na área de logística.

A combinação do algoritmo A* para busca de rotas com o K-Means para agrupamento de entregas cria uma solução inicial para apoiar a organização das entregas da Sabor Express.

Embora o modelo seja simplificado, ele apresenta uma base que pode ser ampliada para uma solução mais próxima de um sistema real de otimização logística.
