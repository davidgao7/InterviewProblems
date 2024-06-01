package main

import (
	"fmt"
)

func countSubstrings(s string) int {
	res := 0
	for i := 0; i < len(s); i++ {
		l := i
		r := i
		for l >= 0 && r < len(s) && s[l] == s[r] {
			res++
			l--
			r++
		}

		l = i
		r = i + 1
		for l >= 0 && r < len(s) && s[l] == s[r] {
			res++
			l--
			r++
		}
	}
	return res
}

func main() {
	fmt.Println(countSubstrings("abc"))
}
