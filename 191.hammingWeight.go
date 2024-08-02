/*
* Write a function that takes the binary representation of a positive integer and returns the number of
set bits
 it has (also known as the Hamming weight).



Example 1:

Input: n = 11

Output: 3

Explanation:

The input binary string 1011 has a total of three set bits.

Example 2:

Input: n = 128

Output: 1

Explanation:

The input binary string 10000000 has a total of one set bit.

Example 3:

Input: n = 2147483645

Output: 30

Explanation:

The input binary string 1111111111111111111111111111101 has a total of thirty set bits.



Constraints:

1 <= n <= 231 - 1


Follow up: If this function is called many times, how would you optimize it?*/

package main

func hammingWeight1(n int) int {
	res := 0
	for n != 0 {
		if n%2 == 1 {
			res++
		}
		n = n >> 1
	}
	return res
}

func hammingWeight2(n int) int {
	res := 0
	for n != 0 {
		n = n & (n - 1)
		res++
	}
	return res
}

func main() {
	println(hammingWeight1(11))         // 3
	println(hammingWeight1(128))        // 1
	println(hammingWeight1(2147483645)) // 30
	println(hammingWeight2(11))         // 3
	println(hammingWeight2(128))        // 1
	println(hammingWeight2(2147483645)) // 30
}
