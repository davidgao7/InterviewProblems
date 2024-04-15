# Design a data structure that supports adding new words and finding if a string matches any previously added string.

# Implement the WordDictionary class:
#
# WordDictionary() Initializes the object.
# void addWord(word) Adds word to the data structure, it can be matched later.
# bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
#
#
# Example:
#
# Input
# ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
# [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
# Output
# [null,null,null,null,false,true,true,true]
#
# Explanation
# WordDictionary wordDictionary = new WordDictionary();
# wordDictionary.addWord("bad");
# wordDictionary.addWord("dad");
# wordDictionary.addWord("mad");
# wordDictionary.search("pad"); // return False
# wordDictionary.search("bad"); // return True
# wordDictionary.search(".ad"); // return True
# wordDictionary.search("b.."); // return True
#
#
# Constraints:
#
# 1 <= word.length <= 25
# word in addWord consists of lowercase English letters.
# word in search consist of '.' or lowercase English letters.
# There will be at most 2 dots in word for search queries.
# At most 104 calls will be made to addWord and search.


# def a trieNode
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False


class WordDictionary:

    def __init__(self):
        # declare empty trieNode
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                # insert the character to the trieNode
                cur.children[c] = TrieNode()

            # move cur to the node
            cur = cur.children[c]
        cur.word = True  # we have create the character

    def search(self, word: str) -> bool:

        def dfs(j, root):
            # NOTE: recursion
            cur = root

            for i in range(j, len(word)):
                c = word[i]

                # c might be a dot
                # matched any 26 characters
                # need backtracking 26 possibilities
                if c == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child):  # skip the dot
                            return True
                    return False

                else:
                    # normal character
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]

            return cur.word

        return dfs(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
