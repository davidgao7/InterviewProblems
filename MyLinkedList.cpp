//
// Created by Tengjun Gao on 11/25/21.
//

//设计链表的实现。您可以选择使用单链表或双链表。单链表中的节点应该具有两个属性：val 和 next。val 是当前节点的值，next 是指向下一个节点的指针
///引用。如果要使用双向链表，则还需要一个属性 prev 以指示链表中的上一个节点。假设链表中的所有节点都是 0-index 的。
//
// 在链表类中实现这些功能：
//
//
// get(index)：获取链表中第 index 个节点的值。如果索引无效，则返回-1。
// addAtHead(val)：在链表的第一个元素之前添加一个值为 val 的节点。插入后，新节点将成为链表的第一个节点。
// addAtTail(val)：将值为 val 的节点追加到链表的最后一个元素。
// addAtIndex(index,val)：在链表中的第 index 个节点之前添加值为 val 的节点。如果 index 等于链表的长度，则该节点将附加
//到链表的末尾。如果 index 大于链表长度，则不会插入节点。如果index小于0，则在头部插入节点。
// deleteAtIndex(index)：如果索引 index 有效，则删除链表中的第 index 个节点。
//
//
//
//
// 示例：
//
// MyLinkedList linkedList = new MyLinkedList();
//linkedList.addAtHead(1);
//linkedList.addAtTail(3);
//linkedList.addAtIndex(1,2);   //链表变为1-> 2-> 3
//linkedList.get(1);            //返回2
//linkedList.deleteAtIndex(1);  //现在链表是1-> 3
//linkedList.get(1);            //返回3
//
//
//
//
// 提示：
//
//
// 所有val值都在 [1, 1000] 之内。
// 操作次数将在 [1, 1000] 之内。
// 请不要使用内置的 LinkedList 库。
//
// Related Topics 设计 链表 👍 308 👎 0

using namespace std;

#include <vector>
#include <string>

//leetcode submit region begin(Prohibit modification and deletion)
class MyLinkedList {
    struct Node {
        int val;
        Node *next;

        Node(int val) : val(val), next(nullptr) {}
    };

public:
    Node *head;
    Node *tail;

    int size;

    MyLinkedList() {
        head = new Node(0);
        tail = head;
        size = 0;
    }

    void printList() {
        printf("size: %d\n", getSize());
        Node *ptr = head;
        while (ptr != nullptr) {
            printf("%d->", ptr->val);
            ptr = ptr->next;
        }
        printf("\n\n");
    }

    int get(int index) {
        if (index == size - 1) return tail->val;
        if (index == 0) return head->val;

        // edge case
        if (index > size - 1 || index < 0) return -1;

        Node *ptr = head;
        while (index != 0) {
            ptr = ptr->next;
            index--;
        }
        return ptr->val;
    }

    void addAtHead(int val) {
        if (size == 0) {
            head = new Node(val);
            tail = head;
        } else {
            Node *newNode = new Node(val);
            newNode->next = head;
            head = newNode;
        }
        size++;
    }

    void addAtTail(int val) {
        if (size == 0) {
            head = new Node(val);
            tail = head;
        } else {
            tail->next = new Node(val);
            tail = tail->next;
        }
        size++;
    }

    void addAtIndex(int index, int val) {
        if (index == 0) addAtHead(val);
        else if (index == size) addAtTail(val);
        else {
            Node *ptr = head;
            for (int i = 1; i < index; ++i) {
                ptr = ptr->next;
            }
            Node *ref = new Node(val);
            ref->next = ptr->next;
            ptr->next = ref;
        }
        size++;
    }

    void deleteAtIndex(int index) {
        if (index==0){head = head->next;}
        else if (index > size-1){return;}
        else{
            Node *ptr = head;
            for (int i = 0; i < index - 1; ++i) {
                ptr = ptr->next;
            }
            ptr->next = ptr->next->next;
        }
        size--;
    }

    int getSize(){ return size;}
};

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList* obj = new MyLinkedList();
 * int param_1 = obj->get(index);
 * obj->addAtHead(val);
 * obj->addAtTail(val);
 * obj->addAtIndex(index,val);
 * obj->deleteAtIndex(index);
 */
int main() {
/*["MyLinkedList","addAtHead","deleteAtIndex"]
[[],[1],[0]]*/
    vector <string> input1{"MyLinkedList","addAtHead","addAtHead","deleteAtIndex","get","addAtIndex"};
    vector <vector<int>> input2{
            {},{1},{9},{0},{0},{1,3}
    };
    MyLinkedList *obj;
    if (input1.size() == input2.size()) {
        int s = input1.size();
        for (int i = 0; i < s; ++i) {
            if (input1[i] == "MyLinkedList") {
                obj = new MyLinkedList();
                printf("initial list:");
            }
            if (input1[i] == "addAtHead") {
                printf("insert %d addAtHead:", input2[i][0]);
                obj->addAtHead(input2[i][0]);
            } else if (input1[i] == "addAtTail") {
                printf("insert %d addAtTail:", input2[i][0]);
                obj->addAtTail(input2[i][0]);
            } else if (input1[i] == "addAtIndex") {
                printf("insert %d addAtIndex %d:", input2[i][1], input2[i][0]);
                obj->addAtIndex(input2[i][0], input2[i][1]);
            } else if (input1[i] == "deleteAtIndex") {
                printf("deleteAtIndex %d: ", input2[i][0]);
                obj->deleteAtIndex(input2[i][0]);
            } else if (input1[i] == "get") {
                printf("get position %d:", input2[i][0]);
                printf("%d\n", obj->get(input2[i][0]));
            }
            obj->printList();
        }
    } else {
        printf("input error!");
    }
}
//leetcode submit region end(Prohibit modification and deletion)

