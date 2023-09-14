from rich import print
import collections

naipes = dict(espadas=3, ouros=2, paus=1, copas=0)


def ordenar_baralho(carta):
    valor_carta = Baralho.valores.index(carta.valor)
    return valor_carta * len(naipes) + naipes[carta.naipe]


Carta = collections.namedtuple('Carta', ['valor', 'naipe'])


class Baralho:
    valores = [str(n) for n in range(2, 11)] + list('JQKA')
    naipes = 'espadas ouros paus copas'.split()

    def __init__(self):
        self._cartas = [
            Carta(valor, naipe)
            for naipe in self.naipes
            for valor in self.valores
        ]

    def __len__(self):
        return len(self._cartas)

    def __getitem__(self, posição):
        return self._cartas[posição]

    def __contains__(self, item):
        print('agora contains')
        return item in self._cartas


deck = Baralho()
