// You are given the heads of two sorted linked lists list1 and list2.
//
// Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
//
// Return the head of the merged linked list.
//
//
//
// Example 1:
//
//
// Input: list1 = [1,2,4], list2 = [1,3,4]
// Output: [1,1,2,3,4,4]
// Example 2:
//
// Input: list1 = [], list2 = []
// Output: []
// Example 3:
//
// Input: list1 = [], list2 = [0]
// Output: [0]
//
//
// Constraints:
//
// The number of nodes in both lists is in the range [0, 50].
// -100 <= Node.Val <= 100
// Both list1 and list2 are sorted in non-decreasing order.

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func printList(l *ListNode) {
	p := l

	for p != nil {
		fmt.Printf("%d -> ", p.Val)
		p = p.Next
	}
}

func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
	// nil is null in go
	// compare the length entire the shorter list ran out of elements
	// then append the rest of the longer list
	// time complexity: O(n + m) where n and m are the length of the two lists
	// space complexity: O(1) since we are not using any extra space

	result := &ListNode{} // := declare + assignment where = is just assignment
	dummy_ptr := result

	// & goes in front of a variable when you want to get that variable's memory address.
	// * goes in front of a pointer variable when you want to get the Value that the pointer
	// is pointing at.
	// ok similar to cpp

	for list1 != nil && list2 != nil {
		// compare the Value of the two lists
		if list1.Val <= list2.Val {
			dummy_ptr.Next = list1
			list1 = list1.Next // after setting up next value, need to update assigned list right away
		} else {
			dummy_ptr.Next = list2
			list2 = list2.Next
		}

		dummy_ptr = dummy_ptr.Next
	}

	// append the rest of the longer list
	if list1 != nil {
		dummy_ptr.Next = list1
		dummy_ptr = dummy_ptr.Next
	}
	if list2 != nil {
		dummy_ptr.Next = list2
		dummy_ptr = dummy_ptr.Next
	}

	return result.Next // get rid of nill fist node
}

func main() {
	list1 := &ListNode{Val: 1, Next: &ListNode{Val: 2, Next: &ListNode{Val: 4, Next: nil}}}
	list2 := &ListNode{Val: 1, Next: &ListNode{Val: 3, Next: &ListNode{Val: 4, Next: nil}}}
	res := mergeTwoLists(list1, list2)
	printList(res)
}
