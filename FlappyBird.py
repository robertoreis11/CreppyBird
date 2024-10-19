import time
import pygame
import os
import random

#Alterações Grupo 2
from PIL import Image, ImageSequence

TELA_LARGURA = 500
TELA_ALTURA = 800

IMAGEM_CANO = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'caixao.png')))
IMAGEM_CHAO = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'base.jpg')))
IMAGEM_BACKGROUND = pygame.image.load(os.path.join('imgs','background_cemiterio.png'))
IMAGEM_VIDA0 = pygame.image.load(os.path.join('imgs', 'vida0.png'))
IMAGEM_VIDA1 = pygame.image.load(os.path.join('imgs', 'vida1.png'))
IMAGEM_VIDA2 = pygame.image.load(os.path.join('imgs', 'vida2.png'))
IMAGEM_VIDA3 = pygame.image.load(os.path.join('imgs', 'vida3.png'))
IMAGEM_GAME_OVER = pygame.image.load(os.path.join('imgs', 'gameover.png'))

# Alteração Grupo 3
pygame.mixer.init()
musica_de_fundo = pygame.mixer.music.load(os.path.join('sons', 'this-is-halloween-172354.mp3'))
pygame.mixer.music.set_volume(0.5)
som_contagem = pygame.mixer.Sound(os.path.join('sons', 'smw_kick.wav'))
som_pulo = pygame.mixer.Sound(os.path.join('sons', 'mixkit-player-jumping-in-a-video-game-2043.wav'))
som_colisão = pygame.mixer.Sound(os.path.join('sons', 'mixkit-arcade-fast-game-over-233.wav'))
som_pulo.set_volume(0.2)

