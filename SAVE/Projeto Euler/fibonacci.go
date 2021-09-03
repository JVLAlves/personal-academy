package main

import "fmt"

func main() {
	numbers := []int{}
	n := 2
	for c := 0; c < 10001; c++ {
		if n/1 == 0 && n%n == 0 {
			numbers = append(numbers, n)
		}
		n += 1

	}
	fmt.Println(numbers)
}
