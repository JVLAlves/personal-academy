package main

import (
	"fmt"
	"strconv"
)

func main() {
	var n float64 = 4.87
	nint := float64(int(n))
	nfloat, _:= strconv.ParseFloat(fmt.Sprintf("%.2f", n - nint), 64)
	fmt.Println(nint, nfloat)
	seg := nfloat / 60
	fmt.Println(seg)
}
