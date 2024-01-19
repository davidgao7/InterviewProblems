/**
 <p>Given an integer array <code>nums</code>, find the <span data-keyword="subarray-nonempty">subarray</span> with the largest sum, and return <em>its sum</em>.</p>

 <p>&nbsp;</p>
 <p><strong class="example">Example 1:</strong></p>

 <pre>
 <strong>Input:</strong> nums = [-2,1,-3,4,-1,2,1,-5,4]
 <strong>Output:</strong> 6
 <strong>Explanation:</strong> The subarray [4,-1,2,1] has the largest sum 6.
 </pre>

 <p><strong class="example">Example 2:</strong></p>

 <pre>
 <strong>Input:</strong> nums = [1]
 <strong>Output:</strong> 1
 <strong>Explanation:</strong> The subarray [1] has the largest sum 1.
 </pre>

 <p><strong class="example">Example 3:</strong></p>

 <pre>
 <strong>Input:</strong> nums = [5,4,-1,7,8]
 <strong>Output:</strong> 23
 <strong>Explanation:</strong> The subarray [5,4,-1,7,8] has the largest sum 23.
 </pre>

 <p>&nbsp;</p>
 <p><strong>Constraints:</strong></p>

 <ul>
 <li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
 <li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
 </ul>

 <p>&nbsp;</p>
 <p><strong>Follow up:</strong> If you have figured out the <code>O(n)</code> solution, try coding another solution using the <strong>divide and conquer</strong> approach, which is more subtle.</p>

 <div><div>Related Topics</div><div><li>Array</li><li>Divide and Conquer</li><li>Dynamic Programming</li></div></div><br><div><li>👍 33020</li><li>👎 1382</li></div>
 */

//leetcode submit region begin(Prohibit modification and deletion)
/**
 * @param {number[]} nums
 * @return {number}
 */

var maxSubArray = function (nums) {
    // var keyword are hoisted and initialized which means they are accessible in their enclosing scope even before they are declared, however their value is undefined before the declaration statement is reached
    // let keyword are hoisted but not initialized which means they are not accessible in their enclosing scope before they are declared, however their value is undefined before the declaration statement is reached
    let result = -Infinity;
    let count = 0;
    for (let i = 0; i < nums.length; i++) {
        count += nums[i];
        if (count > result) {
            result = count;
        }
        // only reset count when the current sum is negative
        if (count < 0) {
            count = 0;
        }
    }
    return result;
};
//leetcode submit region end(Prohibit modification and deletion)
var nums = [-1];
console.log(maxSubArray(nums));