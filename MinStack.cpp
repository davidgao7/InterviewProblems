//
// Created by Tengjun Gao on 10/4/21.
//
//定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。
//
//
//
// 示例:
//
// MinStack minStack = new MinStack();
//minStack.push(-2);
//minStack.push(0);
//minStack.push(-3);
//minStack.min();   --> 返回 -3.
//minStack.pop();
//minStack.top();      --> 返回 0.
//minStack.min();   --> 返回 -2.
//
//
//
//
// 提示：
//
//
// 各函数的调用总次数不超过 20000 次
//
//
//
//
// 注意：本题与主站 155 题相同：https://leetcode-cn.com/problems/min-stack/
// Related Topics 栈 设计 👍 197 👎 0
#include <iostream>
#include <string>
#include <stack>
#include <stdio.h>
#include <vector>
using namespace std;

//leetcode submit region begin(Prohibit modification and deletion)
class MinStack {
    std::stack<int> stack;
    std::stack<int> minimums;
    int MIN = INT_MAX;

public:
    /** initialize your data structure here. */
    MinStack() {
        minimums.push(INT_MAX);
    }

    void push(int x) {
        stack.push(x);
        minimums.push(std::min(minimums.top(), x)); // update min
    }

    void pop() {
        stack.pop();
        minimums.pop();
    }

    int top() {
        return stack.top();
    }

    int min() {
        return minimums.top();
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(x);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->min();
 */
//leetcode submit region end(Prohibit modification and deletion)


int main() {
    MinStack *minStack = new MinStack();
    minStack->push(-2);
    minStack->push(0);
    minStack->push(-3);
    minStack->push(-4);
    int min = minStack->min();
    printf("the minimum in stack is %d --> return -4\n", min);
    minStack->pop();
    int top = minStack->top();
    printf("the top of the stack is %d --> return -3\n", top);
    int min2 = minStack->min();
    printf("the minimum in current stack is %d --> return -3\n", min2);
};