class Solution {
public:
  int hammingWeight(int n) {
    int count = 0;
    while (n) {
      n &= n - 1;
      count++;
    }
    return count;
  }

  int hammingWeight2(int n) {
    int count = 0;
    while (n) {
      count += n & 1;
      n >>= 1;
    }
    return count;
  }
};
