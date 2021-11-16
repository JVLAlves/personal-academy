package main

import (
	"fmt"
	"strconv"
	"strings"
)

var Enter string
var Alphabet = [26]string{"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"}
var Tebahpla = [26]string{"Z", "Y", "X", "W", "V", "U", "T", "S", "R", "Q", "P", "O", "N", "M", "L", "K", "J", "I", "H", "G", "F", "E", "D", "C", "B", "A"}
var Unciphered string
var x int
var i int
var Ciphered []string
var Encrypted string

type Vigenèrie struct {
	Ç []string
	A []string
	B []string
	C []string
	D []string
	E []string
	F []string
	G []string
	H []string
	I []string
	J []string
	K []string
	L []string
	M []string
	N []string
	O []string
	P []string
	Q []string
	R []string
	S []string
	T []string
	U []string
	V []string
	W []string
	X []string
	Y []string
	Z []string
}

func CeaserThis(Unciphered string) (Encrypted string) {

	for x = 0; x < len(Unciphered); x++ {
		for i = 0; i < len(Alphabet); i++ {
			fmt.Printf(" Alphabet: %v; Unciphered: %v;\n", Alphabet[i], string(Unciphered[x]))
			if string(Unciphered[x]) == Alphabet[i] {
				if Alphabet[i] == "Z" {
					Ciphered = append(Ciphered, Alphabet[len(Alphabet)-24])
					break
				} else if Alphabet[i] == "Y" {
					Ciphered = append(Ciphered, Alphabet[len(Alphabet)-25])
					break
				} else if Alphabet[i] == "X" {
					Ciphered = append(Ciphered, Alphabet[len(Alphabet)-26])
					break
				}
				Ciphered = append(Ciphered, Alphabet[(i+3)])
				break
			}
		}
		i = 0
	}

	Encrypted = strings.Join(Ciphered, "")
	return Encrypted
}

func DecryptThis(Encrypted string) (Decrypted string) {
	Ciphered = []string{}
	for x = 0; x < len(Encrypted); x++ {
		for i = 0; i < len(Alphabet); i++ {
			fmt.Printf(" Alphabet: %v; Unciphered: %v;\n", Alphabet[i], string(Encrypted[x]))
			if string(Encrypted[x]) == Alphabet[i] {
				if Alphabet[i] == "A" {
					Ciphered = append(Ciphered, Alphabet[len(Alphabet)-3])
					break
				} else if Alphabet[i] == "B" {
					Ciphered = append(Ciphered, Alphabet[len(Alphabet)-2])
					break
				} else if Alphabet[i] == "C" {
					Ciphered = append(Ciphered, Alphabet[len(Alphabet)-1])
					break
				}
				Ciphered = append(Ciphered, Alphabet[(i-3)])
				break
			}
		}
		i = 0
	}

	Decrypted = strings.Join(Ciphered, "")
	return Decrypted
}

func GravityFallsThis(entrada string) (mensage string) {
	var solved []string
	var Analysis []string
	Chop := strings.Split(entrada, " ")
	for j := 0; j < len(Chop); j++ {
		//regex := functions.RegexThis(`[A-Z]`, Chop[j])
		Analysis = append(Analysis, Chop[j])

	}

	for k := 0; k < len(Analysis); k++ {
		solved = append(solved, A1Z26(Analysis[k]))
	}
	mensage = strings.Join(solved, " ")
	return mensage

}

func AtbashThis(Encrypted string) (Decrypted string) {
	Ciphered = []string{}
	for x = 0; x < len(Encrypted); x++ {
		for i = 0; i < len(Tebahpla); i++ {
			fmt.Printf(" Tebahpla: %v; Unciphered: %v;\n", Tebahpla[i], string(Encrypted[x]))
			if string(Encrypted[x]) == Tebahpla[i] {
				Ciphered = append(Ciphered, Alphabet[i])
				break
			}
		}
		i = 0
	}
	Decrypted = strings.Join(Ciphered, "")
	return Decrypted
}

func A1Z26(Encrypted string) (Decrypted string) {
	Ciphered := []string{}
	Chopper := strings.Split(Encrypted, "-")
	for x = 0; x < len(Chopper); x++ {
		for i = 0; i < len(Alphabet); i++ {
			Wordnum, _ := strconv.Atoi(Chopper[x])
			fmt.Println("WordNumn", Wordnum)
			Numword := i + 1
			fmt.Println("NumWord", Numword)
			if Wordnum == Numword {
				Ciphered = append(Ciphered, Alphabet[i])
				break

			}

		}
		i = 0
	}
	Decrypted = strings.Join(Ciphered, "")
	return Decrypted

}

