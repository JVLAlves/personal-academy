package main

import "fmt"

var Kind string

type ForceOut struct {
	a float64
	m float64
}

type AccelOut struct {
	f float64
	m float64
}

type MassOut struct {
	f float64
	a float64
}

type Force interface {
	Newton() (f float64, k string)
}

func (f ForceOut) Newton() (F float64, k string) {

	return f.a * f.m, "Force"

}

func (a AccelOut) Newton() (A float64, k string) {

	return a.f / a.m, "Acceleration"

}

func (m MassOut) Newton() (M float64, k string) {

	return m.f / m.a, "Mass"

}

func Resolve(f Force) {
	r, k := f.Newton()
	switch k {
	case "Force":
		fmt.Printf("%vN\n", r)
	case "Acceleration":
		fmt.Printf("%vm/s²\n", r)
	case "Mass":
		fmt.Printf("%vKg\n", r)
	}
}

func main() {
	var Incog string
	var Var1 float64
	var Var2 float64
	fmt.Scanf("%v", &Incog)

	switch Incog {

	case "F":
		fmt.Printf("Acceleration: ")
		fmt.Scanf("%v\n", &Var1)
		fmt.Printf("Mass: ")
		fmt.Scanf("%v\n", &Var2)

		eq := ForceOut{
			a: Var1,
			m: Var2,
		}
		Resolve(eq)
	case "A":
		fmt.Printf("Force: ")
		fmt.Scanf("%v", &Var1)
		fmt.Printf("Mass: ")
		fmt.Scanf("%v", &Var2)

		eq := AccelOut{
			f: Var1,
			m: Var2,
		}
		Resolve(eq)
	case "M":
		fmt.Printf("Force: ")
		fmt.Scanf("%v", &Var1)
		fmt.Printf("Acceleration: ")
		fmt.Scanf("%v", &Var2)

		eq := MassOut{
			f: Var1,
			a: Var2,
		}
		Resolve(eq)

	}
}
