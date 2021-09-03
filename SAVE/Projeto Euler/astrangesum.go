package megapower

import (
	"fmt"
	"math"
	"strconv"
)

func megapower() {
	result := 0
	numbers := []int{}
	f := int(math.Pow(2, 1000))
	s := strconv.Itoa(f)
	for n, _ := range s {
		c, _ := strconv.Atoi(string(s[n]))
		numbers = append(numbers, c)
	}

	for _, v := range numbers {
		result += v
	}

	fmt.Println(result)
}
