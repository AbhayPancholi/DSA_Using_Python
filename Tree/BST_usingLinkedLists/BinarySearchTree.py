import QueueLinkedList as queue


class BSTNode:
    def __init__(self, data) -> None:
        self.data = data
        self.leftChild = None
        self.rightChild = None


def insertNode(rootNode, nodeValue):
    if rootNode.data == None:
        rootNode.data = nodeValue
    elif rootNode.data >= nodeValue:
        if rootNode.leftChild is None:
            rootNode.leftChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.rightChild, nodeValue)
    return "Node has been successfully inserted"


def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not customQueue.isEmpty():
            root = customQueue.dequeue()
            print(root.value.data)

            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)


def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)


def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)


def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)


def searchNode(rootNode, value):
    if rootNode.data == value:
        print("Node found")
    elif rootNode.data > value:
        if rootNode.leftChild.data == value:
            print("Node found")
        else:
            searchNode(rootNode.leftChild, value)
    else:
        if rootNode.data == value:
            print("Node found")
        else:
            searchNode(rootNode.rightChild, value)


def minValue(rootNode):
    current = rootNode
    while current.leftChild is not None:
        current = current.leftChild
    return current


def deleteNode(rootNode, nodeValue):
    if rootNode is None:
        return rootNode
    if rootNode.data > nodeValue:
        rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue)
    elif rootNode.data < nodeValue:
        rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue)
    else:
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp

        if rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp

        temp = minValue(rootNode.rightChild)
        rootNode.data = temp.data
        rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)
    return rootNode


newBST = BSTNode(None)
insertNode(newBST, 70)
insertNode(newBST, 60)
insertNode(newBST, 80)
insertNode(newBST, 50)
insertNode(newBST, 40)
insertNode(newBST, 65)

deleteNode(newBST, 80)
postOrderTraversal(newBST)
