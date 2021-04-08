class TrieNode:
    def __init__(self):
        self.isWord = False
        self.children = {}


class WordDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                charNode = TrieNode()
                node.children[char] = charNode
                node = charNode
        node.isWord = True

    def search(self, word: str) -> bool:
        pass


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
