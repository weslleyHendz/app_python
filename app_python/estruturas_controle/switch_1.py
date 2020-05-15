def get_dia_semana(dia):
    dias = {
        1:'Domingo',
        2:'Segunda',
    }
    return dias.get(dia, '** inválido **')

if __name__ == '__main__':
    for dia in range(0, 4):
        print(f'{dia}: {get_dia_semana(dia)}')
