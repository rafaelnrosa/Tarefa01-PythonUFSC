# Connect Four

Jogo para dois jogadores locais, desenvolvido em Python com interface grafica
Tkinter. Os jogadores alternam fichas no tabuleiro de 7 colunas por 6 linhas;
vence quem alinhar quatro fichas na horizontal, vertical ou diagonal.

## Requisitos

- Python 3 instalado
- Tkinter (incluido nas instalacoes padrao do Python para Windows)

## Como executar

Na pasta do projeto, execute:

```powershell
python main.py
```

Clique no numero da coluna para soltar uma ficha. O jogo informa o turno, a
vitoria ou o empate. Use **Reiniciar Jogo** para iniciar uma nova partida.

## Testes

```powershell
python -m unittest discover -s tests -v
```
