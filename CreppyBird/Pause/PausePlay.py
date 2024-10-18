import time
import pygame
import os
import random
# Alterações Grupo 2
# pip install Pillow

from pygame.locals import *
from PIL import Image, ImageSequence

TELA_LARGURA = 500
TELA_ALTURA = 800

IMAGEM_CANO = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'caixao.png')))
IMAGEM_CHAO = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'base.jpg')))
IMAGEM_BACKGROUND_ORIGINAL = pygame.image.load(os.path.join('imgs', 'background_cemiterio.png'))

# Alteração grupo 3
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

# Obtenha as dimensões originais
largura_original = IMAGEM_BACKGROUND_ORIGINAL.get_width()
altura_original = IMAGEM_BACKGROUND_ORIGINAL.get_height()
fator_escala = 0.5
# Cálculo das novas dimensões
TELA_LARGURA = int(largura_original * fator_escala)
TELA_ALTURA = int(altura_original * fator_escala)

# Redimensionando a imagem
IMAGEM_BACKGROUND = pygame.transform.scale(IMAGEM_BACKGROUND_ORIGINAL, (TELA_LARGURA, TELA_ALTURA))

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
FONTE_PONTOS = pygame.font.SysFont('arial', 50)

class Passaro(pygame.sprite.Sprite):
    IMGS = IMAGENS_CORVO 
    # animações da rotação
    ROTACAO_MAXIMA = 25
    VELOCIDADE_ROTACAO = 20
    TEMPO_ANIMACAO = 5

    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.angulo = 0
        self.velocidade = 0
        self.altura = self.y
        self.tempo = 0
        self.contagem_imagem = 0
        self.imagem = self.IMGS[0]
        self.image = self.imagem  # Define a propriedade 'image'
        self.rect = self.image.get_rect(topleft=(self.x, self.y))



    def pular(self):
        self.velocidade = -10.5
        self.tempo = 0
        self.altura = self.y

    def mover(self):
        # calcular o deslocamento
        self.tempo += 1
        deslocamento = 1.5 * (self.tempo**2) + self.velocidade * self.tempo

        # restringir o deslocamento
        if deslocamento > 16:
            deslocamento = 16
        elif deslocamento < 0:
            deslocamento -= 2

        self.y += deslocamento

        # o angulo do passaro
        if deslocamento < 0 or self.y < (self.altura + 50):
            if self.angulo < self.ROTACAO_MAXIMA:
                self.angulo = self.ROTACAO_MAXIMA
        else:
            if self.angulo > -90:
                self.angulo -= self.VELOCIDADE_ROTACAO

    def desenhar(self, tela):
        # definir qual imagem do passaro vai usar
        self.contagem_imagem += 1

        self.image = self.imagem  # Atualiza 'image' para a imagem correta
        imagem_rotacionada = pygame.transform.rotate(self.image, self.angulo)
        pos_centro_imagem = self.image.get_rect(topleft=(self.x, self.y)).center
        retangulo = imagem_rotacionada.get_rect(center=pos_centro_imagem)
        tela.blit(imagem_rotacionada, retangulo.topleft)

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

        # se o passaro tiver caindo eu não vou bater asa
        if self.angulo <= -80:
            self.imagem = self.IMGS[1]
            self.contagem_imagem = self.TEMPO_ANIMACAO*2

        # desenhar a imagem
        imagem_rotacionada = pygame.transform.rotate(self.imagem, self.angulo)
        pos_centro_imagem = self.imagem.get_rect(topleft=(self.x, self.y)).center
        retangulo = imagem_rotacionada.get_rect(center=pos_centro_imagem)
        tela.blit(imagem_rotacionada, retangulo.topleft)

    def get_mask(self):
        return pygame.mask.from_surface(self.imagem)

# Alterações Grupo 5
class Cano:
    DISTANCIA = 200
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

    def mover(self, pontos: float = 0):
        parametro = pontos / 10
        self.x -= self.VELOCIDADE + parametro

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

def desenhar_tela(tela, passaros, canos, chao, pontos):
    tela.blit(IMAGEM_BACKGROUND, (0, 0))
    for passaro in passaros:
        passaro.desenhar(tela)
    for cano in canos:
        cano.desenhar(tela)

    texto = FONTE_PONTOS.render(f"Pontuação: {pontos}", 1, (255, 255, 255))
    tela.blit(texto, (TELA_LARGURA - 10 - texto.get_width(), 10))
    chao.desenhar(tela)
    pygame.display.update()

def jogo():
    passaros = [Passaro(230, 350)]
    chao = Chao(730)
    canos = [Cano(600)]
    pontos = 0
    clock = pygame.time.Clock()
    rodando = True
    contagem(3, tela)
    pygame.mixer.music.play(-1)

    while rodando:
        clock.tick(30)
        chao.mover()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
                break
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    passaros[0].pular()
                    som_pulo.play()

        add_cano = False
        remove_canos = []

        for cano in canos:
            cano.mover(pontos)
            if cano.x + cano.CANO_TOPO.get_width() < 0:
                remove_canos.append(cano)

            if not cano.passou and cano.x < passaros[0].x:
                cano.passou = True
                add_cano = True

            if cano.colidir(passaros[0]):
                som_colisão.play()
                rodando = False
                break

        if add_cano:
            pontos += 1
            canos.append(Cano(600))

        for cano in remove_canos:
            canos.remove(cano)

        for i, passaro in enumerate(passaros):
            passaro.mover()

            if passaro.y + passaro.imagem.get_height() >= 730:
                rodando = False
                break

        desenhar_tela(tela, passaros, canos, chao, pontos)

    pygame.mixer.music.stop()

if __name__ == '__main__':
    pygame.init()
    tela = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA))
    pygame.display.set_caption('Flappy Bird')
    jogo()

# Segunda Alteração Grupo 2
pygame.init()

tela = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA))
pygame.display.set_caption('Pausa')

# Criando o grupo de sprites
todos_sprites = pygame.sprite.Group()
passaro = Passaro(50, 30)
todos_sprites.add(passaro)


# Variável de controle de pausa
pausado = False


# Relógio para controle de FPS
clock = pygame.time.Clock()


# Loop principal do jogo
correndo = True
while correndo:
    # Eventos
    for evento in pygame.event.get():
        if evento.type == QUIT:
            correndo = False


        # Verifica se a tecla "P" foi pressionada para pausar/continuar
        if evento.type == KEYDOWN and evento.key == K_p:
            pausado = not pausado  # Alterna entre pausar e continuar


    # Atualizando os sprites apenas se o jogo não estiver pausado
    if not pausado:
        todos_sprites.update()


    # Atualiza a tela
    tela.fill((255, 255, 255))  # Limpa a tela com a cor branca
    todos_sprites.draw(tela)  # Desenha os sprites
    pygame.display.flip()  # Atualiza a tela


    # Controla a taxa de frames por segundo
    clock.tick(60)

    pygame.quit()