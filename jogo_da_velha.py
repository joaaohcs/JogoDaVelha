import pygame
import sys
import random
from tabuleiro import Tabuleiro
from jogador import Jogador

# Inicialização do Pygame
pygame.init()

# Constantes
LARGURA = 300
ALTURA = 300
LINHAS = 3
COLUNAS = 3
TAMANHO_CELULA = LARGURA // COLUNAS

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
VERMELHO_CLARO = (255, 102, 102)
CINZA = (169, 169, 169)

# Tela
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo da Velha")

class JogoDaVelha:
    def __init__(self):
        self.tabuleiro = Tabuleiro()
        self.jogadores = [Jogador("Jogador 1", "X"), Jogador("Bot", "O")]
        self.turno = 0
        self.jogando = True
        self.resultado = None  # Variável para armazenar o resultado
        self.fim_de_jogo = False  # Controla o menu de fim de jogo

    def alternar_turno(self):
        self.turno = (self.turno + 1) % 2

    def desenhar(self):
        tela.fill(BRANCO)
        self.tabuleiro.desenhar(tela)

        for i in range(LINHAS):
            for j in range(COLUNAS):
                if self.tabuleiro.tabuleiro[i][j] != '':
                    font = pygame.font.Font(None, 74)
                    texto = font.render(self.tabuleiro.tabuleiro[i][j], True, VERMELHO if self.tabuleiro.tabuleiro[i][j] == 'X' else AZUL)
                    tela.blit(texto, (j * TAMANHO_CELULA + 30, i * TAMANHO_CELULA + 30))

        if self.resultado:
            self.exibir_menu_fim()

    def exibir_menu_fim(self):
        tela.fill(PRETO)  # Tela de fundo preta
        font = pygame.font.Font(None, 36)

        # Exibir mensagem de vitória, derrota ou empate
        if self.resultado == "vitoria":
            texto = font.render("Você venceu!", True, VERDE)
        elif self.resultado == "derrota":
            texto = font.render("Você perdeu!", True, VERMELHO_CLARO)
        else:
            texto = font.render("DEU VELHA!", True, BRANCO)

        tela.blit(texto, (LARGURA // 2 - texto.get_width() // 2, ALTURA // 2 - 50))

        # Desenhando os botões com um design mais bonito
        self.desenhar_botao("Jogar novamente", LARGURA // 2 - 120, ALTURA // 2 + 30, 240, 50)
        self.desenhar_botao("Sair", LARGURA // 2 - 40, ALTURA // 2 + 90, 80, 50)

    def desenhar_botao(self, texto, x, y, largura, altura):
        # Cor do botão e borda
        cor_botao = CINZA
        cor_botao_hover = (150, 150, 150)
        cor_borda = PRETO

        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Detectando se o mouse está sobre o botão
        if x < mouse_x < x + largura and y < mouse_y < y + altura:
            pygame.draw.rect(tela, cor_botao_hover, (x, y, largura, altura))
        else:
            pygame.draw.rect(tela, cor_botao, (x, y, largura, altura))

        pygame.draw.rect(tela, cor_borda, (x, y, largura, altura), 3)

        # Texto centralizado no botão
        font = pygame.font.Font(None, 36)
        texto_renderizado = font.render(texto, True, PRETO)
        tela.blit(texto_renderizado, (x + (largura - texto_renderizado.get_width()) // 2, y + (altura - texto_renderizado.get_height()) // 2))

    def bot_jogar(self):
        # O bot escolhe a melhor jogada usando Minimax
        melhor_jogada = self.minimax(self.tabuleiro, True)
        linha, coluna = melhor_jogada
        self.tabuleiro.jogar(linha, coluna, self.jogadores[1].simbolo)

    def minimax(self, tabuleiro, maximizando):
        # Algoritmo Minimax para o bot
        melhor_pontuacao = -float('inf') if maximizando else float('inf')
        melhor_jogada = None

        jogadas_possiveis = [(i, j) for i in range(LINHAS) for j in range(COLUNAS) if tabuleiro.tabuleiro[i][j] == '']
        for jogada in jogadas_possiveis:
            i, j = jogada
            tabuleiro.tabuleiro[i][j] = self.jogadores[1].simbolo if maximizando else self.jogadores[0].simbolo
            pontuacao = self.avaliar(tabuleiro, maximizando)
            tabuleiro.tabuleiro[i][j] = ''  # Reverter a jogada

            if maximizando:
                if pontuacao > melhor_pontuacao:
                    melhor_pontuacao = pontuacao
                    melhor_jogada = jogada
            else:
                if pontuacao < melhor_pontuacao:
                    melhor_pontuacao = pontuacao
                    melhor_jogada = jogada

        return melhor_jogada

    def avaliar(self, tabuleiro, maximizando):
        # Avalia o tabuleiro com base no estado de vitória ou derrota
        if tabuleiro.verificar_vitoria():
            return 1 if maximizando else -1
        elif tabuleiro.is_cheio():
            return 0
        return 0

    def jogar(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if self.fim_de_jogo:
                    # Verificar cliques no menu de fim de jogo
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if pygame.mouse.get_pressed()[0]:
                        # Botão "Jogar novamente"
                        if LARGURA // 2 - 120 < mouse_x < LARGURA // 2 + 120 and ALTURA // 2 + 30 < mouse_y < ALTURA // 2 + 80:
                            self.reiniciar()
                        # Botão "Sair"
                        elif LARGURA // 2 - 40 < mouse_x < LARGURA // 2 + 40 and ALTURA // 2 + 90 < mouse_y < ALTURA // 2 + 140:
                            pygame.quit()
                            sys.exit()
                elif not self.fim_de_jogo:
                    if event.type == pygame.MOUSEBUTTONDOWN and self.resultado is None:
                        if self.turno == 0:  # Somente o jogador pode jogar
                            x, y = event.pos
                            linha = y // TAMANHO_CELULA
                            coluna = x // TAMANHO_CELULA

                            if self.tabuleiro.jogar(linha, coluna, self.jogadores[self.turno].simbolo):
                                if self.tabuleiro.verificar_vitoria():
                                    self.resultado = "vitoria"
                                    self.fim_de_jogo = True
                                elif self.tabuleiro.is_cheio():
                                    self.resultado = "empate"
                                    self.fim_de_jogo = True
                                else:
                                    self.alternar_turno()

                    if self.turno == 1 and self.resultado is None:  # Bot joga se for a vez dele
                        self.bot_jogar()
                        if self.tabuleiro.verificar_vitoria():
                            self.resultado = "derrota"
                            self.fim_de_jogo = True
                        elif self.tabuleiro.is_cheio():
                            self.resultado = "empate"
                            self.fim_de_jogo = True
                        else:
                            self.alternar_turno()

            self.desenhar()
            pygame.display.update()

    def reiniciar(self):
        self.tabuleiro = Tabuleiro()
        self.turno = 0
        self.resultado = None
        self.fim_de_jogo = False


if __name__ == "__main__":
    jogo = JogoDaVelha()
    jogo.jogar()
