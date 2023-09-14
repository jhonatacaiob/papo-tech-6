from rich import print
import collections

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


deck = Baralho()
