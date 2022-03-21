//esse programa foi criado com o intuito de  aprender a estrutura de go enquanto encontra soluções para o jogo Term.ooo.

package term

import (
	"bufio"
	"fmt"
	"math/rand"
	"os"
	"regexp"
	"strings"
	"time"

	"github.com/TwiN/go-color"
)

const Answer = "feroz"         //Answer é a responsa o qual o alvo é encontra-la utilizandoa  lógica do jogo.
const WordLength = len(Answer) //WordLength é a quantidade de caracteres da palavra resposta.

//OpenDictionary abre um arquivo de texto o qual contenha palavras e delas escolhe apenas as com determinado numero de letras.
func OpenDictionary(dictpath string, letterNum int) ([]string, error) {

	file, err := os.Open(dictpath)

	if err != nil {
		return nil, err
	}

	defer file.Close()

	scanner := bufio.NewScanner(file)

	scanner.Split(bufio.ScanLines)
	var text []string

	for scanner.Scan() {
		if len(scanner.Text()) == letterNum {
			text = append(text, strings.ToLower(scanner.Text()))
		}

	}

	if len(text) == 0 || (len(text) == 1 && text[0] == "") {
		return nil, fmt.Errorf("ERROR empty list")
	}

	return text, nil

}

//MaxinInt encontrar o maior valor inteiro em um mapa cuja as Keys também são inteiros.
func MaxinInt(array map[int]int) (int, int) {
	var largerNumber, LikelyPosition, temp int

	for key, element := range array {
		if element > temp {
			temp = element
			largerNumber = temp
			LikelyPosition = key
		}
	}
	return LikelyPosition, largerNumber
}

// MaxinString encontrar o maior valor inteiro em um mapa cuja as Keys são Strings.
func MaxinString(array map[string]int) (string, int) {
	var largerNumber, temp int
	var LikelyPosition string

	for key, element := range array {
		if element > temp {
			temp = element
			largerNumber = temp
			LikelyPosition = key
		}
	}
	return LikelyPosition, largerNumber
}

//RandomSeed escolhe do dicionário indicado uma palavra completamente aleatória.
func RandomSeed(dict []string, devmode bool) string {
	rand.Seed(time.Now().UnixNano())
	if devmode {
		fmt.Println(dict)
	}
	in := rand.Intn(len(dict))
	return dict[in]

}

// ScoreSeed escolhe do dicionário indicado uma palavra com base em uma pontoação
// A pontuação se dá pela quantidade de vezes que uma determinada letra parece em uma determinada posição no "range" de todo o dicionãrio.
func ScoreSeed(dict []string, devmode bool) string {
	if devmode {
		fmt.Printf("\nWORDS IN DICTIONARY: %v\n\n", len(dict))
	}
	if len(dict) == 2 {
		rand.Seed(time.Now().UnixNano())
		in := rand.Intn(len(dict))
		return dict[in]
	}

	PosMap := make(map[int]map[string]int)
	for i := 0; i < 5; i++ {
		letMap := make(map[string]int)
		for _, word := range dict {
			letMap[string(word[i])]++
		}
		PosMap[i] = letMap
	}

	if devmode {
		fmt.Println("POSITION QUANTITY MAP:")
		for key, value := range PosMap {

			fmt.Println(key, value)

		}
	}

	WordScoreMap := make(map[string]int)

	for _, W := range dict {
		var WordScore int

		for pos, Map := range PosMap {

			for leter, score := range Map {

				if string(W[pos]) == leter {

					WordScore += score
				}
			}

		}

		WordScoreMap[W] = WordScore

	}

	GoodWord, score := MaxinString(WordScoreMap)
	if devmode {
		fmt.Printf("\nHIGHSCORED WORD: %v\nSCORE: %v\n", GoodWord, score)
	}
	return GoodWord
}

//FindStart procura no dicionãrio determinado palavras começem com uma determinada letra ou conjunto de letras.
func FindStart(dict []string, starting string) ([]string, error) {
	var redict []string
	for _, d := range dict {

		if strings.Contains(d, starting) && strings.Index(d, starting) == 0 {

			redict = append(redict, d)

		}

	}

	if len(redict) == 0 {
		return nil, fmt.Errorf("ERROR no words starting with '%v' in dictionary", starting)
	}

	return redict, nil

}

//LetterT é o tipo utilizado para armanezar informações sobre as letras de um chute.
type LetterT struct {
	seen       bool   //Indica se esse tipo já foi populado alguma vez
	value      string //Indica o a letra. Não chega a ser utilizado na prática, mas cumpre tabela.
	position   int    //Indica a posição a qual a letra foi encontrada pela primeira vez
	isReapeted bool   //Indica se essa letra é repetida alguma vez
	where      []int  //Indica as posições onde a letra ẽ repetida.
}

