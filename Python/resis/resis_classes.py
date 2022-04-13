import sympy


class load:
    def __init__(self, Distance: float, Value: float):
        self.loadDistance = Distance
        self.loadValue = Value


class continuous(load):

    def __init__(self, Ref: float, Range: float, Value: float):
        super().__init__((Range / 2) + Ref, (Value * Range))
        self.continuousLoad = Value
        self.loadRange = Range

    def Momentum(self, ref: float):
        if self.loadDistance < ref:
            return -1 * (self.loadDistance * self.loadValue)
        elif self.loadDistance > ref:
            return self.loadDistance * self.loadValue
        else:
            return 0

    def PointLoad(self):
        return load(self.loadDistance, self.loadValue)


class point(load):
    def __init__(self, Distance: float, Value: float):
        super().__init__(Distance, Value)

    def Momentum(self, ref: float):
        if self.loadDistance < ref:
            return -1 * (self.loadDistance * self.loadValue)
        elif self.loadDistance > ref:
            return self.loadDistance * self.loadValue
        else:
            return 0


class simple:
    def __init__(self, distance, V):
        self.vertical = V
        self.distance = distance

    def Momentum(self, ref:float):
        if self.distance < ref:
            if isinstance(self.vertical, type(sympy.symbols("CONTROL"))):
                return [-1 * (self.distance * self.vertical), self.vertical]
            return -1 * (self.distance * self.vertical)
        elif self.distance > ref:
            if isinstance(self.vertical, type(sympy.symbols("CONTROL"))):
                return [(self.distance * self.vertical), self.vertical]
            return self.distance * self.vertical
        else:
            return 0


class double:
    def __init__(self, distance, V, H):
        self.vertical = V
        self.horizontal = H
        self.distance = distance

    def Momentum(self, orientation: str, ref:float):
        if orientation.lower() == "vertical":
            if self.distance < ref:
                if isinstance(self.vertical, type(sympy.symbols("CONTROL"))):
                    return [-1 * (self.distance * self.vertical), self.vertical]
                return -1 * (self.distance * self.vertical)
            elif self.distance > ref:
                if isinstance(self.vertical, type(sympy.symbols("CONTROL"))):
                    return [(self.distance * self.vertical), self.vertical]
                return self.distance * self.vertical
            else:
                return 0
        elif orientation.lower() == "horizontal":
            if self.distance < ref:
                if isinstance(self.horizontal, type(sympy.symbols("CONTROL"))):
                    return [-1 * (self.distance * self.horizontal), self.horizontal]
                return -1 * (self.distance * self.horizontal)
            elif self.distance > ref:
                if isinstance(self.horizontal, type(sympy.symbols("CONTROL"))):
                    return [(self.distance * self.horizontal), self.horizontal]
                return self.distance * self.horizontal
            else:
                return 0
        else:
            return


class triple:
    def __init__(self, distance, V, H, M):
        self.vertical = V
        self.horizontal = H
        self.momentum = M
        self.distance = distance

    def Momentum(self, orientation: str, ref: float):
        if orientation.lower() == "vertical":
            if self.distance < ref:
                if isinstance(self.vertical, type(sympy.symbols("CONTROL"))):
                    return [-1 * (self.distance * self.vertical), self.vertical]
                return -1 * (self.distance * self.vertical)
            elif self.distance > ref:
                if isinstance(self.vertical, type(sympy.symbols("CONTROL"))):
                    return [(self.distance * self.vertical), self.vertical]
                return self.distance * self.vertical
            else:
                return 0
        elif orientation.lower() == "horizontal":
            if self.distance < ref:
                if isinstance(self.horizontal, type(sympy.symbols("CONTROL"))):
                    return [-1 * (self.distance * self.horizontal), self.horizontal]
                return -1 * (self.distance * self.horizontal)
            elif self.distance > ref:
                if isinstance(self.horizontal, type(sympy.symbols("CONTROL"))):
                    return [(self.distance * self.horizontal), self.horizontal]
                return self.distance * self.horizontal
            else:
                return 0
        else:
            return self.momentum
