from modulos.config import pygame, os
from modulos.utilidades import load_gif
from modulos.config import TELA_LARGURA, TELA_ALTURA

pygame.mixer.init()
pygame.mixer.music.set_volume(0.3)

pygame.font.init()
# IMAGEMS TELA INICIAL
NOME_JOGO = pygame.image.load('./imgs/game_name.png')
NOME_NICKNAME = pygame.image.load('./imgs/nickname.png')
BOTAO_PLAY_IMG = pygame.image.load('./imgs/botão_play_.png')
BOTAO_QUIT_IMG = pygame.image.load('./imgs/botão_exit_.png')
BOTAO_VOLUME_MAIS = pygame.image.load('./imgs/botao_volume_positivo.png')
BOTAO_VOLUME_MENOS = pygame.image.load('./imgs/botao_volume_negativo.png')

# IMAGENS DE OBSTÁCULOS
IMAGEM_ARANHA = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'aranha.png')))
IMAGEM_CANO = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'caixao.png')))
IMAGEM_CHAO = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'base.jpg')))
IMAGEM_MASCARA1 = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'mascara1.png')))
IMAGEM_MASCARA2 = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'mascara2.png')))


# IMAGENS DE FUNDO
IMAGEM_BACKGROUND = pygame.image.load(os.path.join('imgs','background_cemiterio.png'))
IMAGEM_BACKGROUND2 = pygame.transform.scale(pygame.image.load(os.path.join('imgs','fundoNatalino.jpeg')),(TELA_LARGURA, TELA_ALTURA))
IMAGEM_BACKGROUND3 = pygame.transform.scale(pygame.image.load(os.path.join('imgs','background_carnaval.png')),(TELA_LARGURA, TELA_ALTURA))
IMAGEM_BACKGROUND4 = pygame.transform.scale(pygame.image.load(os.path.join('imgs','fundoTela.jpg')),(TELA_LARGURA, TELA_ALTURA))
IMAGEM_CHAO = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'base.jpg')))

# IMAGENS NA INTERFACE DA GAMEPLAY
IMAGEM_VIDA0 = pygame.image.load(os.path.join('imgs', 'vida0.png'))
IMAGEM_VIDA1 = pygame.image.load(os.path.join('imgs', 'vida1.png'))
IMAGEM_VIDA2 = pygame.image.load(os.path.join('imgs', 'vida2.png'))
IMAGEM_VIDA3 = pygame.image.load(os.path.join('imgs', 'vida3.png'))
FONTE_PONTOS = pygame.font.SysFont('arial', 40)
FONTE_PONTOS_FINAIS = pygame.font.SysFont('arial', 65)

# GAME OVER
IMAGEM_GAME_OVER = pygame.image.load(os.path.join('imgs', 'gameover.png'))
IMAGEM_MENOR_PONTUACAO = pygame.transform.scale(
    pygame.image.load(os.path.join('imgs', 'pontuacao.png')), (120, 25))
IMAGEM_RECORDE = pygame.transform.scale(
    pygame.image.load(os.path.join('imgs', 'recorde-img.png')),(150, 25))
IMAGEM_REINICIAR = pygame.image.load(os.path.join('imgs','botao_reiniciar.png'))
IMAGEM_TELA_INICIAL = pygame.image.load(os.path.join('imgs','botao_tela_inicial.png'))
IMAGEM_FUNDO_PONTUACAO = pygame.image.load(os.path.join('imgs','fundoPontuacao.png'))
BOTAO_INICIO_POSICAO = IMAGEM_TELA_INICIAL

# SONS
MUSICA_DE_FUNDO = pygame.mixer.music.load(os.path.join('sons', 'this-is-halloween-172354.mp3'))
MUSICA_DE_FUNDO_DO_JOGO = pygame.mixer.Sound('./sons/StockTune-Creepy Crawly Capers_1729035356.mp3')
SOM_CONTAGEM = pygame.mixer.Sound(os.path.join('sons', 'smw_kick.wav'))
SOM_PULO = pygame.mixer.Sound(
    os.path.join('sons', 'mixkit-player-jumping-in-a-video-game-2043.wav'))
SOM_COLISAO = pygame.mixer.Sound(os.path.join('sons', 'mixkit-arcade-fast-game-over-233.wav'))

MUSICA_DE_FUNDO_CARNAVAL = pygame.mixer.Sound(os.path.join('sons', 'carnaval_audio.ogg'))
SOM_PULO_CARNAVAL = pygame.mixer.Sound(os.path.join('sons', 'carnaval_audio_salto.ogg'))
SOM_GAME_OVER = pygame.mixer.Sound(
    os.path.join('sons', 'mixkit-evil-dwarf-laugh-421.wav'))
SOM_PULO.set_volume(0.2)
SOM_COLISAO.set_volume(0.3)
SOM_GAME_OVER.set_volume(0.8)

# PERSONAGENS
IMAGENS_CORVO = load_gif(os.path.join('imgs', 'crow.gif'))
IMAGENS_OLINDA = load_gif(os.path.join('imgs', 'olinda.gif'))
IMAGENS_COELHO = load_gif(os.path.join('imgs', 'coelhao.gif'))

# ADICIONAR PERSONAGENS
PERSONAGENS = [
    {'imagens':IMAGENS_CORVO,
     'som_pulo': SOM_PULO},
    
    {'imagens': IMAGENS_OLINDA, 
      'som_pulo': SOM_PULO},

      {'imagens': IMAGENS_COELHO, 
      'som_pulo': SOM_PULO},
]
IMAGENS_BACKGROUND = [
    {'imagem': IMAGEM_BACKGROUND,
     'som_fundo': MUSICA_DE_FUNDO_DO_JOGO},

    {'imagem': IMAGEM_BACKGROUND2,
    'som_fundo': MUSICA_DE_FUNDO_DO_JOGO },

    {'imagem': IMAGEM_BACKGROUND3, 
     'som_fundo': MUSICA_DE_FUNDO_CARNAVAL},
     
     {'imagem': IMAGEM_BACKGROUND4, 
     'som_fundo': MUSICA_DE_FUNDO_DO_JOGO},
]

OBSTACULOS = [
    {'topo': IMAGEM_ARANHA,
     'base': IMAGEM_CANO
    },

    {'topo': IMAGEM_MASCARA1,
     'base': IMAGEM_MASCARA2
    },
]



