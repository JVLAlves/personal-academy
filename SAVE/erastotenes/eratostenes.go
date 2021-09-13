package main

import (
	"fmt"
	"log"

	"github.com/fatih/color"
	"github.com/rodaine/table"
)

var Numbers []int
var Odd []int
var Counter int = 2
var Iter int = 0
var Size int = 0
var Sizenum int = 10001

func main() {
	//Define a formatação da tabela que será criada futuramente
	headerFmt := color.New(color.FgGreen, color.Underline).SprintfFunc()
	columnFmt := color.New(color.FgYellow).SprintfFunc()

	//Cria tabela com os Cabeçalhos "Iterações", "x", "f(x)"
	tbl := table.New("Position", "Odd")

	//Implementação da formatação
	tbl.WithHeaderFormatter(headerFmt).WithFirstColumnFormatter(columnFmt)

	for {
		c := Counter
		for j := 0; j < 105000; j++ {
			Numbers = append(Numbers, c)
			c++
		}

		for _, v := range Numbers {
			if v != 0 {
				Odd = append(Odd, v)
			} else {
				continue
			}
			for i, c := range Numbers {
				if c%v == 0 {
					Numbers[i] = 0
				}
			}
		}

		for x, y := range Odd {
			if x == 10000 {
				fmt.Println(Odd)
				tbl.AddRow(x, y)
				tbl.Print()
				log.Fatalf("DONE")
			}

		}

	}

}

//Print da tabela
