/*
Given a string s, return true if the s can be palindrome after deleting at most one character from it.



Example 1:

Input: s = "aba"
Output: true

Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.

Example 3:

Input: s = "abc"
Output: false



Constraints:

    1 <= s.length <= 105
    s consists of lowercase English letters.

Seen this question in a real interview before?
1/5
Yes
No
Accepted
910.1K
Submissions
2.1M
Acceptance Rate
42.4%
Topics
Two Pointers
String
Greedy
Companies
0 - 3 months
Meta
119
Google
4
0 - 6 months
Amazon
4
Yandex
4
Attentive
3
TikTok
2
6 months ago
Apple
11
Adobe
6
Microsoft
5
Bloomberg
5
Yahoo
4
Whatnot
3
Walmart Labs
2
Uber
2
eBay
2*/

package main

import "fmt"

func isPalindrome(l, r int, s string) bool {
	for l < r {
		if s[l] != s[r] {
			return false
		}
		l++
		r--
	}

	return true
}

func validPalindrome(s string) bool {
	left, right := 0, len(s)-1

	for left < right {
		if s[left] != s[right] {
			// NOTE: slicing in go is same with python, end is not included
			return isPalindrome(left+1, right, s) || isPalindrome(left, right-1, s)
		}
		left++
		right--
	}

	return true
}

func main() {
	fmt.Println(validPalindrome("abca"))
}
