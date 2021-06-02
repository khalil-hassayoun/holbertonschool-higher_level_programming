#!/usr/bin/python3
"square class inherits from Rectangle"
from models.rectangle import Rectangle


class Square(Rectangle):
    "Square class"
    def __init__(self, size, x=0, y=0, id=None):
        "Initiation of Square class"
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        "Size getter"
        return super().width

    @size.setter
    def size(self, value):
        "size setter"
        super().__init__(value, value, self.x, self.y, self.id)

    def update(self, *args, **kwargs):
        "Update the Square values"
        if args is None or len(args) == 0:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                v = kwargs['size']
                super().__init__(v, v, self.x, self.y, self.id)
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']
        else:
            if len(args) < 1:
                return
            self.id = args[0]
            if len(args) < 2:
                return
            super().__init__(args[1], args[1], self.x, self.y, self.id)
            if len(args) < 3:
                return
            self.x = args[2]
            if len(args) < 4:
                return
            self.y = args[3]

    def to_dictionary(self):
        "Square information to dict"
        d = {}
        d.setdefault('id', self.id)
        d.setdefault('size', super().width)
        d.setdefault('x', self.x)
        d.setdefault('y', self.y)
        return d
