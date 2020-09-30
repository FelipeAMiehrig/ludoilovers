import numpy as np
__all__ = ['Casa']

N_CASAS_REC = 52
N_CASAS_BASE = 16
class Casa:

    # parte do tabuleiro recursiva
    coords_rec = [(i, i) for i in np.arange(0, N_CASAS_REC)]
    # casas base
    coords_base = [(i * 100, i * 100) for i in np.arange(0, N_CASAS_BASE)]

    def __init__(self, x, y, safe):
        self.x = x
        self.y = y
        self.safe = safe

    def __repr__(self):
        return "Casa({}, {}, {})".format(self.x, self.y, self.safe)



