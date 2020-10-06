"""
    Neste arquivo, Classes e funções.
"""

# adicionar livro: nome do livro, autor, pagina, ano de leitura, se estou sendo, se já foi lido
class Livro():
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def add_livro(self):
        informações = []

        i = 0
        while i < 3:
            pass