from entidade import Cachorro, Gato, Canarinho

class AnimalLimite:
    def __init__(self):
        self._cachorro = None
        self._gato = None
        self._canarinho = None
    
    def criar_cachorro(self):
        self._cachorro = Cachorro()
        return self._cachorro
    
    def criar_gato(self):
        self._gato = Gato()
        return self._gato
    
    def criar_canarinho(self, tamanho_passo, altura_voo):
        self._canarinho = Canarinho(tamanho_passo, altura_voo)
        return self._canarinho
    
    def mover_animal(self, animal):
        return animal.mover()
    
    def produzir_som_animal(self, animal):
        return animal.produzir_som()
    
    def cachorro_latir(self):
        if self._cachorro:
            return self._cachorro.latir()
        return None
    
    def gato_miar(self):
        if self._gato:
            return self._gato.miar()
        return None
    
    def canarinho_cantar(self):
        if self._canarinho:
            return self._canarinho.cantar()
        return None
    
    def get_cachorro(self):
        return self._cachorro
    
    def get_gato(self):
        return self._gato
    
    def get_canarinho(self):
        return self._canarinho