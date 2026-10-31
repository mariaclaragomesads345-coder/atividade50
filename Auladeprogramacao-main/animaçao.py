import pygame
import math


pygame.init()
tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("lagarto procedural")
relogio = pygame.time.Clock()

NUM_SEGMENTOS = 15
TAMANHO = 15
segmentos = [[400, 300] for _ in range(NUM_SEGMENTOS)]
angulos = [0.0] * NUM_SEGMENTOS
lingua_extensao = 0
lingua_ativa = False

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button ==1:
            lingua_ativa = True

    dt = relogio.tick(60) / 1000
    # A língua avança depressa e depois recolhe, como um movimento de bote.
    if lingua_ativa:
        lingua_extensao += 150 * dt
        if lingua_extensao >= 38:
            lingua_extensao = 38
            lingua_ativa = False
    else:
        lingua_extensao = max(0, lingua_extensao - 85 * dt)

    rato_x, rato_y = pygame.mouse.get_pos()
    dx = rato_x - segmentos[0][0]
    dy = rato_y - segmentos[0][1]
    dist = math.hypot(dx, dy)

    if dist > 5:
        angulos[0] = math.atan2(dy, dx)
        segmentos[0][0] += math.cos(angulos[0]) * min(dist * 0.08, 4.0)
        segmentos[0][1] += math.sin(angulos[0]) * min(dist * 0.08, 4.0)

    for i in range(1, NUM_SEGMENTOS):
        dx = segmentos[i-1][0] - segmentos[i][0]
        dy = segmentos[i-1][1] - segmentos[i][1]
        angulos[i] = math.atan2(dy, dx)
        segmentos[i][0] = segmentos[i-1][0] - math.cos(angulos[i]) * TAMANHO
        segmentos[i][1] = segmentos[i-1][1] - math.sin(angulos[i]) * TAMANHO

    tela.fill((20, 25, 22))

    tempo = pygame.time.get_ticks() * 0.008
    # Quatro patas com dedos, posicionadas dos dois lados do corpo.
    for idx, lado in [(3, -1), (3, 1), (8, -1), (8, 1)]:
        base_x, base_y = segmentos[idx]
        lado_x = math.cos(angulos[idx] + math.pi / 2) * lado
        lado_y = math.sin(angulos[idx] + math.pi / 2) * lado
        passo = math.sin(tempo + idx) * 4
        cotovelo = (base_x + lado_x * 17, base_y + lado_y * 17)
        pe = (base_x + lado_x * 29 + math.cos(angulos[idx]) * passo,
              base_y + lado_y * 29 + math.sin(angulos[idx]) * passo)
        cor_pata = (62, 137, 65)
        pygame.draw.line(tela, (30, 75, 42), (base_x, base_y), cotovelo, 8)
        pygame.draw.line(tela, cor_pata, (base_x, base_y), cotovelo, 5)
        pygame.draw.line(tela, (30, 75, 42), cotovelo, pe, 7)
        pygame.draw.line(tela, cor_pata, cotovelo, pe, 4)
        for dedo in (-1, 0, 1):
            ponta = (pe[0] + math.cos(angulos[idx] + dedo * 0.55) * 7,
                     pe[1] + math.sin(angulos[idx] + dedo * 0.55) * 7)
            pygame.draw.line(tela, cor_pata, pe, ponta, 2)

    # Corpo robusto, afinando até a ponta da cauda.
    for i in range(NUM_SEGMENTOS - 1, 0, -1):
        raio = max(2, 13 - i * 0.72)
        cor = (72 + min(i, 5) * 2, 145 - min(i, 10) * 3, 69)
        pygame.draw.circle(tela, cor, (int(segmentos[i][0]), int(segmentos[i][1])), int(raio))
        if i in (2, 4, 6, 8, 10):
            pygame.draw.circle(tela, (154, 179, 91),
                               (int(segmentos[i][0]), int(segmentos[i][1])), 2)

    # Cabeça larga e focinho apontados na direção do movimento.
    hx, hy = segmentos[0]
    frente = (math.cos(angulos[0]), math.sin(angulos[0]))
    lado = (-frente[1], frente[0])
    def ponto_cabeca(avanco, lateral):
        return (int(hx + frente[0] * avanco + lado[0] * lateral),
                int(hy + frente[1] * avanco + lado[1] * lateral))

    pygame.draw.polygon(tela, (71, 151, 72), [
        ponto_cabeca(-9, -10), ponto_cabeca(3, -13),
        ponto_cabeca(17, -8), ponto_cabeca(19, 0),
        ponto_cabeca(17, 8), ponto_cabeca(3, 13), ponto_cabeca(-9, 10)])
    pygame.draw.ellipse(tela, (173, 190, 101),
                        (int(hx + frente[0] * 10 - 5), int(hy + frente[1] * 10 - 4), 10, 8))
    for lado_olho in (-1, 1):
        olho = ponto_cabeca(3, lado_olho * 9)
        pupila = ponto_cabeca(4, lado_olho * 10)
        pygame.draw.circle(tela, (230, 207, 117), olho, 4)
        pygame.draw.circle(tela, (25, 34, 24), pupila, 2)

    if lingua_extensao > 0:
        base = ponto_cabeca(18, 0)
        ponta = ponto_cabeca(18 + lingua_extensao, 0)
        pygame.draw.line(tela, (221, 61, 83), base, ponta, 3)
        # Língua bifurcada nas duas pontas.
        for lado_ponta in (-1, 1):
            garfo = (ponta[0] + int(frente[0] * 7 + lado[0] * lado_ponta * 5),
                     ponta[1] + int(frente[1] * 7 + lado[1] * lado_ponta * 5))
            pygame.draw.line(tela, (221, 61, 83), ponta, garfo, 2)

    pygame.display.flip()
pygame.quit()
