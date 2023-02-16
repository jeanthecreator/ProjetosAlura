class Programa:

    def __init__(self, nome, ano):
        
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    def dar_likes(self):
        self._likes += 1
      

    @property
    def likes(self):
        return self._likes
    
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def dar_nome(self, novo_nome):
        self._nome = novo_nome
    
    def __str__(self):
        return "{} {} Likes: {}".format(self.nome, self.ano, self.likes)

class Filme(Programa):

    def __init__(self, nome, ano, duracao):
        
        super().__init__(nome, ano)
        self.duracao = duracao
    
    def __str__(self):
        return "{} {} {} Likes: {}".format(self.nome, self.ano, self.duracao, self.likes)
        

class Serie(Programa):

    def __init__(self, nome, ano, temporada):
        
        super().__init__(nome, ano)
        self.temporada = temporada
    
    def __str__(self):
        return "{} {} {} Likes: {}".format(self.nome, self.ano, self.temporada, self.likes)

class Playlist:
    def __init__(self, nome, programas):
        self._nome = nome
        self._programas = programas
    
    def __getitem__(self, item):
        return self._programas[item]

    @property    
    def listagem(self):
        return self._programas 
    
    def __len__(self):
        return len(self._programas)


vingadores = Filme("vigadores - guerra infinita", 2008, 160)
bdo = Filme("a bulsula de ouro", 2004, 120)
caprica = Serie("caprica - historia", 2004, 6)
tbbt = Serie("the big bang theory", 2002, 9)
vingadores.dar_likes()
vingadores.dar_likes()
bdo.dar_likes()
bdo.dar_likes()
tbbt.dar_likes()
caprica.dar_likes()
caprica.dar_likes()
caprica.dar_likes()

filmes_e_series = [vingadores, caprica, bdo, tbbt]

minha_playlist= Playlist("FDS", filmes_e_series)

print("Tamanho da sua Playlist: {}".format(len(minha_playlist)))

for programa in minha_playlist:
    print(programa)

