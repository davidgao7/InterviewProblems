package main

import "fmt"

func reverseBits(num uint32) uint32 {
	var res uint32 = 0

	for i := 0; i < 32; i++ {
		// getting the nth bit of num
		bit := (num >> i) & 1
		// put into the 31-i th position of the res
		res = res | (bit << (31 - i))
	}

	return res
}

func main() {
	num := uint32(43261596)       // 00000010100101000001111010011100
	fmt.Println(reverseBits(num)) // 964176192  // 001110010111100000101
}
