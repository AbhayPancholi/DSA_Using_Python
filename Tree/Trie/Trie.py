class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.endOfString = False


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insertString(self, word):
        current = self.root
        for i in word:
            ch = i
            node = current.children.get(ch)
            if node == None:
                node = TrieNode()
                current.children.update({ch: node})
            current = node
        current.endOfString = True
        print("successfully inserted")

    def searchString(self, word):
        current = self.root
        for i in word:
            node = current.children.get(i)
            if node == None:
                return False
            current = node
        if current.endOfString == True:
            return True
        return False


def deleteString(root, word, index):
    ch = word[index]
    currentNode = root.children.get(ch)
    canThisNodeBeDeleted = False

    if len(currentNode.children) > 1:
        deleteString(root, word, index + 1)
        return False

    if index == len(word) - 1:
        if len(currentNode.children) >= 1:
            currentNode.endOfString = False
            return False
        else:
            root.children.pop(ch)
            return True

    if currentNode.endOfString == True:
        deleteString(currentNode, word, index + 1)
        return False
    canThisNodeBeDeleted = deleteString(currentNode, word, index + 1)

    if canThisNodeBeDeleted == True:
        root.children.pop(ch)
        return True
    else:
        return False


newTrie = Trie()
newTrie.insertString("APP")
newTrie.insertString("APPL")
deleteString(newTrie.root, "APP", 0)
print(newTrie.searchString("APP"))
