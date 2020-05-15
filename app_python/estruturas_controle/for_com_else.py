PALAVRAS_PROIBIDAS =('futebol', 'religiao', 'politica')
textos = [
    'João gosta de futebol e política',
    'A praia foi divertida',
]

for texto in textos:
    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            print('Testo possui pelo menos uma palavra proibida: ', palavra)
            break
    else:
        print ('Texto autorizado', texto)
