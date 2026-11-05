def inteiros(lista):
    if len(lista) <= 0:
        return False
    contador = 0
    for c in lista:
        if c < lista[contador+1]:
            return inteiros(lista[contador+1:])
        contador += 1
    return False

inteiros([10,22,9,33,21,50,41,60])
