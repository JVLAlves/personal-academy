package main

import (
	"fmt"
	"math"
)

type bissection struct {
	f    func(float64) float64
	a    float64
	b    float64
	tol  float64
	nmax float64
}

var function = func(x float64) float64 {

	return (math.Pow(2, x) - (3 * x))
}

func (b bissection) Bmethod() (c float64, n float64, success bool) {
	for n <= b.nmax {
		fmt.Printf("[%v, %v]\n", b.a, b.b)
		c = (b.a + b.b) / 2
		fmt.Println(c)
		if b.f(c) == 0 || (b.b-b.a)/2 < b.tol {
			return c, n, true
		}
		n++
		fmt.Printf("F(a) = %v\n", b.f(b.a))
		fmt.Printf("F(c) = %v\n\n", b.f(c))
		fmt.Printf("SIGNAL C: %v\n", math.Signbit(b.f(c)))
		fmt.Printf("SIGNAL A: %v\n", math.Signbit(b.f(b.a)))
		if math.Signbit(b.f(c)) == math.Signbit(b.f(b.a)) {
			b.a = c
		} else {
			b.b = c
		}
	}
	return 0, n, false
}

func main() {
	eq := bissection{
		f:    function,
		a:    0,
		b:    1,
		tol:  0.1,
		nmax: 100,
	}

	fmt.Println(eq.Bmethod())
}
