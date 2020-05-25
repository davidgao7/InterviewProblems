//There are two sorted arrays nums1 and nums2 of size m and n respectively.
//
// Find the median of the two sorted arrays. The overall run time complexity sho
//uld be O(log (m+n)).==>binary search
//
// You may assume nums1 and nums2 cannot be both empty.
//
// Example 1:
//
//
//nums1 = [1, 3]
//nums2 = [2]
//
//The median is 2.0
//
//
// Example 2:
//
//
//nums1 = [1, 2]
//nums2 = [3, 4]
//
//The median is (2 + 3)/2 = 2.5
//
// Related Topics Array Binary Search Divide and Conquer


public class MedianOfTwoSortedArrays {
    public static void main(String[] args) {
        Solution solution = new MedianOfTwoSortedArrays().new Solution();
        System.out.println(solution.findMedianSortedArrays(new int[]{3,5,8,9}, new int[]{1, 2, 7, 10, 11, 12}));
    }

    /**
     * @formatter:off
    index: 0   1   2   3   4   5
               L1 R1
    num1 : 3   5 | 8   9
                   L2  R2
    num2 : 1   2   7 | 10  11  12
    num3 :1 2 3 5 7 | 8 9 10 11 12

    L1<=R2,
    L2<=R1 done

    L1>R2 <<1
    L2>R1 >>1
     @formatter:on
     **/

    class Solution {
        public double findMedianSortedArrays(int[] A, int[] B) {
            int m = A.length;
            int n = B.length;
            if (m > n) { // to ensure m<=n
                return findMedianSortedArrays(B, A);
            }
            int iMin = 0, iMax = m, halfLen = (m + n + 1) / 2;
            while (iMin <= iMax) {//scan through shorter array
                int i = (iMin + iMax) / 2;//shorter array midpt+1
                int j = halfLen - i;//second half start
                //i in A[]
                // j in B[]
                if (i < iMax && B[j - 1] > A[i]) {
                    iMin = i + 1; // i is too small
                } else if (i > iMin && A[i - 1] > B[j]) {
                    iMax = i - 1; // i is too big
                } else { // i is perfect
                    int maxLeft = 0;
                    if (i == 0) {//A[] is empty,j is half of B by 1 more position
                        maxLeft = B[j - 1];
                    } else if (j == 0) {//B[] is empty, int 0.5 = 0, maxLeft is near mid of A
                        maxLeft = A[i - 1];
                    } else {
                        maxLeft = Math.max(A[i - 1], B[j - 1]);
                    }
                    if ((m + n) % 2 == 1) {
                        return maxLeft;//规律
                    }

                    int minRight = 0;
                    if (i == m) {
                        minRight = B[j];//correspond to maxleft = B[j-1]
                    } else if (j == n) {
                        minRight = A[i];//correspond to maxleft = A[i-1]
                    } else {
                        minRight = Math.min(B[j], A[i]);//ptr right find min of the two numbers
                    }

                    return (maxLeft + minRight) / 2.0;
                }
            }
            return 0.0;
        }
    }

//leetcode submit region end(Prohibit modification and deletion)

}
