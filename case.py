import collections


OrderLine = collections.namedtuple("OrderLine", "code cases")



def rotate (case):
    case.sizex, case.sizey = case.sizey, case.sizex
    

class Case (object):

    def __init__ (self, x, y, sizex, sizey, weight, height):
        self.x = x
        self.y = y
        self.sizex = sizex
        self.sizey = sizey
        self.weight = weight
        self.height = height

        self.frozen_x = None
        self.frozen_y = None
        self.frozen_sizex = None
        self.frozen_sizey = None

    def __hash__(self):
        return hash(str(self))

    def __repr__(self):
        return f"Case(x={self.x}, y={self.y}, sizex={self.sizex}, sizey={self.sizey}, height={self.height}, weight={self.weight})"

    @property
    def top (self):
        return self.y + self.sizey

    @property
    def right (self):
        return self.x + self.sizex

    @property
    def left (self):
        return self.x

    @property
    def down (self):
        return self.y

    def rotate (self):
        self.sizex, self.sizey = self.sizey, self.sizex
