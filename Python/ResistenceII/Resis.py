"""
c (suf.) - Calculate
s (suf.) - Sum
d (suf.) - Define (User enter)
"""
import itertools


class SectionSeg:
    newid = itertools.count()
    def __init__(self, base, height):
        self.id = next(SectionSeg.newid)
        self.base = base
        self.height = height
        self.area = base * height

    def dXgYg(self,Xg, Yg):
        self.Xg = Xg
        self.Yg = Yg

    def cDx(self, XG):
        self.Dx = self.Xg - XG
        print("Dx{} = {:.2f} cm".format(self.id, round(self.Dx, 2)))

    def cDy(self, YG):
        self.Dy = self.Yg - YG
        print("Dy{} = {:.2f} cm".format(self.id, round(self.Dy, 2)))

    def cIx(self, fInertia):
        self.Ix = fInertia(self.base, self.height)
        print("Ix{} = {:.2f} cm^4".format(self.id, round(self.Ix, 2)))

    def cIy(self, fInertia):
        self.Iy = fInertia(self.base, self.height)
        print("Iy{} = {:.2f} cm^4".format(self.id, round(self.Iy, 2)))

class Piece:
    def __init__(self, Segments):
        self.SegmentsNum = len(Segments)
        self.Segments = Segments
    ###########################################
    def cXG(self):
        sAXg = 0
        sA = 0
        for Seg in self.Segments:
            sAXg += (Seg.Xg * Seg.area)
            sA += Seg.area
        #######################################
        XG = sAXg/sA
        self.XG = XG
        print("XG = {:.2f} cm".format(round(self.XG, 2)))

    def cYG(self):
        sAYg = 0
        sA = 0
        for Seg in self.Segments:
            sAYg += (Seg.Yg * Seg.area)
            sA += Seg.area
        #######################################
        YG = sAYg / sA
        self.YG = YG
        print("YG = {:.2f} cm".format( round(self.YG, 2)))

    def cIX(self):
        sIX = 0
        for Seg in self.Segments:
            sIX += (Seg.Ix + (Seg.area *(Seg.Dy**2)))

        self.IX = sIX
        print("IX= {:.2f} cm^4".format( round(self.IX, 2)))

    def cIY(self):
        sIY = 0
        for Seg in self.Segments:
            sIY += (Seg.Iy + (Seg.area * (Seg.Dx ** 2)))

        self.IY = sIY
        print("IY = {:.2f} cm^4".format(round(self.IY, 2)))





