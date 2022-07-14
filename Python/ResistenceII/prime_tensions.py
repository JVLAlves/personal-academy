import math

class prime_tensions:
    def __init__(self, ONE_SET:tuple[float, float], TWO_SET:tuple[float, float]):

        if not (ONE_SET[0] > TWO_SET[0]):
            raise Exception("SigmaDefinitionError: Sigma One must be bigger than Sigma Two.")
        else:
            pass

        self.SIGMA_ONE, self.ALPHA_ONE = ONE_SET
        self.SIGMA_TWO, self.ALPHA_TWO = TWO_SET

    def show(self):
        print(f"SIGMA1: {self.SIGMA_ONE} MPa --- ALPHA1: {self.ALPHA_ONE}\nSIGMA2: {self.SIGMA_TWO} MPa --- ALPHA2: {self.ALPHA_TWO}")

class little_tensions:
    def __init__(self, SIGMAx:float, SIGMAy:float, TAU:float):
        self.SIGMAx = SIGMAx
        self.SIGMAy = SIGMAy
        self.TAU = TAU

    @classmethod
    def CreateByInput(cls):
        SIGMAx = float(input("SIGMA in X axis: "))
        SIGMAy = float(input("SIGMA in y axis: "))
        TAU = float(input("TAU: "))

        return cls(SIGMAx, SIGMAy, TAU)


class alpha_angles:
    def __init__(self, TWOALPHAs:tuple[float, float], ALPHAs:tuple[float, float]):
        self. TWOALPHAs = TWOALPHAs
        self.ALPHAs = ALPHAs

# TG(2ALPHA) = - 2 * TAU/ SIGMAx - SIGMAy
# SIGMA_ = SIGMAx * COS^2(ALPHA_) + SIGMAy * SEN^2(ALPHA_)- TAU * SEN(TWOALPHA_)

def TAN_TWOALPHA(tensions:little_tensions):

    #NORMAL TENSION IN X AXIS
    SIGMAx = tensions.SIGMAx

    # NORMAL TENSION IN Y AXIS
    SIGMAy = tensions.SIGMAy

    # SHEERING TENSION
    TAU = tensions.TAU

    try:
        TAN = (-2*TAU)/(SIGMAx - SIGMAy)
    except ZeroDivisionError:
        return math.inf
    else:
        if TAN == -0:
            TAN = 0 * -1
        return TAN

def ALPHAS(TAN:float):

    TWOALPHA_ = math.degrees(math.atan(TAN))

    if TWOALPHA_ < 0:
        TWOALPHA_ += 180

    TWOALPHA__ = TWOALPHA_ + 180

    TWOALPHAs = (TWOALPHA_, TWOALPHA__)


    ALPHA_ = TWOALPHA_ / 2

    ALPHA__ = TWOALPHA__ / 2

    ALPHAs = (ALPHA_, ALPHA__)

    return alpha_angles(TWOALPHAs, ALPHAs)

def SIGMA(tensions:little_tensions, alphas:alpha_angles):
    #TENSIONS
    # NORMAL TENSION IN X AXIS

    SIGMAx = tensions.SIGMAx

    # NORMAL TENSION IN Y AXIS
    SIGMAy = tensions.SIGMAy

    # SHEERING TENSION
    TAU = tensions.TAU


    #ANGLES
    TWOALPHA_, TWOALPHA__ = alphas.TWOALPHAs

    ALPHA_, ALPHA__ = alphas.ALPHAs

    SIGMA_ = (SIGMAx * (math.cos(math.radians(ALPHA_))  if ALPHA_ != 90 else 0) **2) + (SIGMAy * math.sin(math.radians(ALPHA_))**2) - (TAU * math.sin(math.radians(TWOALPHA_)))

    SIGMA__ = (SIGMAx * (math.cos(math.radians(ALPHA__)) if ALPHA__ != 90 else 0)**2) + (SIGMAy * math.sin(math.radians(ALPHA__))**2) - (TAU*math.sin(math.radians(TWOALPHA__)))

    SIGMAS = {SIGMA_:ALPHA_, SIGMA__:ALPHA__}

    SIGMAONE = max(SIGMA_, SIGMA__)
    SIGMATWO = min(SIGMA_,SIGMA__)


    ONE_SET = (SIGMAONE, SIGMAS[SIGMAONE])
    TWO_SET = (SIGMATWO, SIGMAS[SIGMATWO])

    return prime_tensions(ONE_SET, TWO_SET)

if __name__ == "__main__":
    tensions = little_tensions(0, 0, 1.6)
    TAN = TAN_TWOALPHA(tensions)
    print(TAN)
    angles = ALPHAS(TAN)
    print(angles.TWOALPHAs, angles.ALPHAs)
    PRIME = SIGMA(tensions, angles)
    PRIME.show()







