
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9,10, 11, 12, 14, 20, 15, 30, 60, 70]
for indice in range(len(numeros)):
    numero = numeros[indice]
    valor = ""

    if numero % 3 == 0:
       valor += "Fizz"

    if numero % 5 == 0:
        valor += "Buzz"

    if valor != "":
        numeros[indice] = valor


print(numeros)
