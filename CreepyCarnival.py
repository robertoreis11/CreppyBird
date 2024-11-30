# Alterações Grupo 5 (CreepyCarnival)

import pygame
from PIL import Image, ImageSequence
from modulos.config import TELA_LARGURA, TELA_ALTURA
from App import main, relogio, rodando
from CreepyCarnival import carregar_carnival, ativar_carnival

personagem_original = pygame.image.load('crow.gif')

# Carregando novos sprites
def carregar_carnival():
    carnival = {
        'fundo_original': pygame.image.load('background_cemiterio.png'),
        'fundo_carnavalesco_1': pygame.image.load('campos_atacados.png'),
        'fundo_carnavalesco_2': pygame.image.load('cidade_atacada.png'),
        'personagem_original': pygame.image.load('crow.gif'),
        'boneco_de_olinda': pygame.image.load('boneco_de_olinda.png'),
    }
    return carnival

carnival = False

# Ativar/Desativar o Carnaval
def alternar_carnival():
    global carnival_ativo
    carnival_ativo = not carnival_ativo

# Altera fundo pelo score
def verifica_score(score, carnival):
    if score >= 20:
        carnival['personagem_original'] = carnival['boneco_de_olinda']