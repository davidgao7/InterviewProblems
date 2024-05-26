package main

import "fmt"

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func helper(nums []int) int {
	// one more catch: last value is adjacent to the first value
	rob1, rob2 := 0, 0 // rob1 and rob2 are adjacent

	for _, num := range nums {
		temp := max(rob1+num, rob2) // only choose one
		rob1 = rob2
		rob2 = temp
	}

	return rob2
}

func rob(nums []int) int {
	return max(
		nums[0],
		max(
			helper(nums[1:]),
			helper(nums[:len(nums)-1])), // choose the first value, choose the last value
	) // skip the first value
}

func main() {
	fmt.Println(rob([]int{1, 2, 3, 1})) // 4
}
