# A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.
#
# Implement the Trie class:
#
# Trie() Initializes the trie object.
# void insert(String word) Inserts the string word into the trie.
# boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
# boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
#
#
# Example 1:
#
# Input
# ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
# [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
# Output
# [null, null, true, false, true, null, true]
#
# Explanation
# Trie trie = new Trie();
# trie.insert("apple");
# trie.search("apple");   // return True
# trie.search("app");     // return False
# trie.startsWith("app"); // return True
# trie.insert("app");
# trie.search("app");     // return True
#
#
# Constraints:
#
# 1 <= word.length, prefix.length <= 2000
# word and prefix consist only of lowercase English letters.
# At most 3 * 104 calls in total will be made to insert, search, and startsWith.
class TrieNode:
    def __init__(self):
        self.children = {}  # 26 letters
        self.endOfWord = False  # mark if this node is the end of a word


class Trie:
    """
    prefix tree, searching string efficiently
    """

    def __init__(self):
        self.root = TrieNode()  # create an empty tree

    def insert(self, word: str) -> None:
        # start at the root
        cur = self.root
        # check if the character exits
        for c in word:
            if c not in cur.children:
                # if the character does not exist in tree, create a new node for it
                # this is the only time we create a new node
                cur.children[c] = TrieNode()

            # point current node to the next node
            cur = cur.children[c]

        # after loop, cur will point to the end of the word
        # mark the end of the word to true
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        # searching start from the root
        cur = self.root

        # dfs to search if the word exists
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]

        return True


# Your Trie object will be instantiated and called as such:
if __name__ == "__main__":
    word = "apple"
    prefix = "app"
    obj = Trie()
    obj.insert(word)
    param_2 = obj.search(word)
    param_3 = obj.startsWith(prefix)
