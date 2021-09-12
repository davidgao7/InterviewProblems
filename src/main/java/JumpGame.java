public class JumpGame {
    public boolean canJump(int[] nums) {
        // 关键：可跳的范围
        // 问题转化为：跳跃范围能不能覆盖到终点

        //base case
        if (nums.length == 1) {
            return true;
        }

        // 覆盖范围: 看看能不能覆盖到终点
        int coverRange = nums[0]; //最开始至多能走几步
        for (int i = 0; i <= coverRange; i++) {
            //i+nums[i]: 能跳的范围
            coverRange = Math.max(coverRange, i + nums[i]);
            // 如果中途到了
            if (coverRange >= nums.length - 1) {
                return true;
            }
        }
        return false;
    }
}
