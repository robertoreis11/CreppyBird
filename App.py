import modulos.elementos as elementos
from modulos.config import pygame, random, recorde, TELA_LARGURA, TELA_ALTURA
from modulos.utilidades import desenhar_tela, contagem
from CreepyCarnival import carnival, carregar_carnival, alternar_carnival, verifica_score


class Passaro:
    IMGS = elementos.IMAGENS_CORVO
    ROTACAO_MAXIMA = 5  # Limitar rotação horizontal (próximo de 0º)
    VELOCIDADE_ROTACAO = 2  # Suavizar a velocidade de rotação
    VELOCIDADE_MAXIMA = 10  # Limitar a velocidade de queda
    VELOCIDADE_PULO = -6  # Velocidade de pulo
    GRAVIDADE = 0.8  # Suavizar a gravidade
    TEMPO_ANIMACAO = 5
    TEMPO_INVENCIBILIDADE = 60

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angulo = 0  # Iniciar sem inclinação
        self.velocidade = 0
        self.altura = self.y
        self.tempo = 0
        self.contagem_imagem = 0
        self.imagem = self.IMGS[0]
        self.invencivel = False
        self.tempo_invencivel = 0

    def pular(self):
        self.velocidade = self.VELOCIDADE_PULO
        self.tempo = 0
        self.altura = self.y

    def mover(self):
        self.tempo += 1
        deslocamento = self.GRAVIDADE * (self.tempo ** 2) + self.velocidade * self.tempo

        # Limitar o deslocamento máximo para que a queda seja suave
        if deslocamento > self.VELOCIDADE_MAXIMA:
            deslocamento = self.VELOCIDADE_MAXIMA
        elif deslocamento < 0:  # Se estiver subindo, deslocamento negativo
            deslocamento -= 2

        self.y += deslocamento

        # Manter a rotação horizontal e suave (perto de 0º)
        if deslocamento < 0 or self.y < (self.altura + 50):
            if self.angulo < self.ROTACAO_MAXIMA:
                self.angulo = self.ROTACAO_MAXIMA  # Leve inclinação para cima
        else:
            if self.angulo > 0:  # Limitar para manter na horizontal
                self.angulo -= self.VELOCIDADE_ROTACAO

        # Atualizar invencibilidade
        if self.invencivel:
            self.tempo_invencivel -= 1
            if self.tempo_invencivel <= 0:
                self.invencivel = False


    def desenhar(self, tela):
        self.contagem_imagem += 1

        # Animação do pássaro
        if self.contagem_imagem < self.TEMPO_ANIMACAO:
            self.imagem = self.IMGS[0]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO*2:
            self.imagem = self.IMGS[1]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO*3:
            self.imagem = self.IMGS[0]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO*4:
            self.imagem = self.IMGS[1]
        elif self.contagem_imagem >= self.TEMPO_ANIMACAO*4 + 1:
            self.imagem = self.IMGS[0]
            self.contagem_imagem = 0

        # Efeito de piscar para invencibilidade
        if self.invencivel and self.tempo_invencivel % 10 < 5:
            return  # Não desenha o pássaro durante o "piscar"

        # Rotação do pássaro
        imagem_rotacionada = pygame.transform.rotate(self.imagem, self.angulo)
        pos_centro_imagem = self.imagem.get_rect(topleft=(self.x, self.y)).center
        retangulo = imagem_rotacionada.get_rect(center=pos_centro_imagem)
        tela.blit(imagem_rotacionada, retangulo.topleft)

    def get_mask(self):
        return pygame.mask.from_surface(self.imagem)


class Cano:
    DISTANCIA = 300
    VELOCIDADE = 5
    AJUSTE_ALTURA = 50  # Novo: ajuste para baixar a posição da aranha

    
    CANO_TOPO = elementos.IMAGEM_ARANHA 
    CANO_BASE = elementos.IMAGEM_CANO    

    def __init__(self, x):
        self.x = x
        self.altura = 0
        self.pos_topo = 0
        self.pos_base = 0
        self.passou = False
        self.definir_altura()

    def definir_altura(self):
        self.altura = random.randrange(50, 400)
        self.pos_topo = self.altura - self.CANO_TOPO.get_height() + self.AJUSTE_ALTURA  # Modificado: adicionado AJUSTE_ALTURA
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
    LARGURA = elementos.IMAGEM_CHAO.get_width()
    IMAGEM = elementos.IMAGEM_CHAO

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


