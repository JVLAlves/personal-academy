package main

import (
	"fmt"
	"log"
	"math"
)

type ErrinDel struct{}

type Equation struct {
	Anum float64
	Bnum float64
	Cnum float64
}

type Fullequation struct {
	Anum float64
	Bnum float64
	Cnum float64
	X    float64
}

type Partequation struct {
	Anum  float64
	Bnum  float64
	Delta float64
}

type Resolution interface {
	Eqresolution() []float64
}
type Maximin interface {
	Vertice() []float64
}

func Resolve(r Resolution) {
	fmt.Println(r.Eqresolution())
}

func Vertex(m Maximin) {
	fmt.Println(m.Vertice())
}

func (f Fullequation) Eqresolution() (Coords []float64) {

	y := f.Anum*math.Pow(f.X, 2) + f.Bnum*math.Pow(f.X, 1) + f.Cnum
	Coords = append(Coords, f.X, y)
	return Coords

}

func (p Equation) Eqresolution() (Zeros []float64) {
	Delta := math.Pow(p.Bnum, 2) - (4 * p.Anum * p.Cnum)
	if Delta < 0 {
		log.Fatalf("Delta must be positive")

	}

	sqrt := math.Sqrt(Delta)
	r1 := ((p.Bnum * -1) + (sqrt)) / (2 * (p.Anum))
	r2 := ((p.Bnum * -1) - (sqrt)) / (2 * (p.Anum))
	Zeros = append(Zeros, r1, r2)

	return Zeros

}

func (p Equation) Vertice() (Maxes []float64) {

	Delta := math.Pow(p.Bnum, 2) - (4 * p.Anum * p.Cnum)

	Xmax := -(p.Bnum / (2 * p.Anum))
	Ymax := -(Delta / (4 * p.Anum))

	Maxes = append(Maxes, Xmax, Ymax)

	return Maxes

}

func (p Partequation) Vertice() (Maxes []float64) {

	Xmax := -(p.Bnum / (2 * p.Anum))
	Ymax := -(p.Delta / (4 * p.Anum))

	Maxes = append(Maxes, Xmax, Ymax)

	return Maxes

}

func main() {
	//eq := equation{-4, 0, 5}
	eq1 := Fullequation{1, -20, 36, 18}
	eq2 := Equation{Anum: -4, Bnum: 0, Cnum: 5}
	Resolve(eq1)
	Vertex(eq2)

}
