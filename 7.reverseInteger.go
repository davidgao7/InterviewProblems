package main

import "fmt"

func reverse(x int) int {
	res := 0
	MAX := 2147483647  // Maximum int32
	MIN := -2147483648 // Minimum int32

	for x != 0 {
		// when res is too large or too small than the MAX and MIN, return 0
		if res > MAX/10 || res < MIN/10 {
			return 0
		}
		res = res*10 + x%10 // add the last digit of x to res
		x /= 10
	}

	return res
}

func main() {
	fmt.Println(reverse(123)) // 321
}
