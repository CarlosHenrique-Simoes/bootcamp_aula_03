print("Bem vindos a bilheteria da montanha russa do parque de diversões.")

altura = int(input("Digite sua altura: "))
conta = 0

if altura >= 120:
    print("Entrada permitida na montanha russa.")
    idade = int(input("Digite sua idade: "))

    if idade <= 12:
        conta = 5
        print("Valor da entrada: R$ 5,00")
    elif idade <= 18:
        conta = 7
        print("Valor da entrada: R$ 7,00")

    elif idade <= 45 and idade >= 55:
        conta = 0
        print("Valor da entrada: R$ 0,00")
    else:
        conta = 12
        print("Valor da entrada: R$ 12,00")

    fotos = input("Gostaria de tirar uma foto? (S/N): ")

    if fotos == "S":
        conta += 3

    print(f"Total a pagar: R$ {conta},00")
else:
    print("""Infelizmente você ainda não pode entrar na montanha russa,
    tente o carrossel.""")
