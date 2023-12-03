pontuacoes_personagens = []


def media_atributo(matriz):
    num = 1
    for i in matriz:
        print(f'A média do {num}º atributo é {sum(i)/len(i)}')
        num += 1


media_atributo(pontuacoes_personagens)
