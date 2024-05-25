package main

import "fmt"

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func rob(nums []int) int {
	rob1, rob2 := 0, 0

	for _, num := range nums {
		temp := max(rob1+num, rob2)
		rob1 = rob2
		rob2 = temp
	}

	return rob2
}

func main() {
	fmt.Println(rob([]int{1, 2, 3, 1})) // 4
}
