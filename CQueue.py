# 用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，分别完成在队列尾部插入整数和在队列头部删除整数的
# 功能。(若队列中没有元素，deleteHead 操作返回 -1 )
#
#
#
#  示例 1：
#
#  输入：
# ["CQueue","appendTail","deleteHead","deleteHead"]
# [[],[3],[],[]]
# 输出：[null,null,3,-1]
#
#
#  示例 2：
#
#  输入：
# ["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
# [[],[],[5],[2],[],[]]
# 输出：[null,-1,null,null,5,2]
#
#
#  提示：
#
#
#  1 <= values <= 10000
#  最多会对 appendTail、deleteHead 进行 10000 次调用
#
#  Related Topics 栈 设计 队列
#  👍 270 👎 0
"""
闲话：再多说一些代码开发上的习惯问题，在工业级别代码开发中，最忌讳的就是 实现一个类似的函数，直接把代码粘过来改一改就完事了。

这样的项目代码会越来越乱，一定要懂得复用，功能相近的函数要抽象出来，不要大量的复制粘贴，很容易出问题！（踩过坑的人自然懂）

工作中如果发现某一个功能自己要经常用，同事们可能也会用到，自己就花点时间把这个功能抽象成一个好用的函数或者工具类，不仅自己方便，也方面了同事们。

同事们就会逐渐认可你的工作态度和工作能力，自己的口碑都是这么一点一点积累起来的！在同事圈里口碑起来了之后，你就发现自己走上了一个正循环，以后的升职加薪才少不了你！哈哈哈

"""


# leetcode submit region begin(Prohibit modification and deletion)
class CQueue:

    def __init__(self):
        self.stack = []

    def appendTail(self, value: int) -> None:
        self.stack.append(value)

    def deleteHead(self) -> int:
        if not self.stack:
            return -1
        head = self.stack[0]
        self.stack = self.stack[1:]
        return head


# Your CQueue object will be instantiated and called as such:
obj = CQueue()
obj.appendTail(1)  # [1]
obj.appendTail(2)  # [1,2]
obj.appendTail(3)  # [1,2]
param_2 = obj.deleteHead()  # [2]
print(param_2)
# leetcode submit region end(Prohibit modification and deletion)
