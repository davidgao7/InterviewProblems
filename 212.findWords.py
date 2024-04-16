# Given an m x n board of characters and a list of strings words, return all words on the board.
#
# Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.
#
#
#
# Example 1:
#
#
# Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
# Output: ["eat","oath"]
# Example 2:
#
#
# Input: board = [["a","b"],["c","d"]], words = ["abcb"]
# Output: []
#
#
# Constraints:
#
# m == board.length
# n == board[i].length
# 1 <= m, n <= 12
# board[i][j] is a lowercase English letter.
# 1 <= words.length <= 3 * 104
# 1 <= words[i].length <= 10
# words[i] consists of lowercase English letters.
# All the strings of words are unique.
# Accepted
# 646.8K
# Submissions
# 1.8M
# Acceptance Rate
# 36.3%
# Topics
# Companies
# Hint 1
# Hint 2
# Similar Questions
# Discussion (76)
#
# Choose a type
#
#
# Read more
#
#
# Read more
#
# Copyright ©️ 2024 LeetCode All rights reserved
#
# 9.3K
#
#
# 76

from typing import List


# implement a trie node class
class TrieNode:
    def __init__(self):
        self.children = {}  # struct the children set
        self.isWord = False
        self.refs = 0

    def addword(self, word):
        # deconstruct the word to a tree branch
        cur = self  # better name for easy understand
        cur.refs += 1  # for current node's character
        for c in word:
            if c not in cur.children:
                # for each choice/path, you will have a whole new Trie
                cur.children[c] = TrieNode()

            # now current character is fixed, current point to next position, wait for next
            # chracter choice
            cur = cur.children[c]
            # update current record word length
            cur.refs += 1

        # append/find the entire character sequence(word), return isWord True
        cur.isWord = True

    def removeWord(self, word):
        cur = self
        cur.refs -= 1

        for c in word:
            if c in cur.children:
                cur = cur.children[c]
                cur.refs -= 1


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for word in words:
            root.addword(word)

        ROWS, COLS = len(board), len(board[0])
        res, visited = set(), set()

        def dfs(r, c, node, word):
            if (
                #  position is not right
                r not in range(ROWS)
                or c < 0
                or r == COLS
                or r == ROWS
                # has visited the position when searching a word
                or (r, c) in visited
                # cannot move to this character from current position
                or board[r][c] not in node.children
            ):
                # cannot find this word
                return

            # else we can add this route
            visited.add((r, c))
            # move towards to this route 1
            node = node.children[board[r][c]]
            # undate the word state
            word += board[r][c]

            # if we reach the word end, we can finally confirm this word and add to the result
            if node.isWord:
                res.add(word)

            # do dfs on up left right up down possible route
            dfs(r - 1, c, node, word)  # if go up
            dfs(r + 1, c, node, word)  # if go down
            dfs(r, c - 1, node, word)  # if go left
            dfs(r, c + 1, node, word)  # if go right

            # backtrack the visited position
            # finish this route, but cannot find word, remove it
            visited.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                # for each position, try to find a word
                dfs(r, c, root, "")

        return list(res)
