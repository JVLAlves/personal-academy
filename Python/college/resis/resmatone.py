import math


class ret:
    def __init__(self, b, h, axys: tuple):
        self.X, self.Y = axys
        self.area = b * h
        self.InertiaX = (b * (h ** 3)) / 12
        self.InertiaY = (h * (b ** 3)) / 12


def Centroid(*kwargs: ret):
    ##IN X AXYS##

    Sx = 0
    As = 0
    for k in kwargs:
        Sx += k.area * k.X
        As += k.area

    Xg = Sx / As

    ##IN Y AXYS##
    Sy = 0
    for k in kwargs:
        Sy += k.area * k.Y

    Yg = Sy / As

    return Xg, Yg

def MomentumofInertia(Centroid:tuple, *kwargs:ret):
    ##IN X AXYS##

    IXg = 0
    for k in kwargs:
        print(k.InertiaX, k.area, math.fabs(Centroid[1]- k.Y))
        IXg += k.InertiaX + (k.area * ((math.fabs(Centroid[1] - k.Y)) ** 2))

    ##IN Y AXYS##
    IYg = 0
    for k in kwargs:
        print(k.InertiaY, k.area, math.fabs(Centroid[0]- k.X))
        IYg += k.InertiaY + (k.area * ((math.fabs(Centroid[0] - k.X)) ** 2))

    return IXg, IYg

def suspended_beam_point(z:float, p:float, l:float, E:float=1000.0, I:float=27000.0):
    Theta = ((-p*(z**2))+(p*(l*2)))/(2*E*I)
    y = ((-p*(z**3))+(3*p*(l**2)*z)-(2*p*(l**3)))/(6*E*I)
    return y



if __name__ == "__main__":



