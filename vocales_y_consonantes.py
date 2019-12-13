
texto_del_usuario = input("Dime una texto:")

puntos = "."

comas = ","

espacios = " "



n_puntos = 0
n_comas = 0
n_espacios = 0


for signo in texto_del_usuario:
    if signo in puntos:
        n_puntos += 1
    if signo in comas:
        n_comas += 1
    if signo in espacios:
        n_espacios += 1

print("Los puntos son {}".format(n_puntos))
print("Las comas son {}".format(n_comas))
print("Los espacios son {}".format(n_espacios))
