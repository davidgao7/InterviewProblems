//You are given two non-empty linked lists representing two non-negative integer
//s. The digits are stored in reverse order and each of their nodes contain a sing
//le digit. Add the two numbers and return it as a linked list.
//
// You may assume the two numbers do not contain any leading zero, except the nu
//mber 0 itself.
//
// Example:
//
//
//Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
//Output: 7 -> 0 -> 8
//Explanation: 342 + 465 = 807.
//
// Related Topics Linked List Math


public class AddTwoNumbers {
    public static void main(String[] args) {
        Solution solution = new AddTwoNumbers().new Solution();
        //Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
        //Output: 7 -> 0 -> 8
        //Explanation: 342 + 465 = 807.
        ListNode l1 = new ListNode(2, new ListNode(5, null));
        ListNode l2 = new ListNode(5, new ListNode(5, null));
        ListNode l3 = solution.addTwoNumbers(l1, l2);
        while (l3 != null) {
            System.out.println(l3.val);
            l3 = l3.next;
        }
    }
    //leetcode submit region begin(Prohibit modification and deletion)


    public static class ListNode {
        int val;
        ListNode next;

        ListNode() {
        }

        ListNode(int val) {
            this.val = val;
        }

        ListNode(int val, ListNode next) {
            this.val = val;
            this.next = next;
        }
    }

    class Solution {
        private static final int overflow = 10;

        public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
            //only care the current digit
            if (l1 == null && l2 == null) {
                return null;
            }
            if (l1 == null || l2 == null) {
                return l1 == null ? l2 : l1;
            }
            if (l1.val + l2.val >= overflow) {
                int next = l1.val + l2.val - overflow;
                l1.val = next;
                l1.next = addTwoNumbers(addTwoNumbers(l1.next, new ListNode(1)), l2.next);
            } else {
                l1.val += l2.val;
                l1.next= addTwoNumbers(l1.next,l2.next);
            }
            return l1;
        }
    }
//leetcode submit region end(Prohibit modification and deletion)

}
