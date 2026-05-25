from abstract.AbstractControladorJogo import *

from modelo.Personagem import *
from modelo.Carta import *
from modelo.Jogador import *
from modelo.Mesa import *


class ControladorJogo(AbstractControladorJogo):
    def __init__(self):
        self.__baralho = []
        self.__personagens = []

    @property
    def baralho(self) -> list:
        return self.__baralho

    @property
    def personagens(self) -> list:
        return self.__personagens

    def inclui_personagem_na_lista(
        self,
        energia: int,
        habilidade: int,
        velocidade: int,
        resistencia: int,
        tipo: Tipo
    ) -> Personagem:
        personagem = Personagem(
            energia,
            habilidade,
            velocidade,
            resistencia,
            tipo
        )

        self.__personagens.append(personagem)

        return personagem

    def inclui_carta_no_baralho(
        self,
        personagem: Personagem
    ) -> Carta:
        carta = Carta(personagem)

        self.__baralho.append(carta)

        return carta

    def jogada(self, mesa: Mesa) -> Jogador:
        valor1 = mesa.carta_jogador1.valor_total_carta()
        valor2 = mesa.carta_jogador2.valor_total_carta()

        if valor1 > valor2:
            mesa.jogador1.inclui_carta_na_mao(
                mesa.carta_jogador1
            )

            mesa.jogador1.inclui_carta_na_mao(
                mesa.carta_jogador2
            )

        elif valor2 > valor1:
            mesa.jogador2.inclui_carta_na_mao(
                mesa.carta_jogador1
            )

            mesa.jogador2.inclui_carta_na_mao(
                mesa.carta_jogador2
            )

        else:
            mesa.jogador1.inclui_carta_na_mao(
                mesa.carta_jogador1
            )

            mesa.jogador2.inclui_carta_na_mao(
                mesa.carta_jogador2
            )

        if len(mesa.jogador1.mao) == 0:
            return mesa.jogador2

        if len(mesa.jogador2.mao) == 0:
            return mesa.jogador1

        return None
