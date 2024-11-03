from modulos.config import *


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


def contagem(seconds, tela, som_contagem, img_backgroud):
    while seconds >= 0:
        tela.blit(img_backgroud, (0, 0))
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


def desenhar_tela(tela, passaros, canos, chao, pontos, vidas, img_backgroud, img_vida1, img_vida2, img_vida3, fonte_pontos):
    tela.blit(img_backgroud, (0, 0))
    
    for passaro in passaros:
        passaro.desenhar(tela)
    for cano in canos:
        cano.desenhar(tela)

    if vidas == 3:
        tela.blit(img_vida3, (10, 10))
    elif vidas == 2:
        tela.blit(img_vida2, (10, 10))
    elif vidas == 1:
        tela.blit(img_vida1, (10, 10))

    chao.desenhar(tela)
    texto = fonte_pontos.render(f"Pontos: {pontos}", 1, (255, 255, 255))
    tela.blit(texto, (TELA_LARGURA - 10 - texto.get_width(), 10))
    pygame.display.update()
