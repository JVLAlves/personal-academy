package main

import (
	"fmt"
	"log"
	"math"

	"github.com/fatih/color"
	"github.com/rodaine/table"
)

type Convergence interface {
	Method() float64
}

//Tipo para realização do Metodo de Newton-Raphson
type NewtonRaphson struct {
	f        func(x float64) float64 //Função f(x)
	d        func(x float64) float64 //Derivada f'(x) ou d(x)
	tol      float64                 //Tolerância
	itmax    int                     //Iterações máximas
	interval [2]float64              //Intervalo de convergencia
}

//Tipo para realização do Metodo de Bissecção
type Bissection struct {
	f    func(float64) float64 // Função f(x)
	a    float64               // Intervalo a
	b    float64               // Intervalo b
	tol  float64               // Tolerância
	nmax float64               // Número máximo de iterações
}

/*Variaveis de cor

Implementação: fmt.Print( string(colorName), "stringparacolor")*/
var (
	colorReset  string = "\033[0m"
	colorRed    string = "\033[31m"
	colorGreen  string = "\033[32m"
	colorYellow string = "\033[33m"
	colorBlue   string = "\033[34m"
	colorPurple string = "\033[35m"
	colorCyan   string = "\033[36m"
	colorWhite  string = "\033[37m"
)

