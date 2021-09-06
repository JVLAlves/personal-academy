package main

import (
	"fmt"
	"log"
	"math"
)

type NewtonRaphson struct {
	f        func(x float64) float64
	fl       func(x float64) float64
	tol      float64
	itmax    int
	interval [2]float64
}

type bissection struct {
	f    func(float64) float64
	a    float64
	b    float64
	tol  float64
	nmax float64
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
func (n NewtonRaphson) NRMethod() (float64, int) {
	c := 0
	Xo := (n.interval[0] + n.interval[1]) / 2
	if n.fl(Xo) == 0 {
		log.Fatalf("Erro Matemático.")
	}
	if math.Abs(n.f(Xo)) > n.tol {
		c++
		for c < n.itmax {
			c++
			fmt.Printf("Xo = %v\n", Xo)
			if n.fl(Xo) == 0 {
				log.Fatalf("Erro Matemático.")
			}
			X1 := Xo - (n.f(Xo) / (n.fl(Xo)))
			fmt.Printf("X1 = %v\n", X1)
			fmt.Printf("F(%v) = %v\n", X1, n.f(X1))
			if math.Abs(n.f(X1)) > n.tol {
				Xo = X1
				continue
			} else {
				return X1, c
			}

		}
		log.Fatalf("NÃO CONVERGE")
		return 0, 0
	}
	return Xo, c
}

var f func(float64) float64

//var d func(float64) float64

func main() {
	f = func(x float64) float64 { return (math.Pow(x, 3) + (2 * x)) + 1 }

	eq := bissection{
		f:    f,
		a:    -1,
		b:    0,
		tol:  0,
		nmax: 500,
	}
	fmt.Println(eq.Bmethod())
}

/*
//função
func f(x float64) (y float64) {
	y = math.Exp(-x) - 1*x - 0.2
	return y
}

//derivada
func derf(x float64) (y float64) {
	y = math.Exp(-x) - 1
	return y
}

//raiz aproximada
func xk(x float64) (y float64) {
	y = x - (f(x) / derf(x))
	return y
}

func criterio(x float64) bool {
	if derf(x) == 0 {
		return false
	} else {
		return true
	}
}

//Variaveis
var result float64
var count int = 0
var x float64

func main() {

	fmt.Scanf("%v", &x)
	for {
		result = f(x)
		fmt.Printf("(%v) ZERO: %v\n", count, x)
		fmt.Printf("(%v) RESULT: %v\n", count, result)
		if math.Abs(result) > 0.01 {
			if criterio(x) {
				x = xk(x)
			} else {
				log.Fatalf("DERIVADA == 0")
			}
		} else {
			break
		}
		count++

	}
	fmt.Printf("\n(F) RAIZ APROXIMADA: %v\n", x)
}
*/
