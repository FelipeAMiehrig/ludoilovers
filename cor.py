__all__ = ['Cor']


class Cor:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def __eq__(self, cor):
        if self.red == cor.red and self.green == cor.green and self.blue == cor.blue:
            return True
        else:
            return False

    def __repr__(self):
        return f'R: {self.red} G: {self.green} B: {self.blue}'