import sympy
import sympy as sp
import sympy.physics.units as units
from sympy.physics.units import convert_to, Unit
from sympy.physics.units.systems import SI
from sympy.physics.units.quantities import Quantity
from sympy.physics.units.systems.si import dimsys_SI
from calculus.generators import RandNumGenerator

# Kilonewton definition - kN
kN = Quantity("kilonewton", abbrev="kN")
SI.set_quantity_dimension(kN, units.force)
SI.set_quantity_scale_factor(kN, units.kilo * units.newton)


# Megapascal definition - MPa
MPa = Quantity("megapascal", abbrev="MPa")
SI.set_quantity_dimension(MPa, units.pressure)
SI.set_quantity_scale_factor(MPa, units.mega * units.pascal)

"""

"""

class load:
    def __init__(self, value: float, unit:Quantity):
        self.value = value
        self.unit = unit
        self.quantity = value * unit

class point:
    def __init__(self, value, unit:Quantity = kN):
        self.id = id(id)
        self.value = value
        self.unit = unit
        self.quantity = value * unit


    def convert(self, To:Quantity):
        convertion = convert_to(self.quantity, To)

        if convertion != self.quantity:

            self.quantity = convertion.n()
            self.value = convertion/To
            self.unit = To
        else:
            raise Exception("Units are not from the same dimension.")

class continuous(point):
    def __init__(self, value, unit:Quantity=kN/units.meters):
        super().__init__(value, unit)
        self.id = id(id)

    def Point(self, range:tuple[float, Quantity]):
        length, unit = range
        pLoad = self.value * length
        pUnit = self.unit * unit
        return point(pLoad, pUnit)



class tension(load):

    def __init__(self, value: float, unit: Quantity):
        super().__init__(value, unit)
        self.id = id(id)


    @classmethod
    def createFromLoad(cls, load:point, area:tuple[float, Quantity]):
        aValue, aUnit = area
        value = load.value/aValue
        unit = load.unit/aUnit
        return cls(value, unit)

class structure:
    def __init__(self, loads:list, supports:int, length:tuple[float, Quantity]):

        #Attribute Varifing -- Loads
        if loads is None or len(loads) == 0:
            raise AttributeError
        else:
            for l in loads:
                if not isinstance(l, point)and not isinstance(l, continuous):
                    raise AttributeError

        self.loads = loads


        # Attribute Varifing -- supports
        if supports <= 1 or supports > 2:
            raise AttributeError

        self.supports = supports

        self.length = length

        # Attribute Varifing -- length
        if self.length[0] <= 0:
            raise AttributeError
        else:
            if self.length[0] < 1 and self.length[0] > 0.09:
                convergence = convert_to(self.length[0]*self.length[1], units.centimeters)
                self.length = (convergence/units.centimeters, units.centimeters)

            elif self.length[0] < 0.1 and self.length[0] > 0.009:
                convergence = convert_to(self.length[0]*self.length[1], units.millimeters)
                self.length = (convergence/units.millimeters, units.millimeters)





if __name__ == '__main__':
    pass
    """

                      | 30kN                   10kN         
                      |                         |
    25kN/m            |                         |________________ 50kN/m 
    __________________|_________________________| | | | | | | | |
    | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |  
    V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V
    =============================================================
    A                                                           A
   AAA                                                         AAA
            3                      4                     3              
    ------------------|-------------------------|----------------
    -------------------------------------------------------------
                                   10
    
    This Structure(the Beam)  Has.....                     
                                   
     2 Supports
     4 Loads --> 2 Point & 2 Continuous
     length of 10m --> segmented in 3m (the P1 position), 4m ( the intermidiate position) and 3m (the P2 position)
     | --> also, could be segmented in 3m, 0.5m, 3.5m, 1.5m, 1.5m (the PC1 and PC2 positions) 
     
     A Struture must have: 
     
     At least 1 Support
     At least 1 Load
     An Certain Length - At least 1m. 
     
     Something like this...
     
     | P 
     |
     |
     V                  |\
     ===================|\
                        |\  
     ------------------- \ 
                z
     
     structure:
        loads -----> list of load (Point or Continuous or yet Momentum) PS: Considering only vertical forces 
        supports --> int of max of 3 and min of 1 (default 2)
        length ----> float and a Quantity (Default 1 meter)
    
    
    function isostatic(struture)
    supports incognits 
    sum(point loads) = 0 
    sum(resulting momentum) =
    
    return supports values
    
    
    
     
     
     
     
     
     
                                   
                          | 175kN   
                          |                              | 150kN
                      | 30kN                   10kN      |   
                      |   |                      |       | 
                      |   |                      |       |
                      |   |                      |       |
                      |   |                      |       | 
                      V   V                      V       V
    =============================================================
    A                                                           A
    |                                                           |
    |                                                           |
    |                                                           |
    Ra                                                          Rb
    
    
    C1 = 25kN/m ---> PC1 = 175kN
    C2 = 50kN/m ---> PC2 = 150kN 
    P1 = 30kN
    P2 = 10kN
    
    Ra = ? 
    Rb = ? 
    
    -> Em vigas biapoiadas
    
    Ra = (Σ (P*b))/(a+b)
    Rb = (Σ (P*a))/(a+b)
    
    
    METODO DAS EQUAÇÕES
    
            25kN/m           S1 
        ___________________|      <-----\ M 
        | | | | | | | | |  |    | Q     |     
        V V V V V V V V V  |    |       |
        ===================| ---|--> N  |
        A                  |    |       |
        |                  |    V  _____/
        |                  |
        |---------Z--------|
        |
        174.25kN 
    
        -Q + 174.25 - 25Z -----> Q = -25Z + 174.25
        M - 174.25 + 25Z * Z/2 --> M = -12.5Z^2 + 174.25
        
    """









