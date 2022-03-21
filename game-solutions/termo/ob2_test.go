package term_test

import (
	"fmt"
	term "termo"
	"testing"

	"github.com/stretchr/testify/require"
)

func TestOpenDictionary(t *testing.T) {

	dict, err := term.OpenDictionary("palavras.txt", term.WordLength)
	require.NoError(t, err)
	require.NotEmpty(t, dict)
	require.NotNil(t, dict)
	for _, d := range dict {
		require.Equal(t, term.WordLength, len(d))
		require.NotEmpty(t, d)
	}

	_, err2 := term.OpenDictionary("ds.txt", term.WordLength)
	require.Error(t, err2)

	_, err3 := term.OpenDictionary("palavras.txt", 0)
	require.Error(t, err3)

}

func TestMaxinInt(t *testing.T) {
	array := make(map[int]int)
	array[1] = 32
	array[2] = 41
	key, num := term.MaxinInt(array)
	require.Equal(t, 41, num)
	require.Equal(t, 2, key)

}

func TestRandomSeed(t *testing.T) {
	dict, _ := term.OpenDictionary("palavras.txt", term.WordLength)
	ChancesMap := make(map[string]int)
	for i := 0; i < 4; i++ {
		Rand := term.RandomSeed(dict, true)
		ChancesMap[Rand]++

	}
	require.NotEmpty(t, ChancesMap)
	require.NotEqual(t, 1, len(ChancesMap))
}
func TestScoreSeed(t *testing.T) {
	var Two = []string{"morte", "morrido"}
	dict, _ := term.OpenDictionary("palavras.txt", term.WordLength)
	Rand := term.ScoreSeed(dict, true)
	require.Equal(t, term.WordLength, len(Rand))
	ChancesMap := make(map[string]int)
	for i := 0; i < 10; i++ {
		Rand := term.ScoreSeed(Two, true)
		ChancesMap[Rand]++

	}

	fmt.Println(len(ChancesMap))
	require.NotEmpty(t, ChancesMap)
	require.NotEqual(t, 1, len(ChancesMap))
}

func TestFunnel(t *testing.T) {

	dict, err1 := term.OpenDictionary("palavras.txt", term.WordLength)
	require.NoError(t, err1)
	Rand := term.ScoreSeed(dict, true)
	Map, err := term.MapWord(dict, Rand)
	require.NoError(t, err)
	Dict, errD := term.Funnel(dict, Map)
	require.NoError(t, errD)
	for _, d := range Dict {
		require.Equal(t, term.WordLength, len(d))
	}
	require.NotEmpty(t, dict)
	require.NotEqual(t, len(dict), len(Dict))
	require.NotSame(t, dict, Dict)
	_, err2 := term.Funnel([]string{}, Map)
	require.Error(t, err2)
}

func TestFindStart(t *testing.T) {

	dict, err1 := term.OpenDictionary("palavras.txt", term.WordLength)
	require.NoError(t, err1)
	Words, err2 := term.FindStart(dict, "")
	require.NoError(t, err2)
	for _, word := range Words {
		fmt.Println(word)
	}
	_, err3 := term.FindStart(dict, "0")
	require.Error(t, err3)

}

func TestMultiIndex(t *testing.T) {

	num, err := term.MultiIndex("errar", "r")
	require.NoError(t, err)
	require.Equal(t, 3, len(num))
	_, err2 := term.MultiIndex("errar", "m")
	require.Error(t, err2)

}

func TestMatch(t *testing.T) {

	dict, err1 := term.OpenDictionary("palavras.txt", term.WordLength)
	require.NoError(t, err1)
	GameMap := make(map[int]int)
	for i := 0; i < 100; i++ {
		c := term.MatchRunner(dict, term.ScoreSeed, true)
		GameMap[c]++
	}
	require.NotEqual(t, 0, len(GameMap))

	GameMap2 := make(map[int]int)
	for i := 0; i < 100; i++ {
		c2 := term.MatchRunner(dict, term.RandomSeed, true)
		GameMap2[c2]++
	}
	require.NotEqual(t, 0, len(GameMap2))

}
