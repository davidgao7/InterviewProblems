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

func removeNthFromEnd(head *ListNode, n int) *ListNode {
	// make a dummy head at the front
	dummy := &ListNode{0, head}

	// both fast and slow pointers start at the dummy head
	fast := dummy
	slow := dummy

	// index start at 0, so loop need n+1 times
	// for is while in go
	for n+1 > 0 {
		fast = fast.Next
		n -= 1
	}

	// now fast is one step ahead of target node
	// start moving slow pointer
	// once fast pointer reach the end, slow pointer is at one ahead the target node
	for fast != nil {
		fast = fast.Next
		slow = slow.Next
		// fmt.Println("slow pointer:")
		// printList(slow)
		// fmt.Println("==========")
	}

	// remove the target node
	if slow.Next != nil {
		slow.Next = slow.Next.Next
	}

	return dummy.Next
}

func main() {
	// 1 -> 2 -> 3 -> 4 -> 5 -> nil
	list := &ListNode{1, &ListNode{2, &ListNode{3, &ListNode{4, &ListNode{5, nil}}}}}
	printList(list)
	fmt.Println()
	// 1 -> 2 -> 3 -> 5 -> nil
	list = removeNthFromEnd(list, 2)
	printList(list)
	fmt.Println()
}
