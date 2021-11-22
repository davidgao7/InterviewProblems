//
// Created by Tengjun Gao on 11/21/21.
//
//给你一个正整数 n ，生成一个包含 1 到 n² 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。
//
//
//
// 示例 1：
//
//
//输入：n = 3
//输出：[[1,2,3],[8,9,4],[7,6,5]]
//
//
// 示例 2：
//
//
//输入：n = 1
//输出：[[1]]
//
//
//
//
// 提示：
//
//
// 1 <= n <= 20
//
// Related Topics 数组 矩阵 模拟 👍 527 👎 0
#include <vector>
using namespace std;
//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        vector<vector<int>> answer(n , vector<int>(n,0)); // empty matrix with 0 filled
        //纯考代码熟练度
        int startx = 0, starty=0; // 定义每循环一个圈的起始位置
        int loop = n/2; // 每个圈循环几次， n=3, loop=1， 只循环一圈，矩阵中间的值需要单独处理
        int mid = n/2; // 矩阵中间的位置， n=3, 中间的位置就是(1,1), n为5， 中间位置（2，2）
        int count = 1; // 用来给矩阵中每一个空格赋值
        int offset = 1; // 每一圈循环，需要控制每一条边遍历的长度
        int i,j;

        while(loop--){
            i = startx;
            j = starty;

            // 下面4个 for 就是模拟转了一圈

            // 模拟填充上行从左到右 (左闭右开）
            for(j = starty; j<starty+n-offset; j++){
                answer[startx][j] = count++;
            }

            // 模拟填充右列从上到下（左闭右开）
            for (i = startx; i<startx+n-offset;i++) {
                answer[i][j] = count++;
            }

            // 模拟填充下行从右到左（左闭右开）
            for(;j>starty; j--){
                answer[i][j] = count++;
            }

            // 模拟填充左列从下到上（左闭右开）
            for(; i>startx;i--){
                answer[i][j] = count++;
            }

            // 第二圈开始的时候， 起始位置要各自加1， eg 第一圈起始位置（0，0），第二圈起始位置为（1，1）
            startx++;
            starty++;

            // offset 控制每一圈每一条边遍历的长度
            offset += 2;

        }

        // 如果n为奇数， 需要单独给矩阵最中间的位置赋值
        if (n % 2){
            answer[mid][mid] = count;
        }

        return answer;
    }
};
//leetcode submit region end(Prohibit modification and deletion)
int main(){
Solution *s = new Solution();
vector<vector<int>> answer = s->generateMatrix(3);
}