func VIG(Encrypted string) {
	for y := 0; y < len(Encrypted); y++ {

	}
}
func Vigenerie(key string, Encrypted string) (Decrypted string) {

	Vivi := Vigenèrie{
		Ç: []string{"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"},
		A: []string{"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"},
		B: []string{"B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A"},
		C: []string{"C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B"},
		D: []string{"D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C"},
		E: []string{"E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D"},
		F: []string{"F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E"},
		G: []string{"G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F"},
		H: []string{"H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G"},
		I: []string{"I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H"},
		J: []string{"J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I"},
		K: []string{"K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J"},
		L: []string{"L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"},
		M: []string{"M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"},
		N: []string{"N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"},
		O: []string{"O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N"},
		P: []string{"P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"},
		Q: []string{"Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P"},
		R: []string{"R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q"},
		S: []string{"S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R"},
		T: []string{"T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S"},
		U: []string{"U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T"},
		V: []string{"V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U"},
		W: []string{"W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V"},
		X: []string{"X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W"},
		Y: []string{"Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X"},
		Z: []string{"Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y"},
	}

	Ciphered := []string{}
	keywords := []string{}
	truekeywords := [][]string{}
	Index := []int{}

	i = 0
	x = 0
	for u := 0; u < len(Encrypted); u++ {
		fmt.Printf("ENCRYPTED[%v] of %v: %v\n", u, len(Encrypted), string(Encrypted[u]))
		fmt.Printf("KEY[%v] of %v: %v\n", i, len(key), string(key[i]))
		keywords = append(keywords, string(key[i]))
		i++
		if i > (len(string(key)) - 1) {
			i = 0
		}
	}
	for k := 0; k < len(keywords); k++ {
		switch keywords[k] {

		case "A":
			truekeywords = append(truekeywords, Vivi.A)
		case "B":
			truekeywords = append(truekeywords, Vivi.B)
		case "C":
			truekeywords = append(truekeywords, Vivi.C)
		case "D":
			truekeywords = append(truekeywords, Vivi.D)
		case "E":
			truekeywords = append(truekeywords, Vivi.E)
		case "F":
			truekeywords = append(truekeywords, Vivi.F)
		case "G":
			truekeywords = append(truekeywords, Vivi.G)
		case "H":
			truekeywords = append(truekeywords, Vivi.H)
		case "I":
			truekeywords = append(truekeywords, Vivi.I)
		case "J":
			truekeywords = append(truekeywords, Vivi.J)
		case "K":
			truekeywords = append(truekeywords, Vivi.K)
		case "L":
			truekeywords = append(truekeywords, Vivi.L)
		case "M":
			truekeywords = append(truekeywords, Vivi.M)
		case "N":
			truekeywords = append(truekeywords, Vivi.N)
		case "O":
			truekeywords = append(truekeywords, Vivi.O)
		case "P":
			truekeywords = append(truekeywords, Vivi.P)
		case "Q":
			truekeywords = append(truekeywords, Vivi.Q)
		case "R":
			truekeywords = append(truekeywords, Vivi.R)
		case "S":
			truekeywords = append(truekeywords, Vivi.S)
		case "T":
			truekeywords = append(truekeywords, Vivi.T)
		case "U":
			truekeywords = append(truekeywords, Vivi.U)
		case "V":
			truekeywords = append(truekeywords, Vivi.V)
		case "W":
			truekeywords = append(truekeywords, Vivi.W)
		case "X":
			truekeywords = append(truekeywords, Vivi.X)
		case "Y":
			truekeywords = append(truekeywords, Vivi.Y)
		case "Z":
			truekeywords = append(truekeywords, Vivi.Z)
		}
	}

	for l := 0; l < len(Encrypted); l++ {

		for i = 0; i < len(truekeywords[l]); i++ {

			if string(Encrypted[l]) == truekeywords[l][i] {
				Index = append(Index, i)
				break
			}
		}
	}

	for c := 0; c < len(Index); c++ {
		Ciphered = append(Ciphered, Vivi.Ç[Index[c]])
	}

	Decrypted = strings.Join(Ciphered, "")
	return Decrypted

}

func main() {
	RESPONSE := Vigenerie("SHIFTER", "OOIYDMEVVNIBWRKAMWBRUWLL")
	fmt.Println(RESPONSE)
}
