from Resis import *

S1 = SectionSeg(2, 8)
S2 = SectionSeg(10, 2)
S3 = SectionSeg(2, 8)

S1.dXgYg(1, 4)
S2.dXgYg(5, 9)
S3.dXgYg(9,4)

Segments = [S1, S2, S3]

Piece = Piece(Segments)
Piece.cXG()
Piece.cYG()

for s in Segments:
    s.cDx(Piece.XG)
    s.cDy(Piece.YG)

def SquareX(base , height):
    result = round((base * (height**3))/12, 3)
    return result

def SquareY(base , height):
    result = round((height * (base**3))/12, 3)
    return result

for s in Segments:
    s.cIx(SquareX)
    s.cIy(SquareY)

Piece.cIX()
Piece.cIY()