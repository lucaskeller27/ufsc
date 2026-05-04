from .mamifero import Mamifero

class Gato(Mamifero):
    def __init__(self):
        super().__init__(volume_som=2, tamanho_passo=2)
    
    def miar(self):
        return self.produzir_som()
    
    def produzir_som(self):
        return super().produzir_som() + " SOM: MIAU"
    
    def mover(self):
        return super().mover()