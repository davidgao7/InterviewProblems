import java.util.ArrayDeque;
import java.util.Deque;

public class Calculator {
    /*
     * 整数计算器
     * input: string of number, operator:+-* three way of calculations
     * output: answer of the equation
     * space complexity: O(n) linear
     * time complexity: O(n)
     *
     * input: "(2*(3-4))*5"
     * output: -10
     * */

    public int solve(String s) {
        return calculate(s);
    }

    public int calculate(String s) {
        s = s.trim();
        Deque<Integer> stack = new ArrayDeque<>(); // hold 16 element initial
        int number = 0;
        char sign = '+';
        char[] charArray = s.toCharArray();

        for (int i = 0, n = charArray.length; i < n; i++) {
            char c = charArray[i]; // position i
            if (c == ' ') { // 防止trim没用
                continue;
            }
            if (Character.isDigit(c)) {
                number = number * 10 + (c - '0'); // char - '0': to get the real number val of char
            }
            if (c == '(') {
                int j = i + 1; // next from current position
                int counterPartition = 1;
                while (counterPartition > 0) {
                    if (charArray[j] == '(') {
                        counterPartition++; // level of parentheses
                    }
                    if (charArray[j] == ')') {
                        counterPartition--;
                    }
                    j++;
                }
                number = calculate(s.substring(i + 1, j - 1)); // parenthese from start to end which needs to calculate
                i = j - 1; // move ptr after parenthese which we've calculated
            }
            if (!Character.isDigit(c) || i == n - 1) { // n = s.length
                if (sign == '+') {
                    stack.push(number);
                } else if (sign == '-') {
                    stack.push(-1 * number);
                } else if (sign == '*') {
                    stack.push(stack.pop() * number);
                } else if (sign == '/') {
                    stack.push(stack.pop() / number);
                }
                number = 0;
                sign = c;
            }
        }
        int ans = 0;
        while (!stack.isEmpty()) {
            ans += stack.pop();
        }
        return ans;
    }

    public static void main(String args[]) {
        Calculator calculator = new Calculator();
        String input = "3+ (2- 3)*4-1 / (4+5) -0+4";
        int answer = calculator.calculate(input);
        System.out.println("input equation: " + input);
        System.out.println("answer of the equation: " + answer + "\n");
    }
}
