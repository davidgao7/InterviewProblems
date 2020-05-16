//Given an array of integers, return indices of the two numbers such that they a
//dd up to a specific target.
//
// You may assume that each input would have exactly one solution, and you may n
//ot use the same element twice.
//
// Example:
//
//
//Given nums = [2, 7, 11, 15], target = 9,
//
//Because nums[0] + nums[1] = 2 + 7 = 9,
//return [0, 1].
//
// Related Topics Array Hash Table

import java.util.Arrays;
import java.util.HashMap;

public class TwoSum {
    public static void main(String[] args) {
        Solution solution = new TwoSum().new Solution();
        int[] input = {3, 3, 5, 8, 7};
        int target = 15;
        int[] ouput = solution.twoSum(input, target);
        System.out.print(Arrays.toString(ouput));
    }

    //leetcode submit region begin(Prohibit modification and deletion)
    class Solution {
        public int[] twoSum(int[] nums, int target) {
            HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
            //mark index
            for (int i = 0; i < nums.length; i++) {
                map.put(nums[i], i);
            }
            //if value found not itself and not null
            for (int i = 0; i < nums.length; i++) {
                if (map.get(target - nums[i]) != null && map.get(target - nums[i]) != i) {
                    return new int[]{i, map.get(target - nums[i])};
                }
            }
            return null;
        }
    }
}
//leetcode submit region end(Prohibit modification and deletion)

