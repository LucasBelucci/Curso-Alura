from filme import Filme
from serie import Serie
from programa import Programa
from playlist import Playlist

n = 0
m = 0

Filme1 = Filme('Vingadores1', 2020, 160)
Serie1 = Serie('Breaking Bad1', 2018, 5)

Filme2 = Filme('Vingadores2', 2022, 164)
Serie2 = Serie('Breaking Bad2', 2012, 6)

Filme3 = Filme('Vingadores3', 2023, 166)
Serie3 = Serie('Breaking Bad3', 2033, 7)

Filme4 = Filme('Vingadores4', 2034, 165)
Serie4 = Serie('Breaking Bad4', 2014, 8)

Filme5 = Filme('Demolidor', 2034, 165)


Filme1.dar_likes()
Serie1.dar_likes()
Filme1.dar_likes()
Serie1.dar_likes()

Filme2.dar_likes()
Serie2.dar_likes()
Filme2.dar_likes()
Serie2.dar_likes()
Filme2.dar_likes()
Serie2.dar_likes()

Filme3.dar_likes()
Serie3.dar_likes()
Filme3.dar_likes()
Serie3.dar_likes()
Filme3.dar_likes()
Serie3.dar_likes()
Filme3.dar_likes()
Serie3.dar_likes()

Filme4.dar_likes()
Serie4.dar_likes()

'''
print(f'{Filme1.nome}, {Filme1.ano}, {Filme1.duracao}, {Filme1.likes}')
print(f'{Serie1.nome}, {Serie1.ano}, {Serie1.temporada}, {Serie1.likes}')



print('--------------------------------------------------------------')
print(f'{Filme1.nome}, {Filme1.ano}, {Filme1.duracao}, {Filme1.likes}')
print(f'{Serie1.nome}, {Serie1.ano}, {Serie1.temporada}, {Serie1.likes}')
'''

filmes_e_series = [Filme1, Serie1, Filme2,
                   Serie2, Filme3, Serie3, Filme4, Serie4]

playlist_fim_de_semana = Playlist('Fim de semana', filmes_e_series)

print(f'Tamanho da playlist: {len(playlist_fim_de_semana)}')
print('---------------------------------------------------------------')
for programa in playlist_fim_de_semana:
    print(programa)

print(Filme5 in playlist_fim_de_semana)
