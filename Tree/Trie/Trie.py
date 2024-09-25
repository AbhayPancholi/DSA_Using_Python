class TrieNode:
    def __init__(self) -> None:
        self.childern = {}
        self.endOfString = False


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insertString(self, word):
        current = self.root
        for i in word:
            ch = i
            node = current.childern.get(ch)
            if node == None:
                node = TrieNode()
                current.childern.update({ch: node})
            current = node
        current.endOfString = True
        print("successfully inserted")


newTrie = Trie()
newTrie.insertString("APP")
newTrie.insertString("APPL")
