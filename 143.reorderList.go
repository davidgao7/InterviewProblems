// You are given the head of a singly linked-list. The list can be represented as:
//
// L0 → L1 → … → Ln - 1 → Ln
// Reorder the list to be on the following form:
//
// L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
// You may not modify the values in the list's nodes. Only nodes themselves may be changed.
//
//
//
// Example 1:
//
//
// Input: head = [1,2,3,4]
// Output: [1,4,2,3]
// Example 2:
//
//
// Input: head = [1,2,3,4,5]
// Output: [1,5,2,4,3]
//
//
// Constraints:
//
// The number of nodes in the list is in the range [1, 5 * 104].
// 1 <= Node.val <= 1000

package main

// Definition for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

func reorderList(head *ListNode) {
	slow := head
	fast := head
	for fast != nil && fast.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next
	}
	secondList := slow.Next
	slow.Next = nil
	reversedSecondList := reverse(secondList)
	a := head
	b := reversedSecondList
	for b != nil {
		aNext := a.Next
		bNext := b.Next
		a.Next = b
		b.Next = aNext
		a = aNext
		b = bNext
	}
}

func reverse(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}
	newTail := head
	it := head.Next
	previous := head
	for it != nil {
		itNext := it.Next
		it.Next = previous
		previous = it
		it = itNext
	}
	newTail.Next = nil
	return previous
}

func printList(head *ListNode) {
	p := head
	for p != nil {
		print(p.Val)
		p = p.Next
	}
	println("")
}

func main() {
	l1 := &ListNode{Val: 1, Next: &ListNode{Val: 2, Next: &ListNode{Val: 3, Next: &ListNode{Val: 4, Next: nil}}}}
	printList(l1)
	reorderList(l1)
	printList(l1)

	println("")

	l2 := &ListNode{Val: 1, Next: &ListNode{Val: 2, Next: &ListNode{Val: 3, Next: &ListNode{Val: 4, Next: &ListNode{Val: 5, Next: nil}}}}}
	printList(l2)
	reorderList(l2)
	printList(l2)
}
