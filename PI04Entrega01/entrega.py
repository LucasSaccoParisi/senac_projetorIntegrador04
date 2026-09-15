# TASK: Fazer um módulo que converte Pé -> Metros -> Pé: Entrada do usuário que define a conversão
#   Jarda → Metros
#   Jarda → Pé

# NOTE: 1 pé = 0,3048 metros
#       1 jarda = 0,9144 metros
#       1 metro = 3,281 pés
#   FORMULAS:
#       Jd para m
#           m = jd * 0,9144
#       jd para pe
#           ft = jd * 3
#       pe para m
#           m = ft * 0,3048


# definindo input
print("""=== Escolha uma das opições ===

1. Jarda → Metro

2. Jarda → Pé

3. Pé → Metro

4. Metro → Pé

""")

user_escolha00 = input("As únicas opções válidas são os números das opções\n> ")


print("\nAgora coloque os seus números\n")

user_Nu01 = input("> ")
print()

# para converter os inputs em numeros
N01 = float(user_Nu01)

userInput = float(user_escolha00)  # para facilitar a programação

# Pegar e calcular o input
match userInput:
    case 1:
        escolha = "Jarda"
        covPara = "Metro"
        resultado = N01 * 0.9144  # Jarda → Metros
    case 2:
        escolha = "Jarda"
        covPara = "Pé"
        resultado = N01 * 3  # Jarda → Pé
    case 3:
        escolha = "Pé"
        covPara = "Metro"
        resultado = N01 * 0.3048  # Pé → Metro
    case 4:
        escolha = "Metro"
        covPara = "Pé"
        resultado = N01 * 3.28084  # Metro → Pé
    case _:
        escolha = "unknown"
        covPara = "unknown"
        resultado = "unknown"

print(f"{escolha}\n\n{N01}\n\n{covPara}\n\nSaída: {resultado}")
