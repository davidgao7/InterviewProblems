/*
* You are given a stream of points on the X-Y plane. Design an algorithm that:

Adds new points from the stream into a data structure. Duplicate points are
allowed and should be treated as different points.
Given a query point, counts the number of ways to choose three points from
the data structure such that the three points and the query point form an
axis-aligned square with positive area.
An axis-aligned square is a square whose edges are all the same length and
are either parallel or perpendicular to the x-axis and y-axis.

Implement the DetectSquares class:

DetectSquares() Initializes the object with an empty data structure.
void add(int[] point) Adds a new point point = [x, y] to the data structure.
int count(int[] point) Counts the number of ways to form axis-aligned squares
with point point = [x, y] as described above.
*/

package main

import "fmt"

type DetectSquares struct {
	Map map[int]map[int]int
}

func Constructor() DetectSquares {
	return DetectSquares{Map: make(map[int]map[int]int)}
}

func (this *DetectSquares) Add(point []int) {
	if _, ok := this.Map[point[0]]; !ok {
		this.Map[point[0]] = make(map[int]int)
	}
	this.Map[point[0]][point[1]]++
}

func (this *DetectSquares) Count(point []int) int {
	res, px, py := 0, point[0], point[1]

	for k := range this.Map[px] {
		if py == k {
			continue
		}
		dist := py - k
		if py-k < 0 {
			dist = k - py
		}
		res += this.Map[px][k] * (this.Map[px-dist][k]*this.Map[px-dist][py] + this.Map[px+dist][py]*this.Map[px+dist][k])
	}

	return res
}

/**
 * Your DetectSquares object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Add(point);
 * param_2 := obj.Count(point);
 */

func main() {
	detectSquares := Constructor()
	detectSquares.Add([]int{3, 10})
	detectSquares.Add([]int{11, 2})
	detectSquares.Add([]int{3, 2})
	fmt.Println(detectSquares.Count([]int{11, 10})) // return 1. You can choose:
	//   - The first, second, and third points
	detectSquares.Count([]int{14, 8})               // return 0. The query point cannot form a square with any points in the data structure.
	detectSquares.Add([]int{11, 2})                 // Adding duplicate points is allowed.
	fmt.Println(detectSquares.Count([]int{11, 10})) // return 2. You can choose:
	//   - The first, second, and third points
	//   - The first, third, and fourth points
}
