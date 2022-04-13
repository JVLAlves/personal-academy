package mecsol

import "math"

type GranCurve struct {
	D60 float64
	D10 float64
	D30 float64
}

func NewGranCurve(d10, d30, d60 float64) GranCurve {
	return GranCurve{D10: d10, D30: d30, D60: d60}
}

func (c GranCurve) UniCoefficient() (float64, string) {
	CU := c.D60 / c.D10

	switch {

	case CU < 5:
		return CU, "Uniforme"
	case 5 < CU && CU <= 5:
		return CU, "Medianamente Uniforme"
	case CU > 15:
		return CU, "Desuniforme"
	}
	return CU, ""
}

func (c GranCurve) CurvCoefficient() (float64, string) {
	CC := (math.Pow(c.D30, 2)) / (c.D60 * c.D10)

	switch {

	case 1 < CC && CC < 3:
		return CC, "Contĩnua (Bem Graduado)"
	case CC < 1:
		return CC, "Descontínua (Mal Graduado)"
	case CC > 3:
		return CC, "Curva uniforme na parte central (Mal Graduado)"
	}

	return CC, ""

}

type Atterberg struct {
	LL float64 //Limite de Liquidez
	LP float64 //Limite de Plasticidade
	LC float64 //Limite de Contração
}

func NewAtterberg(ll, lp, lc float64) Atterberg {
	return Atterberg{LL: ll, LP: lp, LC: lc}
}

func (a Atterberg) IP() float64 {

	return a.LL - a.LP
}