class bater:
    def mostrar_recorde(self, pontos, tela):
        global recorde
        if pontos > recorde:
            recorde = pontos

        
        # Exibe a imagem da Pontuação 
        tela.blit(elementos.IMAGEM_FUNDO_PONTUACAO,(10,300))
        tela.blit(elementos.IMAGEM_MENOR_PONTUACAO, (60, 320))
        tela.blit(elementos.IMAGEM_RECORDE, (300, 320))
        # Atribui a uma variável o valor da pontuação
        txt_menor_pontuacao = elementos.FONTE_PONTOS_FINAIS.render(f"{pontos}", 1, (255, 255, 255))
        txt_recorde = elementos.FONTE_PONTOS_FINAIS.render(f"{recorde}", 1, (255, 255, 255))
        
        # Exibe o valor da Pontuação
        tela.blit(txt_menor_pontuacao, (90, 350))
        tela.blit(txt_recorde, (350, 350))
        
    def exibir_game_over(self, tela):
        tela.blit(elementos.IMAGEM_VIDA0, (10, 10))
        tela.blit(elementos.IMAGEM_GAME_OVER, (1, 220))
        botao_reiniciar_posicao = elementos.IMAGEM_REINICIAR.get_rect(center=(250, 450))
        botao_inicio_posicao = elementos.IMAGEM_TELA_INICIAL.get_rect(center=(250, 520))
        tela.blit(elementos.IMAGEM_REINICIAR, botao_reiniciar_posicao.topleft)
        tela.blit(elementos.IMAGEM_TELA_INICIAL, botao_inicio_posicao.topleft)

        pygame.display.update()
        pygame.time.delay(400) 
    
        # Loop para manter a tela de Game Over até que a tecla de espaço seja pressionada 
        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if evento.type == pygame.MOUSEBUTTONDOWN:
                        if botao_reiniciar_posicao.collidepoint(evento.pos):
                            # reiniciar_velocidade()
                            main(REINICIOU=1)  # Reinicia o jogo
                            return
                        if botao_inicio_posicao.collidepoint(evento.pos):
                            # reiniciar_velocidade()
                            main(REINICIOU=0)  # Vai para a tela inicial
                            return
                    if evento.type == pygame.KEYDOWN:
                        if evento.key == pygame.K_SPACE:
                            main(REINICIOU=1)  # Reinicia o jogo com a tecla de espaço
                            return

#// alteraçôes Grupo 1
def tela_inicial():
    tela2 = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA))
    font_nick = pygame.font.Font(None, 25)
    nick_usuario = ''
    largura_nick = 230
    campo_nick = pygame.Rect(140, 270, largura_nick, 20)

    imagem_fundo_tela = pygame.image.load('./imgs/background_inicial.png')
    imagem_fundo_tela_re = pygame.transform.scale(imagem_fundo_tela, (TELA_LARGURA, TELA_ALTURA))

    pygame.mixer.init()
    elementos.MUSICA_DE_FUNDO_DO_JOGO.play(-1)
    volume_inicio = 0.1
    elementos.MUSICA_DE_FUNDO_DO_JOGO.set_volume(volume_inicio)

    progresso_barra = 20
    largura_barra = 200
    tela_inicio = True

    while tela_inicio:
        tela2.blit(imagem_fundo_tela_re, (0, 0))
        nome_jogo = elementos.NOME_JOGO
        nome_jogo_re = pygame.transform.scale(nome_jogo, (300, 300))
        nome_jogo_posi = nome_jogo_re.get_rect(center=(250, 110))
        tela2.blit(nome_jogo_re, nome_jogo_posi)

        nome_nickname = elementos.NOME_NICKNAME
        nome_nickname_re = pygame.transform.scale(nome_nickname, (200, 200))
        nome_nickname_posi = nome_nickname_re.get_rect(center=(250, 240))
        tela2.blit(nome_nickname_re, nome_nickname_posi)

        botao_play_img = elementos.BOTAO_PLAY_IMG
        botao_play_re = pygame.transform.scale(botao_play_img, (150, 100))
        botao_play_posicao = botao_play_re.get_rect(center=(250, 370))
        tela2.blit(botao_play_re, botao_play_posicao)

        botao_quit_img = elementos.BOTAO_QUIT_IMG
        botao_quit_re = pygame.transform.scale(botao_quit_img, (150, 100))
        botao_quit_posicao = botao_quit_re.get_rect(center=(250, 490))
        tela2.blit(botao_quit_re, botao_quit_posicao)

        botao_volume_mais = elementos.BOTAO_VOLUME_MAIS
        botao_volume_mais_re = pygame.transform.scale(botao_volume_mais, (50, 50))
        botao_volume_mais_posi = botao_volume_mais_re.get_rect(center=(370, 700))
        tela2.blit(botao_volume_mais_re, botao_volume_mais_posi)

        botao_volume_menos = elementos.BOTAO_VOLUME_MENOS
        botao_volume_menos_re = pygame.transform.scale(botao_volume_menos, (50, 50))
        botao_volume_menos_posi = botao_volume_menos_re.get_rect(center=(130, 700))
        tela2.blit(botao_volume_menos_re, botao_volume_menos_posi)

        barra_volume = pygame.draw.rect(tela2, (255, 255, 255), (150, 690, largura_barra, 20))
        pygame.draw.rect(tela2, (153, 204, 50), (150, 690, progresso_barra, 20))

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()

            if evento.type == pygame.MOUSEBUTTONDOWN:
                if botao_play_posicao.collidepoint(evento.pos):
                    elementos.MUSICA_DE_FUNDO_DO_JOGO.stop()
                    return  # Retorna para a main() para iniciar o jogo

                if botao_quit_posicao.collidepoint(evento.pos):
                    pygame.quit()
                    quit()

                if botao_volume_mais_posi.collidepoint(pygame.mouse.get_pos()):
                    if volume_inicio < 1:
                        volume_inicio += 0.10
                        elementos.MUSICA_DE_FUNDO_DO_JOGO.set_volume(volume_inicio)

                        if progresso_barra < largura_barra:
                            progresso_barra += 20
                            pygame.time.delay(1)

                if botao_volume_menos_posi.collidepoint(pygame.mouse.get_pos()):
                    if volume_inicio > 0:
                        volume_inicio -= 0.10
                        elementos.MUSICA_DE_FUNDO_DO_JOGO.set_volume(volume_inicio)

                        if progresso_barra > 0:
                            progresso_barra -= 20
                            pygame.time.delay(1)

                        elif progresso_barra == 0:
                            volume_inicio = 0.0

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN and nick_usuario != '':
                    texto_exibir = f'Bem Vindo {nick_usuario}!'
                    texto_exibir_re = font_nick.render(texto_exibir, True, (255, 255, 255))
                    tela2.blit(texto_exibir_re, (20, 20))

                elif evento.key == pygame.K_BACKSPACE:
                    nick_usuario = nick_usuario[:-1]

                elif font_nick.render(nick_usuario, True, (255, 255, 255)).get_width() < largura_nick - 5:
                    nick_usuario += evento.unicode

            pygame.draw.rect(tela2, (0, 0, 0), campo_nick, 2)
            nick_re = font_nick.render(nick_usuario, True, (255, 255, 255))
            tela2.blit(nick_re, campo_nick)

            pygame.display.update()


