package main

/*
* 66. Plus One
Easy
Topics
Companies
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.



Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
Example 3:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].


Constraints:

1 <= digits.length <= 100
0 <= digits[i] <= 9
digits does not contain any leading 0's.
Accepted
2.4M
Submissions
5.2M
Acceptance Rate
45.9%
Topics
Array
Math*/

import "fmt"

func reverse2(input []int) {
	for i, j := 0, len(input)-1; i < j; i, j = i+1, j-1 {
		input[i], input[j] = input[j], input[i]
	}
}

func plusOne(digits []int) []int {
	// reverse the digits
	reverse2(digits)
	one, i := 1, 0

	for one != 0 {
		if i < len(digits) {
			if digits[i] == 9 {
				digits[i] = 0
			} else {
				digits[i]++
				one = 0
			}
		} else {
			digits = append(digits, 1)
			one = 0
		}
		i++
	}
	reverse2(digits)
	return digits
}

func plusOneFast(digits []int) []int {
	n := len(digits)

	for i := n - 1; i >= 0; i-- {
		if digits[i] < 9 {
			// add 1 to the last element
			digits[i] = digits[i] + 1
			return digits
		} else {
			// if the last element is 9, then make it 0
			digits[i] = 0
		}
	}

	// if the first element is 0, then add 1 to the first element
	if digits[0] == 0 {
		digits = append([]int{1}, digits...)
	}

	return digits
}

func main() {
	fmt.Println(plusOne([]int{1, 2, 3}))     // [1, 2, 4]
	fmt.Println(plusOneFast([]int{1, 2, 3})) // [1, 2, 4]
}
