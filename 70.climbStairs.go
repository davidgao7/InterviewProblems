/*
*You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?



Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

* */

package main

import (
	"fmt"
)

func climbStairs(n int) int {
	// using dp
	df := make([]int, n+1)
	df[0] = 1 // start with 1 step, but we need to define 0 step
	df[1] = 1

	for i := 2; i <= n; i++ {
		// current ways of step = ways of previous step + ways of previous to previous step
		df[i] = df[i-1] + df[i-2]
	}
	return df[n] // return the last value
}

func climbStairsReverse(n int) int {
	// using dp
	df := make([]int, n+1)
	df[n] = 1   // there are 1 way from end to end
	df[n-1] = 1 // there are 1 way from end-1 to end
	for i := n - 2; i >= 0; i-- {
		// current ways of step = ways of previous step + ways of previous to previous step
		df[i] = df[i+1] + df[i+2]
	}
	return df[0] // return the last value
}

func main() {
	n := 3
	fmt.Println(climbStairs(n))

	n = 2
	fmt.Println(climbStairs(n))
}
