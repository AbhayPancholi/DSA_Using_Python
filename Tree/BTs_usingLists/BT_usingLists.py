class BinaryTree:
    def __init__(self, size) -> None:
        self.customList = size * [None]
        self.maxSize = size
        self.lastUsedIndex = 0

    def insertNode(self, value):
        if self.lastUsedIndex + 1 == self.maxSize:
            return "The tree is full"
        self.customList[self.lastUsedIndex + 1] = value
        self.lastUsedIndex += 1
        return "Node inserted successfully"

    def searchNode(self, nodeValue):
        """This method is implemented using the level order traversal technique
        that is demonstrated below"""
        for i in range(len(self.customList)):
            if self.customList[i] == nodeValue:
                return "Success"
        return "Node not found"

    def preOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        print(self.customList[index])
        self.preOrderTraversal(index * 2)
        self.preOrderTraversal(index * 2 + 1)

    def inOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        self.inOrderTraversal(index * 2)
        print(self.customList[index])
        self.inOrderTraversal(index * 2 + 1)

    def postOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        self.postOrderTraversal(index * 2)
        self.postOrderTraversal(index * 2 + 1)
        print(self.customList[index])


newBT = BinaryTree(8)
print(newBT.insertNode("Drinks"))
print(newBT.insertNode("Hot"))
print(newBT.insertNode("Cold"))
print(newBT.insertNode("Tea"))
print(newBT.insertNode("Coffee"))
print(newBT.insertNode("Lassi"))

print(newBT.searchNode("Lassi"))

# newBT.postOrderTraversal(1)
