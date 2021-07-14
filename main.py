import os.path
import pygame.display
from base_game import *

#---Toda lógica de programação---#

def main():
    passaros = [Passaro(230, 350)]
    chao = Chao(670)
    canos = [Cano(690)]
    tela = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA))
    pontos = 0
    relogio = pygame.time.Clock()

    rodando = True
    while rodando:
        relogio.tick(25)

        # Interação do usuário como o game.
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    for passaro in passaros:
                        passaro.pular()

        # Movimentação de cenário e objetos
        for passaro in passaros:
            passaro.mover()
        chao.mover()

        adicionar_cano = False
        remover_canos = []
        for cano in canos:
            for i, passaro in enumerate(passaros):
                if cano.colidir(passaro):
                    passaros.pop(i)
                if not cano.passou and passaro.x > cano.x:
                    cano.passou = True
                    adicionar_cano = True
            cano.mover()
            if cano.x + cano.CANO_TOPO.get_width() < 0:
                remover_canos.append(cano)

        if adicionar_cano:
            pontos += 1
            canos.append(Cano(600))
            # Níveis e suas dificuldades
            if pontos >= 10:
                Cano.DISTANCIA = 170
                Cano.VELOCIDADE = 7.5
            if pontos >= 15:
                Cano.DISTANCIA = 140
                Cano.VELOCIDADE = 9.5
            if pontos >= 20:
                Cano.DISTANCIA = 110
                Cano.VELOCIDADE = 12
        for cano in remover_canos:
            canos.remove(cano)

        for i, passaro in enumerate(passaros):
            if (passaro.y + passaro.imagem.get_height()) > chao.y or passaro.y < 0:
                passaros.pop(i)

        desenhar_tela(tela, passaros, canos, chao, pontos)
if__name__ = '__main__':
    main()
