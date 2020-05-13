import java.io.IOException;

public class JumpingCloud {
    static int jumpingOnClouds(int[] c) {
        return minJump(0, c, 0);
    }

    private static boolean canJump(int[] c, int next) {
        return next < c.length && c[next] == 0;
    }

    private static int minJump(int currentPosition, int[] array, int jumps) {

        if (!canJump(array, currentPosition)) {
            return Integer.MAX_VALUE;
        } else if (currentPosition == array.length - 1) {
            return jumps;
        } else if (currentPosition >= array.length) {
            return Integer.MAX_VALUE;
        }
        return Math.min(minJump(currentPosition + 1, array, jumps + 1),
                minJump(currentPosition + 2, array, jumps + 1));
    }


    public static void main(String[] args) throws IOException {
        int[] c = {0, 0, 0, 0, 1, 0, 0};
        int result = jumpingOnClouds(c);
        System.out.println(result);
    }
}
