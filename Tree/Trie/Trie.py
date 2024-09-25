class TrieNode:
    def __init__(self) -> None:
        self.childern = {}
        self.endOfString = False


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()


newTrie = Trie()
