def imprimir(maximo, atual):
    if atual < maximo:
        print (atual)
        imprimir(maximo, atual + 1)


imprimir(100, 1)
