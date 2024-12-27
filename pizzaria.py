print("Bem vindo a pizzaria do Carlão.")
tamanho_da_pizza = input("Qual o tamanho da pizza? P, M ou G: ")
peperonni = input("Deseja peperonni? (S/N): ")
queijo_extra = input("Deseja queijo extra? (S/N): ")

VALOR_DA_PIZZA = 0

# TODO - Quanto terá que pagar baseado na escolha do tamanho da pizza.

if tamanho_da_pizza == "P":
    VALOR_DA_PIZZA = 15
elif tamanho_da_pizza == "M":
    VALOR_DA_PIZZA = 20
elif tamanho_da_pizza == "G":
    VALOR_DA_PIZZA = 25

# TODO - Quanto terá que pagar baseado na escolha do peperonni.

if peperonni == "S":
    if tamanho_da_pizza == "P":
        VALOR_DA_PIZZA += 2
    elif tamanho_da_pizza == "M":
        VALOR_DA_PIZZA += 3
    elif tamanho_da_pizza == "G":
        VALOR_DA_PIZZA += 3

# TODO - Quanto terá que pagar baseado na escolha do queijo extra.

if queijo_extra == "S":
    if tamanho_da_pizza == "P":
        VALOR_DA_PIZZA += 1
    elif tamanho_da_pizza == "M":
        VALOR_DA_PIZZA += 1
    elif tamanho_da_pizza == "G":
        VALOR_DA_PIZZA += 1

print(f"Valor da pizza: R$ {VALOR_DA_PIZZA},00")
