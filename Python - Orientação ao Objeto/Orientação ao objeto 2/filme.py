from programa import Programa


class Filme(Programa):

    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'Nome: {self._nome} - Ano: {self._ano} - Duração: {self.duracao}  - Likes: {self._likes}'
