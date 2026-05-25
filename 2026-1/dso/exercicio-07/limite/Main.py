from controle.ControladorJogo import *
from modelo.Jogador import *
from modelo.Mesa import *
from modelo.Personagem import Tipo


controle = ControladorJogo()

jogador1 = Jogador("Lucas")
jogador2 = Jogador("Pedro")


p1 = controle.inclui_personagem_na_lista(
    50, 40, 30, 20, Tipo.fogo
)

p2 = controle.inclui_personagem_na_lista(
    10, 20, 30, 40, Tipo.agua
)


c1 = controle.inclui_carta_no_baralho(p1)
c2 = controle.inclui_carta_no_baralho(p2)


jogador1.inclui_carta_na_mao(c1)
jogador2.inclui_carta_na_mao(c2)


mesa = Mesa(
    jogador1,
    jogador2,
    jogador1.baixa_carta_da_mao(),
    jogador2.baixa_carta_da_mao()
)


vencedor = controle.jogada(mesa)

if vencedor is not None:
    print("Vencedor:", vencedor.nome)

else:
    print("Nenhum vencedor.")