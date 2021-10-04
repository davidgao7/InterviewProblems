//
// Created by Tengjun Gao on 10/4/21.
//
//用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，分别完成在队列尾部插入整数和在队列头部删除整数的
//功能。(若队列中没有元素，deleteHead 操作返回 -1 )
//
//
//
// 示例 1：
//
// 输入：
//["CQueue","appendTail","deleteHead","deleteHead"]
//[[],[3],[],[]]
//输出：[null,null,3,-1]
//
//
// 示例 2：
//
// 输入：
//["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
//[[],[],[5],[2],[],[]]
//输出：[null,-1,null,null,5,2]
//
//
// 提示：
//
//
// 1 <= values <= 10000
// 最多会对 appendTail、deleteHead 进行 10000 次调用
//
// Related Topics 栈 设计 队列 👍 319 👎 0

#include <iostream>
#include <string>
#include <stack>

class CQueue {
    std::stack<int> stack1, stack2; // global

public:
    CQueue() {
        // empty stack
        while(!stack1.empty()){
            stack1.pop();
        }
        while(!stack2.empty()){
            stack2.pop();
        }
    }

    void appendTail(int value) {
        stack1.push(value);
    }

    int deleteHead() { // 相当于delete top of stack1 reverse since we store use stack1
        if(stack2.empty()){
            while (!stack1.empty()){
                stack2.push(stack1.top()); // stack2 = reverse stack 1
                stack1.pop(); // empty stack1
            }
        }
        if (stack2.empty()){
            return -1; // stack1 has nothing
        }else{
            int itemDeleted = stack2.top();
            stack2.pop(); // remove element
            return itemDeleted;
        }
    }
};

int main() {
    printf("create CQueue\n");
    CQueue *queue = new CQueue();
    printf("append 1 at end\n");
    queue->appendTail(1);
    printf("append 3 at end\n");
    queue->appendTail(3);
    printf("append 5 at end\n");
    queue->appendTail(5);
    printf("append 7 at end\n");
    queue->appendTail(7);

    printf("top of queue: (should be 1): %d\n", queue->deleteHead());
    printf("top of queue: (should be 3): %d\n", queue->deleteHead());
    printf("top of queue: (should be 5): %d\n", queue->deleteHead());
    printf("top of queue: (should be 7): %d\n", queue->deleteHead());
    printf("top of queue: (should be -1): %d\n", queue->deleteHead());
};
