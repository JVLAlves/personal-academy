import unittest
from resis.units import point,structure, continuous, kN, MPa
import sympy
import sympy.physics.units as units

class TestStructure(unittest.TestCase):
    ls1 = [point(1)]
    def test_structure_loads(self):

        ls4 = [1, 2, 3]
        ls5 = [point(1), continuous(2), 3]
        ls6 = [point(1), 2, continuous(3)]
        ls7 = [1, point(2), continuous(3)]

        self.assertRaises(AttributeError, structure, ls4, 2, (1, units.meters))  # fully incorrect type array
        self.assertRaises(AttributeError, structure, ls5, 2, (1, units.meters))  # last   position incorrect type
        self.assertRaises(AttributeError, structure, ls6, 2, (1, units.meters))  # middle position incorrect type
        self.assertRaises(AttributeError, structure, ls7, 2, (1, units.meters))  # first  position incorrect type

    def test_structure_supports(self):



        self.assertRaises(AttributeError, structure, self.ls1, -1, (1, units.meters))  # Negative  amount
        self.assertRaises(AttributeError, structure, self.ls1, 0, (1, units.meters))  # Null       amount
        self.assertRaises(AttributeError, structure, self.ls1, 3, (1, units.meters))  # Overvalued amount


    def test_structure_length(self):

        self.assertRaises(AttributeError, structure, self.ls1, 2, (0, units.meters))  # null      length
        self.assertRaises(AttributeError, structure, self.ls1, 2, (-1, units.meters))  # negative length


        S1 = structure( self.ls1, 2, (0.1, units.meters))
        S01 = structure(self.ls1, 2, (0.01, units.meters))

        self.assertEqual(S01.length[1], units.millimeter) # Convert to millimeters
        self.assertEqual(S1.length[1], units.centimeters) # Convert to Centimeters
        self.assertEqual(S1.length[0], 10)                # 0.1 Meters is 10 Centimeters
        self.assertEqual(S01.length[0], 10)              # 0.01 Meters is 10 millimeters

if __name__ == '__main__':
    unittest.main()