// MapWord analisa cada letra da palavra aleatória escolhida e popula o struct LetterT com as informações retiradas da anãlise.
func MapWord(dict []string, seed string) (map[string]*LetterT, error) {

	var letMap = make(map[string]*LetterT)
	for index, letter := range seed {
		//O programa informa a existência de uma determianda letra com base em sua(s) posição(ôes)
		//Caso ela exista na palavra resposta, a posição indicada - por padrão - recebe +1 e torna-se negativa. Isso indica que a palavra existe mas não está na posição correta.
		if strings.Contains(Answer, string(letter)) {
			//Caso a key já exista no mapa, isso indica que essa letra é repetida.
			LetterValue, ok := letMap[string(letter)]

			//Confirma-se completamente a repetição da letra se o atributo seen dela for verdadeiro.
			if ok && LetterValue.seen {

				//Caso ela seja repetida, o atribute isReapeted torna-se verdadeiro e marca-se o lugar onde ela se repte no array Where
				letMap[string(letter)].isReapeted = true
				letMap[string(letter)].where = append(letMap[string(letter)].where, (index+1)*-1)

			} else {

				let := &LetterT{
					seen:       true,
					value:      string(letter),
					position:   (index + 1) * -1,
					isReapeted: false,
					where:      nil,
				}

				letMap[string(letter)] = let
			}

		} else {
			//Caso a palavra não exista, ela recebe a posição 0
			let := &LetterT{
				seen:       true,
				value:      string(letter),
				position:   0,
				isReapeted: false,
				where:      nil,
			}

			letMap[string(letter)] = let
			continue
		}
		LettList := letMap[string(letter)]
		Multi, _ := MultiIndex(Answer, string(letter))

		//Por fim, caso ela existe e esteja na posição correta, a posição padrão é alterada para positiva e +1
		for _, m := range Multi {

			//se o atributo isReapeted for verdadeiro, analisa se a letra está na posição correta no array.
			if LettList.isReapeted {

				if index == m {
					LettList.where[len(LettList.where)-1] = index + 1
				}

			} else {
				if index == m {
					LettList.position = index + 1
				}
			}
		}
	}

	return letMap, nil

}

// MultiIndex verifica se uma determina letra se repete mais de uma vez na palavra resposta.
func MultiIndex(answer, letter string) ([]int, error) {
	var Multindex []int
	re := regexp.MustCompile(letter)
	IndexList := re.FindAllIndex([]byte(answer), -1)
	for _, v := range IndexList {
		Multindex = append(Multindex, v[0])
	}

	if len(Multindex) == 0 {
		err := fmt.Errorf("ERROR\tThere is no '%v' in the chosen word", letter)
		return nil, err
	}
	return Multindex, nil
}

// Funnel verifica quais palavras satisfazem as condiçôes de inclusão e então retorna um novo dicionãrio com essas palavras.
//as condições de inclusão estão relacionadas com a posição de cada letra, se ela existe, se está correta ou não.
func Funnel(dict []string, m map[string]*LetterT) ([]string, error) {
	var Redict []string
	for _, word := range dict {
		var appendable int = 0
		var appendableUnits int = len(m)
		//A função analisa letra a letra a palavra retirada do dicionãrio e aplica a ela as condições de inclusão.
		for key, letterT := range m {

			if letterT.position == 0 {
				if !strings.Contains(word, key) {
					appendable++
				}
			}

			if letterT.position < 0 {
				index := (letterT.position * -1) - 1
				if strings.Contains(word, key) && !(string(word[index]) == key) {
					appendable++
				}
			}

			if letterT.position > 0 {

				index := (letterT.position - 1)
				if strings.Contains(word, key) && string(word[index]) == key {
					appendable++
				}

			}

			if letterT.isReapeted {

				appendableUnits += len(letterT.where)

				for _, RePos := range letterT.where {

					if RePos < 0 {
						index := (RePos * -1) - 1
						if strings.Contains(word, key) && !(string(word[index]) == key) {
							appendable++
						}
					}

					if RePos > 0 {

						index := (RePos - 1)
						if strings.Contains(word, key) && string(word[index]) == key {
							appendable++
						}

					}

				}

			}
		}

		if appendable == appendableUnits {
			Redict = append(Redict, word)
		}
	}

	if len(Redict) == 0 || Redict == nil {
		return nil, fmt.Errorf("ERROR\t Verification malfunctioned")
	}
	return Redict, nil

}

//RandomGenT é o tipo utilizado como parametro no momento de rodar certas funções. Dessa forma, é possĩvel diversificar o cdóigo com poucas linhas.
type RandomGenT func([]string, bool) string

//MatchRunner é o conjunto de todas as funções que componhe o jogo.
//Ao chamá-la, receberemos o número de tentativas necessesárias para descobrir a palavra resposta.
func MatchRunner(dict []string, ARandom RandomGenT, Devmode bool) int {
	var Redict = dict
	var c int = 1
	var Rand string
MatchLoop:
	for {

		//A funçao do tipo RandomGenT é uma abertura para testar diversas funções que retornam um certo tipo de chute.
		Rand = ARandom(Redict, Devmode)

		if Devmode {
			fmt.Printf("\nREAL GUESS: %v\nGUESS COUNT: %v\n\n", color.Ize(color.Green, Rand), c)
		}

		if Rand == Answer {
			if Devmode {
				fmt.Println("OK!")
			}

			break MatchLoop
		}
		Map, _ := MapWord(Redict, Rand)
		for k, v := range Map {
			if Devmode {
				fmt.Println(k, v)
			}

		}

		Redict, _ = Funnel(Redict, Map)
		if Devmode {
			fmt.Printf("\nDICTIONARY:\t%v\n\n", Redict)
		}

		if len(Redict) > 0 && len(Redict) < 3 {
			if (Redict[0] == Answer && len(Redict) == 1) || (Redict[0] == Answer && Redict[1] == Redict[0]) {

				if Devmode {
					fmt.Println("OK!")
				}

				break MatchLoop

			}

		}
		c++
	}
	return c
}
