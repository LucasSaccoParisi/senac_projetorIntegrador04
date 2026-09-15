# como o exercicio tem dois enunciados diferentes entre o colab com informações e o notions, os dois foram feitos

import matplotlib.pyplot as plt
import numpy as np

mes = np.arange(12) + 1 # meses de 1 a 12

# quantidades de produtos vendidos por mês. As entradas são de Janeiro a Dezembro
creme_facial = np.array([ 2500, 2630, 2140, 3400, 3600, 2760, 2980, 3700, 3540, 1990, 2340, 2900 ])
limpeza_facial = np.array([ 1500, 1200, 1340, 1130, 1740, 1555, 1120, 1400, 1780, 1890, 2100, 1760 ])
pasta_dentaria = np.array([ 5200, 5100, 4550, 5870, 4560, 4890, 4780, 5860, 6100, 8300, 7300, 7400 ])
sabonete = np.array([ 9200, 6100, 9550, 8870, 7760, 7490, 8980, 9960, 8100, 10300, 13300, 14400 ])
shampoo = np.array([ 1200, 2100, 3550, 1870, 1560, 1890, 1780, 2860, 2100, 2300, 2400, 1800 ])
hidratante = np.array([ 1500, 1200, 1340, 1130, 1740, 1555, 1120, 1400, 1780, 1890, 2100, 1760 ])

# Gráfico 4 - Stack plot com o total de produtos vendidos a cada mês com todos os produtos
fig, ax = plt.subplots()

ax.stackplot(
    mes,
    creme_facial,
    limpeza_facial,
    pasta_dentaria,
    sabonete,
    shampoo,
    hidratante,
    labels=[
        "Creme Facial",
        "Limpeza Facial",
        "Pasta Dentária",
        "Sabonete",
        "Shampoo",
        "Hidratante"
    ]
)

ax.set(
    xlim=(1, 12),
    xticks=np.arange(1, 13),
    ylim=(0, 32000),
    yticks=np.arange(0, 32001, 5000)
)

ax.set_title("Total de Produtos Vendidos por Mês")
ax.set_xlabel("Mês")
ax.set_ylabel("Quantidade Vendida")

ax.legend(loc="upper left")

plt.show()

# grafico 4: Histograma de quantidade de meses (y) e faixas de quantidades de produtos vendidos (1000-1999, 2000-2999, ...)

vendas = np.concatenate([
    creme_facial,
    limpeza_facial,
    pasta_dentaria,
    sabonete,
    shampoo,
    hidratante
])

fig, ax = plt.subplots()

ax.hist(
    vendas,
    bins=np.arange(1000, 16001, 1000),
    edgecolor="white",
    linewidth=0.7
)

ax.set(
    xlabel="Quantidade de Produtos Vendidos",
    ylabel="Quantidade de Ocorrências"
)

ax.set_title("Distribuição da Quantidade de Produtos Vendidos")

plt.show()