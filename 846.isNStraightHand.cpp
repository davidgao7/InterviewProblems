/*
 * You are given an integer array hand where hand[i] is the value written on the
ith card and an integer groupSize.

You want to rearrange the cards into groups so that each group is of size
groupSize, and card values are consecutively increasing by 1.

Return true if it's possible to rearrange the cards in this way, otherwise,
return false.

Example 1:

Input: hand = [1,2,4,2,3,5,3,4], groupSize = 4

Output: true
Explanation: The cards can be rearranged as [1,2,3,4] and [2,3,4,5].

Example 2:

Input: hand = [1,2,3,3,4,5,6,7], groupSize = 4

Output: false
Explanation: The closest we can get is [1,2,3,4] and [3,5,6,7], but the cards in
the second group are not consecutive.

Constraints:

1 <= hand.length <= 1000
0 <= hand[i] <= 1000
1 <= groupSize <= hand.length
*/

#include <iostream>
#include <map>
#include <vector>

class Solution {
public:
  bool isNStraightHand(std::vector<int> &hand, int groupSize) {
    if (hand.size() % groupSize != 0) {
      return false;
    }
    std::map<int, int> hand_map;
    for (int i = 0; i < hand.size(); i++) {
      // create a map with the count of each card
      hand_map[hand[i]]++;
    }
    for (auto it = hand_map.begin(); it != hand_map.end(); it++) {
      if (it->second > 0) { // if the count of the card is greater than 0
        for (int i = groupSize - 1; i >= 0; i--) {
          if (hand_map[it->first + i] < it->second) {
            // if the count of the card is less than the count of the current
            // card
            return false;
          }

          // reduce the count of the card
          hand_map[it->first + i] -= it->second;
        }
      }
    }
    return true;
  }
};

int main(int argc, char *argv[]) {
  std::vector<int> hand = {1, 2, 4, 2, 3, 5, 3, 4};
  int groupSize = 4;
  Solution sol;
  std::cout << sol.isNStraightHand(hand, groupSize) << std::endl; // 1
  return 0;
}
