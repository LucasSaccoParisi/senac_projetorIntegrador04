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

# Gráfico 5 - Pizza com % da quantidade produtos vendidos no ano em cada produto

total_produtos = [
    creme_facial.sum(),
    limpeza_facial.sum(),
    pasta_dentaria.sum(),
    sabonete.sum(),
    shampoo.sum(),
    hidratante.sum()
]

nomes_produtos = [
    "Creme Facial",
    "Limpeza Facial",
    "Pasta Dentária",
    "Sabonete",
    "Shampoo",
    "Hidratante"
]

fig, ax = plt.subplots()

ax.pie(
    total_produtos,
    labels=nomes_produtos,
    autopct="%1.1f%%"
)

ax.set_title("Porcentagem de Produtos Vendidos no Ano")

plt.show()