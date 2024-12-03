# CreepyThings - Halloween; Christmas; Carnival; Easter - Edition &#x1F383; &#x1F385; &#x1F3AD; &#x1F430;

## Visão geral

<b>CreepyThings</b> é uma recriação do clássico Flappy Bird, mas com um toque assustador, carnavalesco, natalino e pascual, em vez de guiar um pássaro alegre através de canos, você controla um corvo sombrio voando através de um cemitério cheio de lápides e árvores mortas, ao atingir certa pontuação, o senário e o personagem mudam para um bode em um tema nataino, em outro momento é alterado para um tema carnavalesco,por fim é alterado para o tema de páscoa com o coelho como personagem.O desafio permanece o mesmo: sobreviver o máximo possível sem colidir com os obstáculos. No entanto, agora o ambiente está repleto de sombras, sons arrepiantes e uma atmosfera sombria em todas as temáticas do jogo.

Prepare-se para uma experiência divertida, aterrorizante, natalina e carnavalesca, com gráficos inspirados no mundo do terror e sons que farão sua espinha gelar.

<hr></hr>

<br></br>

## 🎮 Funcionalidades

<ul>
    <li><b>Personagem Principal</b>: O personagem muda no decorrer do jogo, começando com um corvo, depois bode, boneco de olinda e por fim um coelho.</li>
    <li><b>Obstáculos dos Temas</b>: Cada temática tem seus proprios obstaculos assustadores e divertiods.</li>
    <li><b>Cenários dos Temas</b>: Cada temática tem seu proprio senário inspirado no tema.</li>
    <li><b>Efeitos dos temas</b>: Com cada mudança de senário os efeitos sonoros também são alterados de acordo com o tema.</li>
    <li><b>Música Temática</b>: Uma trilha sonora sombria para complementar a atmosfera de de cada senário.</li>
    <li><b>Sistema de Pontuação</b>: A cada obstáculo superado, sua pontuação aumenta.</li>
    <li><b>Dificuldades</b>: Quanto maior os pontos, mais veloz fica o desafio, e ocorre a mudança de senário a cada 200 pontos.</li>
</ul>

<hr></hr>

<br></br>

## 🧛‍♂️ Requisitos

<ul>
    <li><b>Python:</b> 3.7 ou superior</li>
    <li><b>Sistema Operacional:</b> Windows 7 ou maior (64 bit)</li>
    <li><b>Processador:</b> 1.7+ GHz ou melhor</li>
    <li><b>Memória:</b> 2 GB de RAM</li>
    <li><b>Armazenamento:</b> 50,0 MB de espaço disponível</li>
    <li><b>Placa de som:</b> DirectX Compatible Sound Card</li>
    <li><b>Bibliotecas:</b></li>
    <ul>
        <li><a href="https://www.pygame.org/wiki/GettingStarted"><code>pygame (biblioteca principal, utilizada para desenvolver o jogo)</code> </a></li>
        <li><a href="https://pillow.readthedocs.io/en/latest/installation/basic-installation.html"><code>PIL (do pacote Pillow)</code> </a></li>
    </ul>
    <font size="4"><b>Instalações</b></font>
    <br></br>
    <pre><code>python --version</code></pre>
    <pre><code>pip install pygame</code></pre>
    <pre><code>pip install pillow</code></pre>
    <br>
    <font size="4"><b>Ou</b></font>
    <br></br>
    <pre><code>pip install -r requirements.txt</code></pre>
</ul>

<hr></hr>

<br></br>

## 🎃 Como Jogar

<ol>
    <li>Pressione a tecla Espaço para fazer o corvo bater asas e voar.</li>
    <li>Evite colidir com os obstáculos assustadores no caminho.</li>
    <li>Quanto mais você voar, mais alta será sua pontuação, e terá a mudança de senário e personagem</li>
    <li>Cada vez que você bater em um obstáculo perderá um coração</li>
    <li>Tente superar seu recorde anterior e desafie seus amigos a fazerem o mesmo!</li>
    <br>
    <font size="4"><b>Controles</b></font>
    <br></br>
    <ul>
        <li><b>Espaço</b>: Faz o personagem pular.</li>
    </ul>
</ol>

<hr></hr>

<br></br>

## 🕆 Fluxo do jogo

