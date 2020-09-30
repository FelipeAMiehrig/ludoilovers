import numpy as np
__all__ = ['Casa']
class Casa:

    # parte do tabuleiro recursiva
    coords_rec = [(i, i) for i in np.arange(0, 52)]
    # casas base
    coords_base = [(i * 100, i * 100) for i in np.arange(1, 17)]

    def __init__(self, x, y, safe):
        self.x = x
        self.y = y
        self.safe = safe

    def __repr__(self):
        return "Casa({}, {}, {})".format(self.x, self.y, self.safe)



