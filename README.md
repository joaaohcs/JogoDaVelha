# Jogo da Velha com Python 

Este é um projeto de um **Jogo da Velha** desenvolvido em Python, aplicando os principais conceitos de **Programação Orientada a Objetos (POO)** e **desenvolvimento de interfaces gráficas** com a biblioteca **Pygame**. Além disso, utiliza a serialização de objetos e boas práticas de engenharia de software para modelar o problema.

---

##  Objetivo

Criar uma aplicação funcional do jogo da velha que:  
1. Aplique os conceitos de:
   - **Herança**
   - **Polimorfismo**
   - **Encapsulamento Total**
2. Forneça uma interface gráfica amigável usando **Pygame**.

---

##  Funcionalidades
- Modo de jogo contra o computador (com um bot inteligente baseado no algoritmo **Minimax**).
- Verificação de vitória ou empate em tempo real.
- Interface gráfica interativa com design visual agradável.
- Opções no final do jogo: **Jogar novamente** ou **Sair**.
- Utilização de **POO** para estruturar o código de forma modular e escalável.

---



##  Tecnologias Utilizadas

- **Python 3.x**
- **Pygame**  
  Biblioteca para desenvolvimento de jogos e interfaces gráficas.
- **Serialização**  
  Implementada para persistência de dados e manipulação do estado do jogo.

---

##  Estrutura do Código

O projeto está dividido em módulos para facilitar a manutenção:
- `jogador.py`  
  Define a classe `Jogador`.
- `tabuleiro.py`  
  Define a classe `Tabuleiro`, responsável por gerenciar o estado do jogo.
- `main.py`  
  Contém a lógica principal e a classe `JogoDaVelha`.

---

##  Como Executar

### Pré-requisitos
Certifique-se de ter o **Python** instalado em sua máquina. Você pode instalá-lo [aqui](https://www.python.org/downloads/).  

### Passos
1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/jogo-da-velha.git
2. Navegue até o diretório do projeto:
   ```bash
   cd jogo-da-velha
3. Instale as dependências necessárias:
   ```bash
   pip install pygame
4. Execute o jogo:
   ```bash
   python main.py
   

