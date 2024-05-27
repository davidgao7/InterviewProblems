package main

func longestPalindrome(s string) string {
	res := ""
	longest_len := 0

	for i := 0; i < len(s); i++ {
		// check odd length palindromes
		l, r := i, i

		for l >= 0 && r < len(s) && s[l] == s[r] {

			if r-l+1 > longest_len {
				res = s[l : r+1]
				longest_len = r - l + 1
			}
			l--
			r++
		}
		// even length palindromes
		l, r = i, i+1
		for l >= 0 && r < len(s) && s[l] == s[r] {
			if r-l+1 > longest_len {
				res = s[l : r+1]
				longest_len = r - l + 1
			}
			l--
			r++
		}
	}
	return res
}

func main() {
	println(longestPalindrome("babad"))
}
