
import dataclasses

@dataclasses.dataclass
class Corso:
    codins: str
    crediti: int
    nome: str
    pd: int

    # @property
    # def codins(self):
    #     return self.codins
    #
    # @codins.setter
    # def codins(self, new_codins):
    #     self.codins = new_codins
    #
    # @property
    # def crediti(self):
    #     return self.crediti
    #
    # @crediti.setter
    # def crediti(self, crediti):
    #     self.crediti = crediti
    #
    # @property
    # def nome(self):
    #     return self.nome
    #
    # @nome.setter
    # def nome(self, nome):
    #     self.nome = nome
    #
    # @property
    # def pd(self):
    #     return self.pd
    #
    # @pd.setter
    # def pd(self, pd):
    #     self.pd = pd

    def __eq__(self, other):
        pass

    def __hash__(self):
        pass

    def __str__(self):
        return self.nome