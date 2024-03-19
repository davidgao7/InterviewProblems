/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func invertTree(root *TreeNode) *TreeNode {
	invert(root)
	return root
}

func invert(node *TreeNode) {
	if node == nil {
		return
	}
	// invert current layer
	node.Left, node.Right = node.Right, node.Left
	invert(node.Left)
	invert(node.Right)
}

func main() {
	root := TreeNode{
		Val:   4,
		Left:  &TreeNode{2, nil, nil},
		Right: &TreeNode{7, nil, nil},
	}
	fmt.Println(invertTree(&root))
}
