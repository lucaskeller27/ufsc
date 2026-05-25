from abstract.AbstractCarta import *
from modelo.Personagem import *


class Carta(AbstractCarta):
    def __init__(self, personagem: Personagem):
        self.__personagem = personagem

    def valor_total_carta(self) -> int:
        return (
            self.__personagem.energia
            + self.__personagem.habilidade
            + self.__personagem.velocidade
            + self.__personagem.resistencia
        )

    @property
    def personagem(self) -> Personagem:
        return self.__personagem