func (b Bissection) Method() (c float64) {
	//Contador Float --> Para limitar
	n := 0.0

	//Contador de Iterações
	i := 0

	//Arrays de histórico
	Iter := []int{}
	Interval := [][]float64{}
	X := []float64{}
	Fx := []float64{}

	//Metodo da Bissecção
	for n <= b.nmax {

		//Formula de iteração
		c = (b.a + b.b) / 2
		//Limpa Array de Armazenamento Intermediario do Intervalo
		Inter := []float64{}

		//Acrescenta informações aos seus devidos lugares
		X = append(X, c)
		Iter = append(Iter, i)
		Inter = append(Inter, b.a)
		Inter = append(Inter, b.b)
		Interv := Inter[:]
		Interval = append(Interval, Interv)
		Fx = append(Fx, b.f(c))

		//Expõe o valor de X aproximado no momento
		fmt.Printf("X= %v%v%v\n\n", string(colorYellow), c, string(colorReset))

		//Se F(x) == 0, X aproximado encontrado.
		if b.f(c) == 0 {
			//Define a formatação da tabela que será criada futuramente
			headerFmt := color.New(color.FgGreen, color.Underline).SprintfFunc()
			columnFmt := color.New(color.FgYellow).SprintfFunc()

			//Cria tabela com os Cabeçalhos "Iterações", "x", "f(x)"
			tbl := table.New("Iterações", "x", "Intervalo", "F(x)")

			//Implementação da formatação
			tbl.WithHeaderFormatter(headerFmt).WithFirstColumnFormatter(columnFmt)

			//Acrescentando informações a tabela
			for n, _ := range Iter {
				tbl.AddRow(Iter[n], X[n], Interval[n], Fx[n])
			}

			//Print da tabela
			tbl.Print()

			//Retorna X aproximado
			return c
		}

		//Incremento no contador de iteração
		n++

		//Expõe Valores de F(a) e F(x)
		fmt.Printf("F(a) = %v\n", b.f(b.a))
		fmt.Printf("F(c) = %v\n\n", b.f(c))

		//Expõe Diferença ou Igualdade de sinais
		fmt.Printf("SIGNAL C: %v\n", math.Signbit(b.f(c)))
		fmt.Printf("SIGNAL A: %v\n\n", math.Signbit(b.f(b.a)))

		//Se os sinais forem iguais, substitui o intervalo a. Caso contrário, substitui o valor do intervalo b.
		if math.Signbit(b.f(c)) == math.Signbit(b.f(b.a)) {
			fmt.Printf("[%v%v%v, %v]\n", string(colorGreen), b.a, string(colorReset), b.b)
			b.a = c
		} else {
			fmt.Printf("[%v, %v%v%v]\n", b.a, string(colorGreen), b.b, string(colorReset))
			b.b = c
		}

		//Incremento no contador de limite
		i++
	}

	//Caso o contador de limite seja exedido, o intervalo não converge para um X aproximado.
	log.Fatalf("NÃO CONVERGE EM SOMENTE %v ITERAÇÕES", i)
	return 0
}
func (n NewtonRaphson) Method() float64 {
	//Arrays de histórico
	Iter := []int{}
	Seed := []float64{}
	Zero := []float64{}

	//Iteração 0
	c := 0
	Xo := (n.interval[0] + n.interval[1]) / 2
	if n.d(Xo) == 0 {
		log.Fatalf("Erro Matemático.")
	}

	Iter = append(Iter, c)
	Seed = append(Seed, Xo)
	Zero = append(Zero, n.f(Xo))

	if math.Abs(n.f(Xo)) > n.tol {
		for c < n.itmax {
			//Incrementa contador de iterações
			c++

			//Verifica se d(x) = 0 (Ela não pode ser zero, pois é o denominador da fórmula de iteração)
			if n.d(Xo) == 0 {
				log.Fatalf("Erro Matemático.")
			}

			//Fórmula de iteração
			X1 := Xo - (n.f(Xo) / (n.d(Xo)))

			//Expõe processos realizados
			fmt.Printf("%v%v%v\n", string(colorYellow), c, string(colorReset))
			fmt.Printf("Xo - f(Xo) / d(Xo)  = %v\n", X1)
			fmt.Printf("F(%v) = %v%v%v\n\n", X1, string(colorBlue), n.f(X1), string(colorReset))

			//Acrescenta resultados a listas de "Histórico"
			Seed = append(Seed, X1)
			Iter = append(Iter, c)
			Zero = append(Zero, n.f(X1))

			//Se f(x) for menor que a tolerância, raiz não encontrada. Continua iterando.
			//Caso contrário, raiz encontrada.
			if math.Abs(n.f(X1)) > n.tol {
				Xo = X1
				continue
			} else {

				//Define a formatação da tabela que será criada futuramente
				headerFmt := color.New(color.FgGreen, color.Underline).SprintfFunc()
				columnFmt := color.New(color.FgYellow).SprintfFunc()

				//Cria tabela com os Cabeçalhos "Iterações", "x", "f(x)"
				tbl := table.New("Iterações", "x", "F(x)")

				//Implementação da formatação
				tbl.WithHeaderFormatter(headerFmt).WithFirstColumnFormatter(columnFmt)

				//Acrescentando informações a tabela
				for n, _ := range Iter {
					tbl.AddRow(Iter[n], Seed[n], Zero[n])
				}

				//Print da tabela
				tbl.Print()

				//Retorna resultados
				return X1
			}

		}

		//Caso o intervalo não converja, Print dos Seeds e fatal log
		fmt.Printf("Seed: %v%v%v", string(colorBlue), Seed, string(colorReset))
		log.Fatalf("NÃO CONVERGE EM SOMENTE %v ITERAÇÕES", c)
		return 0
	}
	//Caso, na mais completa sorte, o intervalo converja de primeira, Print do Seed e retorna os valores
	fmt.Printf("Seed: %v%v%v", string(colorBlue), Seed, string(colorReset))
	return Xo
}

func Converge(c Convergence) {
	fmt.Printf("\nANSWER: %v%v%v\n", string(colorYellow), c.Method(), string(colorReset))
}

var f func(float64) float64
var tol float64
var d func(float64) float64

func main() {

	//METODO DE NEWTON-RAPHSON

	f = func(x float64) float64 { return (math.Pow(x, 6)) + (6.3 * x) - 18.2 } // Função F(x)
	d = func(x float64) float64 { return (6*(math.Pow(x, 5)) + 6.3) }          //Derivada F'(x)
	tol = math.Pow10(-6)                                                       //Tolerancia

	eq := NewtonRaphson{
		f:        f,
		d:        d,
		tol:      tol,
		itmax:    5,
		interval: [2]float64{-2, -1.5},
	}
	/*
		//METODO DA BISSECÇÃO
		tol = 1
		f = func(x float64) float64 {
			var p float64 = 1
			var q float64 = 4

			return (math.Pow(x, 3) + (p * x) + q)
		}
		eq := Bissection{

			f:    f,
			a:    -1.5,
			b:    -1,
			tol:  tol,
			nmax: 500,
		}
	*/
	Converge(eq)
}
