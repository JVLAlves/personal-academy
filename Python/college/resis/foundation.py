

# The first function must verify this cases
# Case 01: Neutral Line outside of the foundation (Load inside of the Central Core)
# Case 02: Neutral line inside of the foundation line (Load outside of the Central Core)
# Case 03 Neutral line in the Baricenter of the foundation (tipping)

# Given the cases it must calculate what it is asked to

class foundation:
    def __init__(self, Normal:float, Momentum:float, Size:tuple[float, float]):
        self.normal = Normal
        self.momentum = Momentum
        self.height = Size[0]
        self.width = Size[1]

    def excentricity(self):

        return self.momentum/self.normal

    def _area(self):
        return self.height * self.width

    def condition(self):
        e = self.excentricity()

        if e < (self.height/6):
            return 0
        elif (self.height/6) < e and e < (self.height/3):
            return 1
        elif e > (self.height/3):
            return -1
        else:
            raise TimeoutError

    def conditionInterpreter(self, condition:int):

        if condition == 0:

            print(
                f"(e = {self.excentricity()}) < (h/6 = {(self.height / 6)})\n"
                f"--> Inside of CC\n"
                f"--> NL Outside\n"
                f"--> Must find σ2\n\n"
                )

        elif condition == 1:
            print(
                f"(h/6 = {(self.height / 6)}) < (e = {self.excentricity()}) < (h/3 = {(self.height / 3)})\n"
                f"--> Outside of CC\n"
                f"--> NL Inside\n"
                f"--> Must find σc,max\n\n"
                )

        elif condition == -1:
            print(
                f"(e = {self.excentricity()}) > (h/3 = {(self.height / 3)})\n"
                f"--> NL in the Baricenter\n"
                f"--> ALERT OF TIPPING\n"
                f"--> Must recalculate the Height and find σc,max\n\n"
                )


def Foundation_calculus(f:foundation):

    condition = f.condition()
    f.conditionInterpreter(condition)


    if condition == 1:
        x = 3*((f.height/2)-f.excentricity())

        Sigma_c_max = (2*f.normal)/(f.width*x)
        print(f"σc,max = {Sigma_c_max * 100} Kgf/cm2\n\n")

    elif condition == 0:

        SigmaN = f.normal/f._area()
        SigmaM = (f.momentum * (f.height/2))/((f.width*(f.height**3))/12)

        Sigma02 = SigmaN + SigmaM

        print(f"σ2 = {Sigma02 * 100} Kgf/cm2\n\n")

    elif condition == -1:
        print(f"ALERT OF TIPPING! MUST RECALCULATE!\n")

        e = f.excentricity()
        nHeight = 3*e

        print(f"NEW HEIGHT: {nHeight} cm\n")

        x = 3 * ((nHeight / 2) - f.excentricity())

        Sigma_c_max = (2 * f.normal) / (f.width * x)
        print(f"σc,max = {Sigma_c_max * 100} Kgf/cm2\n\n")


if __name__ == '__main__':

    F1 = foundation(80, 2500, (200, 120))
    F2 = foundation(50, 2500, (200, 120))
    F3 = foundation(30, 2500, (200, 120))

    Fs = [F1, F2, F3]

    for num, F in enumerate(Fs):
        print(f"Foundation 0{num+1}")
        Foundation_calculus(F)