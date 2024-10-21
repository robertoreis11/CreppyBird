<font size="8"><b>CreepyBird - Halloween Edition 🪦</b></font>

<font size="5"><b>Visão geral</b></font>

<b>CreepyBird</b> é uma recriação do clássico Flappy Bird, mas com um toque assustador! Em vez de guiar um pássaro alegre através de canos, você controla um corvo sombrio voando através de um cemitério cheio de lápides e árvores mortas. O desafio permanece o mesmo: sobreviver o máximo possível sem colidir com os obstáculos. No entanto, agora o ambiente está repleto de sombras, sons arrepiantes e uma atmosfera sombria que vai te deixar no clima de Halloween!

Prepare-se para uma experiência divertida e aterrorizante, com gráficos inspirados no mundo do terror e sons que farão sua espinha gelar. Você consegue guiar o corvo até o amanhecer?

<hr></hr>

<br></br>
<font size="5"><b>🎮 Funcionalidades</b></font>

<ul>
    <li><b>Personagem Principal</b>: Um corvo sombrio, com asas batendo em um cenário assustador.</li>
    <li><b>Obstáculos de Halloween</b>: Passe por lápides aterrorizantes.</li>
    <li><b>Cenário Sinistro</b>: Um cemitério envolto em névoa, com um fundo escuro e lua cheia.</li>
    <li><b>Efeitos Sonoros de Terror</b>: Sons sinistros e risadas macabras para aumentar a imersão.</li>
    <li><b>Música Temática</b>: Uma trilha sonora sombria para complementar a atmosfera de Halloween.</li>
    <li><b>Sistema de Pontuação</b>: A cada obstáculo superado, sua pontuação aumenta.</li>
    <li><b>Dificuldades</b>: Quanto mior os pontos, mais veloz fica o desafio.</li>
</ul>

<hr></hr>

<br></br>
<font size="5"><b>🧛‍♂️ Requisitos</b></font>

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
</ul>

<hr></hr>

<br></br>
<font size="5"><b>🎃 Como Jogar</b></font>


<ol>
    <li>Pressione a tecla Espaço para fazer o corvo bater asas e voar.</li>
    <li>Evite colidir com os obstáculos assustadores no caminho.</li>
    <li>Quanto mais você voar, mais alta será sua pontuação.</li>
    <li>Cada vez que você bater em um obstáculo perderá um coração</li>
    <li>Tente superar seu recorde anterior e desafie seus amigos a fazerem o mesmo!</li>
    <br>
    <font size="4"><b>Controles</b></font>
    <br></br>
    <ul>
        <li><b>Espaço</b>: Faz o corvo bater as asas.</li>
    </ul>
</ol>

<hr></hr>

<br></br>
<font size="5"><b>👻 Estrutura do Projeto</b></font>


<pre><code>CreppyBird/
│
├── imgs/                           # Imagens do jogo
│   ├── background_cemiterio.png    # Imagem de fundo (Background) do Jogo.
│   ├── background_inicial.png      # Tela inicial que aparece no menu do jogo.
│   ├── caixao.png                  # Caixão (Obstáculo)
│   └── crow.gif                    # Corvo (Personagem)
│
├── sons/                           # Sons do jogo
│   ├── mixkit-evil.wav             # Risadas macabras
│   ├── StockTune-Creepy.mp3        # Som da tela inicial
│   ├── this-is-halloween.mp3       # Trilha sonora principal do jogo
│   └── mixkit-arcade-fast.wav      # Som da colisão
│
├── FlappyBird.py                   # Código do jogo e configurações
└── README.md                       # Documentação
</code></pre>

<hr></hr>

<br></br>
<font size="5"><b>🕸️ Componentes do Jogo</b></font>


<ul>
    <font size="4"><b>Corvo</b></font>
    <br></br>
    <ul>
        <li>O personagem principal é um corvo sombrio que precisa voar por entre obstáculos místicos de Halloween.</li>
        <li>Ele é controlado pelo jogador e se move para frente automaticamente, com a gravidade puxando-o para baixo. Cada vez que o jogador pressiona a tecla Espaço, o corvo bate asas e sobe.</li>
    </ul>
    <font size="4"><b>Obstáculos de Halloween</b></font>
    <br></br>
    <ul>
        <li><b>Caixões:</b> Aparecem de forma similar aos canos do Flappy Bird, como obstáculos verticais que devem ser evitados.</li>
        <li><b>Aranhas:</b> Surgem caindo do céu, evite-as para não perder seus corações de vida.</li>
    </ul>
    <font size="4"><b>Cenário Sinistro</b></font>
    <br></br>
    <ul>
        <li>O fundo do jogo é composto por um céu escuro e lua cheia.</li>
    </ul>
    <font size="4"><b>Efeitos Sonoros</b></font>
    <br></br>
    <ul>
        <li>Sons arrepiantes, como risadas macabras criam uma experiência imersiva.</li>
        <li>Efeitos sonoros para colisão e pontos também estão incluídos.</li>
    </ul>
    <font size="4"><b>Pontuação</b></font>
    <br></br>
    <ul>
        <li>A cada conjunto de obstáculos superado, a pontuação aumenta em 5 pontos.</li>
        <li>A pontuação é exibida na parte superior da tela.</li>
        <li>Cada vez que o jogador acumula 50 pontos, a velocidade do desafio aumenta.</li>
    </ul>
</ul>

<hr></hr>

<br></br>
<font size="5"><b>👽 Funções e Módulos</b></font>
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


<code>Função desenhar_tela()</code>
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
<font size="5"><b>🔮 Adicionais</b></font>
<br></br>

<font size="3"><b>Projeto desenvolvido pelo Professor Roberto de Pádua Carvalho Reis e aprimorado pela turma do 5º período de Engenharia de software 3 no curso de Sistemas de informações Matutino.</b></font>
