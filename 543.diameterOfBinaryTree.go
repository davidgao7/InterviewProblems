package interviewproblems

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func diameterOfBinaryTree(root *TreeNode) int {
	maxDiameter := 0
	helper(root, &maxDiameter) // pass the reference of maxDiameter
	return maxDiameter

}

func helper(root *TreeNode, maxDiameter *int) int {
	if root == nil {
		return 0
	}

	// height is disance(diameter in this case)
	leftHeight := helper(root.Left, maxDiameter)
	rightHeight := helper(root.Right, maxDiameter)

	currentNodeHeight := 1 + int(math.Max(float64(leftHeight), float64(rightHeight)))

	if *maxDiameter < leftHeight+rightHeight {
		*maxDiameter = leftHeight + rightHeight
	}

	return currentNodeHeight

}