<ol>
    <li><b>Tela Inicial:</b> O usuário pode optar por jogar ou sair. A música de fundo é tocada e o volume pode ser ajustado.</li>
    <li><b>Contagem Regressiva:</b> Antes do início do jogo, uma contagem de 3 segundos é exibida.</li>
    <li><b>Loop Principal:</b> O jogador deve controlar o personagem para evitar os obstaculos. A pontuação aumenta a cada obstaculo ultrapassado.</li>
    <li><b>Colisões:</b> Se o personagem colide, ele perde uma vida e entra em modo de invencibilidade temporária.</li>
    <li><b>Game Over:</b> Quando todas as vidas são perdidas, a tela de Game Over é exibida, e o jogador pode reiniciar o jogo.</li>
    
</ol>

<hr></hr>

<br></br>

## 👻 Estrutura do Projeto

<pre><code>CreppyThings/
│
/modulos
 ├── config.py
 ├── elementos.py
 └── utilidades.py
/sons
 ├── this-is-halloween-172354.mp3
 ├── StockTune-Creepy Crawly Capers_1729035356.mp3
 ├── smw_kick.wav
 ├── mixkit-player-jumping-in-a-video-game-2043.wav
 ├── mixkit-arcade-fast-game-over-233.wav
 └── mixkit-evil-dwarf-laugh-421.wav
/imgs
 ├── game_name.png
 ├── nickname.png
 ├── botão_play_.png
 ├── botão_exit_.png
 ├── botao_volume_positivo.png
 ├── botao_volume_negativo.png
 ├── aranha.png
 ├── caixao.png
 ├── base.jpg
 ├── background_cemiterio.png
 ├── vida0.png
 ├── vida1.png
 ├── vida2.png
 ├── vida3.png
 ├── gameover.png
 ├── pontuacao.png
 ├── recorde-img.png
 ├── botao_reiniciar.png
 └── botao_tela_inicial.png
/App.py

 ├── README.md                     # Documentação
 └── requirements.txt              # Bibliotecas utilizadas no projeto

• /modulos: Contém os arquivos Python que implementam a lógica principal do 
jogo.
• /sons: Contém os arquivos de áudio usados no jogo.
• /imgs: Contém as imagens e GIFs usados no jogo.
• main.py: O arquivo principal onde o jogo é executado.

</code></pre>

<hr></hr>

<br></br>

## 🔥 Alterações por grupo

<br>
<ol>
    <li><b>Grupo 1: Manutenção</b></li>
    <ul>
        <li>Correção dos bugs remanescentes: correção da velocidade; correção do audio (em determinados eventos do jogo, o som desaparece) e mudança do nome do jogo para "CreepyThings".</li>
    </ul>
    <br>
    <li><b>Grupo 2: Refatoração</b></li>
    <ul>
        <li>Refatoração do código, com o intuito de dividí-lo em módulos de acordo com as suas funções e criação de um arquivo executável para o jogo.</li>
    </ul>
    <br>
    <li><b>Grupo 3: CreepyChristmas</b></li>
    <ul>
        <li>Alteração do cenários e do sprite principal para uma temática natalina com atmosfera assustadora, Agora nesta fase, o sprite principal será um bodeMudança dos sons característicos do sprite principal.Ao atingir 200 pontos, haverá a mudança de cenário.</li>
    </ul>
    <br>
    <li><b>Grupo 4: CreepyEaster</b></li>
    <ul>
        <li> Alteração do cenários e do sprite principal para uma temática pascoal com atmosfera assustadora,agora nesta fase, o sprite principal será um coelho gigante, com manchas de sangue, olhos vermelhos, dentes pontiagudos e sem uma pata e mudança dos sons característicos do sprite principal.</li>
    </ul>
    <br>
    <li><b>Grupo 5: CreepyCarnival</b></li>
    <ul>
        <li>Alteração do cenários e do sprite principal para uma temática carnavalesca com atmosfera assustadora, agora nesta fase, o sprite principal será um boneco de Olinda e mudança dos sons característicos do sprite principal, ao atingir 200 pontos, haverá a mudança de cenário.</li>
    </ul>
    
    
</ol>

<hr></hr>

<br></br>

## 🕸️ Componentes do Jogo

