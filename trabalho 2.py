pontuacoes = []


def media(vetor):
    pontos = 1
    num = 1
    while pontos >= 0:
        pontos = int(input(f'Digite sua pontuação no jogo {num}: '))
        vetor.append(pontos)
        num += 1
    for i in vetor:
        if i < 0:
            vetor.remove(i)
    soma = sum(vetor)
    print(f'A média de suas pontuações é de {soma/len(vetor)} dividida entre {len(vetor)} jogos')


media(pontuacoes)