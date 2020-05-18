//Given a string, find the length of the longest substring without repeating cha
//racters.
//
//
// Example 1:
//
//
//Input: "abcabcbb"
//Output: 3
//Explanation: The answer is "abc", with the length of 3.
//
//
//
// Example 2:
//
//
//Input: "bbbbb"
//Output: 1
//Explanation: The answer is "b", with the length of 1.
//
//
//
// Example 3:
//
//
//Input: "pwwkew"
//Output: 3
//Explanation: The answer is "wke", with the length of 3.
//             Note that the answer must be a substring, "pwke" is a subsequence
// and not a substring.
//
//
//
//
// Related Topics Hash Table Two Pointers String Sliding Window


import java.util.HashSet;

public class LongestSubstringWithoutRepeatingCharacters {
    public static void main(String[] args) {
        Solution solution = new LongestSubstringWithoutRepeatingCharacters().new Solution();
        int result = solution.lengthOfLongestSubstring("dvdf");
        System.out.println(result);
    }

    //leetcode submit region begin(Prohibit modification and deletion)
    class Solution {
        public int lengthOfLongestSubstring(String s) {
            if(s.length()==0) {
                return 0;
            }
            int start = 0;
            int end = 0;
            int max = 0;
            HashSet<Character> pattern = new HashSet<Character>();
            while (start < s.length() && end < s.length()) {
                if (!pattern.contains(s.charAt(end))) {
                    pattern.add(s.charAt(end));
                    max = Math.max(max, end - start + 1);
                    end++;
                } else {
                    start++;
                    end = start;
                    pattern.clear();
                }
            }
            return max;
        }
    }
//leetcode submit region end(Prohibit modification and deletion)
}