<ul>
    <font size="4"><b>Personagens</b></font>
    <br></br>
    <ul>
        <li>Cada senário tem seu proprio personagem principal voando entre os obstaculos para se manter no jogo .</li>
        <li>Controlado pelo jogador e se move para frente automaticamente, com a gravidade puxando-o para baixo. Cada vez que o jogador pressiona a tecla Espaço, o personagem sobe.</li>
    </ul>
    <br></br>
    <font size="4"><b>Obstáculos de Temas do Jogo</b></font>
    <br></br>
    <ul>
        <li><b>Obstaculos:</b> Cada senário tem seus proprios obstaculos de acordo com o tema do senário, os obstaculos aparecem de forma similar aos canos do Flappy Bird, como obstáculos verticais que devem ser evitados.</li>   
    </ul>
    <br></br>
    <font size="4"><b>Cenários Sinistros</b></font>
    <br></br>
    <ul>
        <li>O fundo do jogo é composto por um céu escuro e lua cheia inicialmente, no decorrer do jogo o fundo do jogo é alterado de acordo com o tema.</li>
    </ul>
    <br></br>
    <font size="4"><b>Efeitos Sonoros</b></font>
    <br></br>
    <ul>
        <li>Sons arrepiantes, com cada mudança de senário o som taabém muda.</li>
        <li>Efeitos sonoros para colisão e pontos também estão incluídos.</li>
    </ul>
    <br></br>
    <font size="4"><b>Pontuação</b></font>
    <br></br>
    <ul>
        <li>A cada conjunto de obstáculos superado, a pontuação aumenta em 20 pontos.</li>
        <li>A pontuação é exibida na parte superior da tela.</li>
        <li>Cada vez que o jogador acumula 50 pontos, a velocidade do desafio aumenta.</li>
    </ul>
</ul>

<hr></hr>

<br></br>

## 👽 Funções e Módulos

<br></br>

<code>Classe Passaro</code>

<ul>
    <li>Funções para desenhar e controlar o comportamento do Corvo, como:</li>
    <ul>
        <li>Movimentação</li>
        <li>Pulo e gravidade</li>
    </ul>
</ul>
<hr></hr>

<code>Classe Cano</code>

<ul>
    <li>Funções para desenhar e controlar os obstáculos do jogo, como:</li>
    <ul>
        <li>Movimentação e altura dos caixões e aranhas</li>
        <li>Colisões com o corvo</li>
    </ul>
</ul>
<hr></hr>

<code>Classe Chao</code>

<ul>
    <li>Funções para desenhar o chão do jogo e gerar impressão de movimento.</li>
</ul>
<hr></hr>

<code>Função load_gif()</code>

<ul>
    <li>Carrega uma animação GIF para o corvo.</li>
</ul>
<hr></hr>

<code>Função tela_inicial()</code>

<ul>
    <li>Exibe a tela inicial do jogo.</li>
    <li>Adiciona botão de play e quit para o jogo.</li>
    <li>Mixer com uma barra para controlar o volume do jogo.</li>
</ul>
<hr></hr>

<code>Função contagem()</code>

<ul>
    <li>Função para exibir uma contagem regressiva antes do jogo começar.</li>
</ul>
<hr></hr>

<code>Função desenhar_tela()</code>

<ul>
    <li>Pede como parametro as instancias das classes principais para desenhar os elementos na tela, como:</li>
    <ul>
        <li>O corvo.</li>
        <li>Corações de vida.</li>
        <li>Chão do jogo.</li>
        <li>Pontos obtidos pelo jogador.</li>
    </ul>
</ul>
<hr></hr>

<code>Função exibir_game_over()</code>

<ul>
    <li>Mostra a tela de Game Over com os pontos obtidos pelo jogador ao decorrer da partida.</li>
</ul>
<hr></hr>

<code>Função main()</code>

<ul>
    <li>Contém o loop principal do jogo e é responsável por:</li>
    <ul>
        <li>Instanciar os objetos do game.</li>
        <li>Iniciar o jogo.</li>
        <li>Controlar a lógica de aparições e velocidade dos obstáculos.</li>
        <li>Controlar a lógica de movimento.</li>
        <li>Detectar colisões.</li>
        <li>Gerenciar a pontuação.</li>
        <li>Reeniciar o jogo após o fim.</li>
    </ul>
</ul>

<hr></hr>

<br></br>

## 👿 Possíveis melhorias

<ol>
    <li><b>Salvar Pontuação Máxima:</b> Implementar um sistema para salvar a pontuação mais alta do jogador.</li>
    <li><b>Variedade de Personagens:</b> Incluir diferentes personagens para o jogador escolher.</li>
    <li><b>Suporte a Multijogador:</b> Implementar um modo multiplayer, onde dois jogadores competem simultaneamente.</li>
    
</ol>

<hr></hr>

<br></br>

## 🔮 Adicionais

<br></br>

<font size="3"><b>Projeto desenvolvido pelo Professor Roberto de Pádua Carvalho Reis e aprimorado pela turma do 5º período de Engenharia de software 3. Curso de Sistemas de informações, turno matutino.</b></font>
