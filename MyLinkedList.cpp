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
private:
    vector<int> list;
public:
    MyLinkedList() {
    }
    void printList(){
        for (int i = 0; i < list.size(); ++i) {
            printf("%d ", list[i]);
        }
        printf("\n");
    }

    int get(int index) {
        return list[index];
    }

    void addAtHead(int val) {
        auto it = list.begin();
        list.insert(it, val);
    }

    void addAtTail(int val) {
        list.push_back(val);
    }

    void addAtIndex(int index, int val) {
        auto it = list.begin();
        while (index != 0) {
            it++;
            index--;
        }
        list.insert(it, val);
    }

    void deleteAtIndex(int index) {
        vector<int> con;

        for (int i = 0; i < list.size(); ++i) {
            if (i != index){
                con.push_back(list[i]);
            }
        }

        for (int i = 0; i < con.size(); ++i) {
            list[i] = con[i];
        }

        list.pop_back();
    }
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
    vector<string>input1{"MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"};
    vector<vector<int>>input2{{},{1},{3},{1,2},{1},{1},{1}};
    MyLinkedList* obj;
    if (input1.size() == input2.size()){
        int s = input1.size();
        for (int i = 0; i < s; ++i) {
            if (i==0){
                obj = new MyLinkedList();
            }
            if (input1[i]=="addAtHead"){
                printf("addAtHead:");
                obj->addAtHead(input2[i][0]);
            }else if(input1[i]=="addAtTail"){
                printf("addAtTail:");
                obj->addAtTail(input2[i][0]);
            }else if(input1[i]=="addAtIndex"){
                printf("addAtIndex %d:", input2[i][1]);
                obj->addAtIndex(input2[i][0],input2[i][1]);
            }else if(input1[i]=="deleteAtIndex"){
                printf("deleteAtIndex %d: ", input2[i][0]);
                obj->deleteAtIndex(input2[i][0]);
            }else if(input1[i]=="get"){
                printf("get position %d:", input2[i][0]);
                printf("%d\n",obj->get(input2[i][0]));
            }
            obj->printList();
        }
    }else{
        printf("input error!");
    }
}
//leetcode submit region end(Prohibit modification and deletion)

