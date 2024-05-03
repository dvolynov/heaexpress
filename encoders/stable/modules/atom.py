class Coords:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    def __call__(self):
        return (self.x, self.y, self.z)


class Atom:
    def __init__(self, _type, coords):
        self.type    = _type
        self.coords  = Coords(*coords)