# Variável para controlar o último múltiplo de 100
ultimo_multiplo_100 = 0

def main(REINICIOU=0):
    global ultimo_multiplo_100  # Tornar o último múltiplo de 100 acessível dentro da função
    
    if REINICIOU == 0:
        tela_inicial()

    passaros = [Passaro(230, 350)]
    chao = Chao(700)
    canos = [Cano(700)]
    tela = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA))
    pontos = 0
    relogio = pygame.time.Clock()
    vidas = 3
    pygame.mixer.music.play(-1)
    contagem(3, tela, elementos.SOM_CONTAGEM, elementos.IMAGEM_BACKGROUND)
    rodando = True
    jogo_pausado = False
    pygame.mixer.music.set_volume(0.5)

    Cano.VELOCIDADE = 5

    indice_personagem_atual = 0
    indice_fundo_atual = 0
    indice_obstaculo_atual = 0
    indice_som_fundo_atual = 0 

    while rodando:
        relogio.tick(30)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
                pygame.quit()
                quit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE and not jogo_pausado:
                    for passaro in passaros:
                        passaro.pular()
                        elementos.SOM_PULO.play()
                if evento.key == pygame.K_p:
                    jogo_pausado = not jogo_pausado
                    if not jogo_pausado:
                        contagem(2, tela, elementos.SOM_CONTAGEM, elementos.IMAGEM_BACKGROUND)

        if jogo_pausado:
            # Exibir a mensagem de "PAUSE"
            font = pygame.font.SysFont('arial', 74)
            text = font.render('PAUSE', True, (255, 255, 255))
            tela.blit(elementos.IMAGEM_BACKGROUND, (0, 0))
            tela.blit(text, (TELA_LARGURA // 2 - text.get_width() // 2, TELA_ALTURA // 2 - text.get_height() // 2))
            pygame.display.flip()
            continue

        # Atualização dos movimentos dos objetos
        for passaro in passaros:
            passaro.mover()
            chao.mover()
        if (passaro.y < 0):
            passaro.y += 10
        if (passaro.y > 600):
            passaro.y -= 10

        adicionar_cano = False
        remover_canos = []
        for cano in canos:
            for passaro in passaros:
                if cano.colidir(passaro) and not passaro.invencivel:
                    elementos.SOM_COLISAO.play()
                    vidas -= 1
                    if vidas == 0:
                        pygame.mixer.music.stop()
                        elementos.SOM_GAME_OVER.play()
                    passaro.invencivel = True
                    passaro.tempo_invencivel = passaro.TEMPO_INVENCIBILIDADE

                if not cano.passou and cano.x < passaro.x - 100:
                    cano.passou = True
                    adicionar_cano = True
                cano.mover()

            if cano.x + cano.CANO_TOPO.get_width() < 0:
                remover_canos.append(cano)

        if adicionar_cano:
            pontos += 20
            canos.append(Cano(600))
            if pontos % 50 == 0:
                Cano.VELOCIDADE += 3

        for cano in remover_canos:
            canos.remove(cano)

         # Ajustado para o pássaro não perder as 3 vidas quando tocar no chão ou no topo da tela
          
        if vidas == 0:
            bater().mostrar_recorde(pontos, tela)
            bater().exibir_game_over(tela)
            
        # Atualizar os recursos do jogo quando atingir um múltiplo de 100
        if pontos % 100 == 0 and pontos > 0 and pontos != ultimo_multiplo_100:
            indice_personagem_atual += 1
            if indice_personagem_atual >= len(elementos.PERSONAGENS):
                indice_personagem_atual = 0

            indice_fundo_atual += 1
            if indice_fundo_atual >= len(elementos.IMAGENS_BACKGROUND):
                indice_fundo_atual = 0  # Corrigido para reiniciar corretamente o índice de fundo

            indice_obstaculo_atual += 1
            if indice_obstaculo_atual >= len(elementos.OBSTACULOS):
                indice_obstaculo_atual = 0

            indice_som_fundo_atual += 1
            if indice_som_fundo_atual >= len(elementos.IMAGENS_BACKGROUND):
                indice_som_fundo_atual = 0  # Para garantir que o som reinicie corretamente

            som_fundo_atual = elementos.IMAGENS_BACKGROUND[indice_som_fundo_atual]['som_fundo']


            # Atualiza os recursos do jogo com base nos novos índices
            passaros[0].IMGS = elementos.PERSONAGENS[indice_personagem_atual]['imagens']
            elementos.SOM_PULO = elementos.PERSONAGENS[indice_personagem_atual]['som_pulo']
            som_fundo_atual = elementos.IMAGENS_BACKGROUND[indice_som_fundo_atual]['som_fundo']
            pygame.mixer.music.load(som_fundo_atual)  # Carrega a música de fundo
            pygame.mixer.music.play(-1)  # Toca a música em loop 
            elementos.IMAGEM_BACKGROUND = elementos.IMAGENS_BACKGROUND[indice_fundo_atual]['imagem']
            Cano.CANO_TOPO = elementos.OBSTACULOS[indice_obstaculo_atual]['topo']
            Cano.CANO_BASE = elementos.OBSTACULOS[indice_obstaculo_atual]['base']
        
            # Marca o último múltiplo de 100
            ultimo_multiplo_100 = pontos
            
            print(f"Índice Personagem: {indice_personagem_atual}, Índice Fundo: {indice_fundo_atual}, Índice Obstáculo: {indice_obstaculo_atual}")

        # Exibe a tela
        desenhar_tela(
            tela,
            passaros,
            canos,
            chao,
            pontos,
            vidas,
            elementos.IMAGEM_BACKGROUND,
            elementos.IMAGEM_VIDA1,
            elementos.IMAGEM_VIDA2,
            elementos.IMAGEM_VIDA3,
            elementos.FONTE_PONTOS
        )



if __name__ == '__main__':
    main()  # Chama a main para iniciar o jogo

    # Controle de estado para eventos
    estado_jogo = 'pausado'
    IMAGENS_CORVO = pygame.image.load('imgs', 'crow.gif')
    IMAGEM_BACKGROUND_ORIGINAL = pygame.image.load('imgs', 'background_cemiterio.png')

running = True

while running:
    # Processa eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False

# Segredo: Ativa/desativa o Carnaval
if estado_jogo == "pausado":  # Apenas no estado pausado
    if evento.key == pygame.K_c:
        alternar_carnival()

        # Atualiza o jogo se o Carnaval for ativado
        if carnival:
            IMAGENS_CORVO = pygame.image.load('boneco_de_olinda.png')
            IMAGEM_BACKGROUND_ORIGINAL = pygame.image.load('campos_atacados.png')
        else:
            IMAGENS_CORVO = pygame.image.load("sprite_original.png")
            IMAGEM_BACKGROUND_ORIGINAL = pygame.image.load("fundo_original.png")