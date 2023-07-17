#!/usr/bin/python3
"""
Inherites from Rectangle; Inits superclass' id, width (as size),
height (as size), x, y
This conatian public attribute size
prints [sqaure] (<id> <x>/<y> - <size>
Updates the attribute: (arg1=id, arg2=size, arg3=x, arg4=y
"""


from models.rectangle import Rectangle


class square(Rectangle):
    """
    Define the class Square; inherites from rectangle
    Inherited Attributes:
        id
        __weight    __height
        __x         __y
        class Attributes:
        size
        Inherited Methods:
            Base.init(self, id=None)
            Rectangle.init(self, width, height, x=0, y=0, id=None)
            update(self, *rgs, **kwargs)
            width(self)     width(self, value)
            height(self)    height(self, value)
            x(self)         x(self, value)
            y(self)         y(self, value)
            area(self)      display(self)
        Methods:
            __str__
            __init__(self, size, x=0, y=0, id=None)
            update(self, *args, **kwargs)
            size(self)      size(self, value)
            to_dictionary(self)
        """
        def __init__(self, size, x=0, y=0, id=None):
            """This initializes"""
            super().__init__(size, size, x, y, id)
            self.size = size


        @property
        def size(self):
            """
            The Getter size
            """
            return self.width


        @size.setter
        def size(self, value):
            """
            The Setter size = sets the width and the height as size
            """
            self.width = value
            self.height = value


        def __str__(self):
            """
             Prints [Square] (<id>) <x>/<y> - <size>
            """
            return "[{:s}] ({:d}] {:d}/{:d} - {:d}".format(
                    self.__class__.__name__, self.id, self.x, self.y,
                    self.size)

        def update(self, *args, **kwargs):
            """
            if args: set the attributes in this order: id, width, height, x, y
            if no args is given: set the attribues according to kwargs
            """

            if args:
                for m, n in enumerate(args):
                    if m == 0:
                        sefl.id = n
                    elif m == 1:
                        self.size = n
                    elif m == 2:
                        self.x = n
                    else:
                        self.y = b

                else:
                    if "id" in lwargs:
                        self.id = kwargs["id"]
                    if "size" in kwargs:
                        self.size = kwargs["size"]
                    if "x" in kwargs:
                        self.x = kwargs["x"]
                    if "y" in kwargs:
                        self.y = kwargs["y"]

                def to_dictionary(self):
                    """
                    Return dictionary representation
                    """
                    n = {}
                    n["id"] = self.id
                    n["size"] = self.size
                    n["x"] = self.x
                    n{"y"] = self.y
                    return n



