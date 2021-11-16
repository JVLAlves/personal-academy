package main

import "fmt"

/*
É bem possível que existam casos onde hajam mais ou menos variaveis
que o definido nas Strutcs. Para lidar com isso é só fazer o seguinte:

No caso de Variaveis A MAIS que o definido:
Utilize o método mais de uma vez zerando os campos inutilizados.

No caso de Variaveis A MENOS que o definido:
Simplesmente zere os campos inutilizados.
*/
//Tipo para Pressão Diferencial
type Static interface {
	Pressure() float64
}
type Diferencial struct {
	Po    float64   //Pressão inicial
	Ylq1  float64   //Peso especifico do líquido 1
	Ylq2  float64   //Peso especifico do líquido 2
	Hslq1 []float64 //Array de alturas do líquido 1
	Hslq2 []float64 //Array de alturas do líquido 2
}

//Tipo para PRessão em Tubo em U
type TuboemU struct {
	Patm  float64   //Pressão Atmosférica no local
	Ylq1  float64   //Peso especifico do líquido 1
	Ylq2  float64   //Peso especifico do líquido 2
	Ylq3  float64   //Peso especifico do líquido 3
	Hslq1 []float64 //Array de alturas do líquido 1
	Hslq2 []float64 //Array de alturas do líquido 2
	Hslq3 []float64 //Array de alturas do líquido 3
}

//Método Pressure para Pressão Diferencial
func (d Diferencial) Pressure() (VarP float64) {
	VarP = 0.0

	for _, h := range d.Hslq1 {
		VarP += d.Ylq1 * h
	}

	for _, h := range d.Hslq2 {
		VarP += d.Ylq2 * h
	}

	return VarP
}

func (t TuboemU) Pressure() (VarP float64) {
	VarP = t.Patm

	for _, h := range t.Hslq1 {
		VarP += t.Ylq1 * h
	}

	for _, h := range t.Hslq2 {
		VarP += t.Ylq2 * h
	}

	for _, h := range t.Hslq3 {
		VarP += t.Ylq3 * h
	}

	return VarP

}

func Pressao(s Static) {
	fmt.Printf("Pressão Absoluta = %vPa\n", s.Pressure())

}

func main() {
	eq := TuboemU{
		Ylq1:  8330,
		Ylq2:  133280,
		Hslq1: []float64{-0.25, 0.15, 0.5},
		Hslq2: []float64{0.1},
	}

	Pressao(eq)
}
