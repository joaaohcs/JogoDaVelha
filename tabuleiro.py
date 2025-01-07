import pygame

# Constantes do jogo
LINHAS = 3
COLUNAS = 3
TAMANHO_CELULA = 100
LARGURA = COLUNAS * TAMANHO_CELULA
ALTURA = LINHAS * TAMANHO_CELULA

class Tabuleiro:
    def __init__(self):
        self.tabuleiro = [['' for _ in range(COLUNAS)] for _ in range(LINHAS)]

    def desenhar(self, tela):
        for linha in range(1, LINHAS):
            pygame.draw.line(tela, (0, 0, 0), (0, linha * TAMANHO_CELULA), (LARGURA, linha * TAMANHO_CELULA), 2)
            pygame.draw.line(tela, (0, 0, 0), (linha * TAMANHO_CELULA, 0), (linha * TAMANHO_CELULA, ALTURA), 2)

    def verificar_vitoria(self):
        for i in range(LINHAS):
            if self.tabuleiro[i][0] == self.tabuleiro[i][1] == self.tabuleiro[i][2] and self.tabuleiro[i][0] != '':
                return True
            if self.tabuleiro[0][i] == self.tabuleiro[1][i] == self.tabuleiro[2][i] and self.tabuleiro[0][i] != '':
                return True
        if self.tabuleiro[0][0] == self.tabuleiro[1][1] == self.tabuleiro[2][2] and self.tabuleiro[0][0] != '':
            return True
        if self.tabuleiro[0][2] == self.tabuleiro[1][1] == self.tabuleiro[2][0] and self.tabuleiro[0][2] != '':
            return True
        return False

    def is_cheio(self):
        for linha in self.tabuleiro:
            if '' in linha:
                return False
        return True

    def jogar(self, linha, coluna, jogador):
        if self.tabuleiro[linha][coluna] == '':
            self.tabuleiro[linha][coluna] = jogador
            return True
        return False