def contagem(seconds, tela):
    while seconds >= 0:
        tela.blit(IMAGEM_BACKGROUND, (0, 0))
        font = pygame.font.SysFont('arial', 74)
        if seconds == 0:
            text = font.render('GO!', True, (255, 255, 255))
        else:
            text = font.render(str(seconds), True, (255, 255, 255))
        tela.blit(text, (TELA_LARGURA // 2 - text.get_width() // 2, TELA_ALTURA // 2 - text.get_height() // 2))
        pygame.display.flip()
        time.sleep(1)
        seconds -= 1
        som_contagem.play()

def load_gif(filename):
    gif = Image.open(filename)
    frames = []
    for frame in ImageSequence.Iterator(gif):
        frame = frame.convert('RGBA')
        pygame_surface = pygame.image.frombuffer(
            frame.tobytes(), frame.size, frame.mode
        )
        frames.append(pygame.transform.scale2x(pygame_surface))
    return frames

IMAGENS_CORVO = load_gif(os.path.join('imgs', 'crow.gif'))

pygame.font.init()
FONTE_PONTOS = pygame.font.SysFont('arial', 40)

class Passaro:
    IMGS = IMAGENS_CORVO
    ROTACAO_MAXIMA = 25
    VELOCIDADE_ROTACAO = 20
    TEMPO_ANIMACAO = 5
    TEMPO_INVENCIBILIDADE = 60

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angulo = 0
        self.velocidade = 0
        self.altura = self.y
        self.tempo = 0
        self.contagem_imagem = 0
        self.imagem = self.IMGS[0]
        self.invencivel = False
        self.tempo_invencivel = 0

    def pular(self):
        self.velocidade = -10.5
        self.tempo = 0
        self.altura = self.y

    def mover(self):
        self.tempo += 1
        deslocamento = 1.5 * (self.tempo**2) + self.velocidade * self.tempo

        if deslocamento > 16:
            deslocamento = 16
        elif deslocamento < 0:
            deslocamento -= 2

        self.y += deslocamento

        if deslocamento < 0 or self.y < (self.altura + 50):
            if self.angulo < self.ROTACAO_MAXIMA:
                self.angulo = self.ROTACAO_MAXIMA
        else:
            if self.angulo > -90:
                self.angulo -= self.VELOCIDADE_ROTACAO

        # Atualiza o tempo de invencibilidade
        if self.invencivel:
            self.tempo_invencivel -= 1
            if self.tempo_invencivel <= 0:
                self.invencivel = False

    def desenhar(self, tela):
        self.contagem_imagem += 1

        if self.contagem_imagem < self.TEMPO_ANIMACAO:
            self.imagem = self.IMGS[0]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO*2:
            self.imagem = self.IMGS[1]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO*3:
            self.imagem = self.IMGS[2]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO*4:
            self.imagem = self.IMGS[1]
        elif self.contagem_imagem >= self.TEMPO_ANIMACAO*4 + 1:
            self.imagem = self.IMGS[0]
            self.contagem_imagem = 0

        # Efeito visual para invencibilidade (pássaro pisca)
        if self.invencivel and self.tempo_invencivel % 10 < 5:
            return  # Não desenha o pássaro se estiver no intervalo de "piscar"

        imagem_rotacionada = pygame.transform.rotate(self.imagem, self.angulo)
        pos_centro_imagem = self.imagem.get_rect(topleft=(self.x, self.y)).center
        retangulo = imagem_rotacionada.get_rect(center=pos_centro_imagem)
        tela.blit(imagem_rotacionada, retangulo.topleft)

    def get_mask(self):
        return pygame.mask.from_surface(self.imagem)

class Cano:
    DISTANCIA = 300
    VELOCIDADE = 5

    def __init__(self, x):
        self.x = x
        self.altura = 0
        self.pos_topo = 0
        self.pos_base = 0
        self.CANO_TOPO = pygame.transform.flip(IMAGEM_CANO, False, True)
        self.CANO_BASE = IMAGEM_CANO
        self.passou = False
        self.definir_altura()

    def definir_altura(self):
        self.altura = random.randrange(50, 400)
        self.pos_topo = self.altura - self.CANO_TOPO.get_height()
        self.pos_base = self.altura + self.DISTANCIA

    def mover(self):
        self.x -= self.VELOCIDADE

    def desenhar(self, tela):
        tela.blit(self.CANO_TOPO, (self.x, self.pos_topo))
        tela.blit(self.CANO_BASE, (self.x, self.pos_base))

    def colidir(self, passaro):
        passaro_mask = passaro.get_mask()
        topo_mask = pygame.mask.from_surface(self.CANO_TOPO)
        base_mask = pygame.mask.from_surface(self.CANO_BASE)

        distancia_topo = (self.x - passaro.x, self.pos_topo - round(passaro.y))
        distancia_base = (self.x - passaro.x, self.pos_base - round(passaro.y))

        topo_ponto = passaro_mask.overlap(topo_mask, distancia_topo)
        base_ponto = passaro_mask.overlap(base_mask, distancia_base)

        if base_ponto or topo_ponto:
            return True
        else:
            return False

class Chao:
    VELOCIDADE = 5
    LARGURA = IMAGEM_CHAO.get_width()
    IMAGEM = IMAGEM_CHAO

    def __init__(self, y):
        self.y = y
        self.x1 = 0
        self.x2 = self.LARGURA

    def mover(self):
        self.x1 -= self.VELOCIDADE
        self.x2 -= self.VELOCIDADE

        if self.x1 + self.LARGURA < 0:
            self.x1 = self.x2 + self.LARGURA
        if self.x2 + self.LARGURA < 0:
            self.x2 = self.x1 + self.LARGURA

    def desenhar(self, tela):
        tela.blit(self.IMAGEM, (self.x1, self.y))
        tela.blit(self.IMAGEM, (self.x2, self.y))

def desenhar_tela(tela, passaros, canos, chao, pontos, vidas):
    tela.blit(IMAGEM_BACKGROUND, (0, 0))
    
    for passaro in passaros:
        passaro.desenhar(tela)
    for cano in canos:
        cano.desenhar(tela)

    if vidas == 3:
        tela.blit(IMAGEM_VIDA3, (10, 10))
    elif vidas == 2:
        tela.blit(IMAGEM_VIDA2, (10, 10))
    elif vidas == 1:
        tela.blit(IMAGEM_VIDA1, (10, 10))

    chao.desenhar(tela)
    texto = FONTE_PONTOS.render(f"Pontos: {pontos}", 1, (255, 255, 255))
    tela.blit(texto, (TELA_LARGURA - 10 - texto.get_width(), 10))
    pygame.display.update()

def exibir_game_over(tela):
    tela.blit(IMAGEM_VIDA0,(10,10))
    tela.blit(IMAGEM_GAME_OVER, (1, 300))
    pygame.display.update()
    pygame.time.delay(400) 
 
    # Loop para manter a tela de Game Over até que a tecla de espaço seja pressionada 
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE: 
                    main()
                    return


def main():
    passaros = [Passaro(230, 350)]
    chao = Chao(730)
    canos = [Cano(700)]
    tela = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA))
    pontos = 0
    relogio = pygame.time.Clock()
    vidas = 3

    contagem(3, tela)
    pygame.mixer.music.play(-1)

    rodando = True
    while rodando:
        relogio.tick(30)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
                pygame.quit()
                quit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    for passaro in passaros:
                        passaro.pular()
                    som_pulo.play()

        for passaro in passaros:
            passaro.mover()
            chao.mover()

        adicionar_cano = False
        remover_canos = []
        for cano in canos:
            for passaro in passaros:
                if cano.colidir(passaro) and not passaro.invencivel:
                    # Som de colisão e perda de vida
                    som_colisão.play()
                    vidas -= 1
                    passaro.invencivel = True  # Passaro fica invencível
                    passaro.tempo_invencivel = passaro.TEMPO_INVENCIBILIDADE  # Reinicia o tempo de invencibilidade


                if not cano.passou and cano.x < passaro.x:
                    cano.passou = True
                    adicionar_cano = True
                cano.mover()
            if cano.x + cano.CANO_TOPO.get_width() < 0:
                remover_canos.append(cano)

        if adicionar_cano:
            pontos += 1
            canos.append(Cano(600))

        for cano in remover_canos:
            canos.remove(cano)
        for i, passaro in enumerate(passaros):
            if (passaro.y + passaro.imagem.get_height()) > chao.y or passaro.y < 0:
                vidas-= 1
       
        if vidas == 0:
            exibir_game_over(tela)

        desenhar_tela(tela, passaros, canos, chao, pontos, vidas)

if __name__ == '__main__':
    main()
