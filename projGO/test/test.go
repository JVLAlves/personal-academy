package main

import (
	"fmt"
	mrand "math/rand"
)

func main() {

	r1 := mrand.Int()
	r2 := mrand.Int()
	r3 := mrand.Int()
	r4 := mrand.Int()
	r5 := mrand.Int()
	rr1 := r1 * r2
	rr2 := r3 * r4
	rrt := rr1 + rr2
	rt := rrt / r5
	fmt.Printf("%d", rt)
}
