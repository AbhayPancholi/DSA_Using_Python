import QueueLinkedList as queue


class AVLNode:
    def __init__(self, data) -> None:
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.height = 1


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
        if rootNode.rightChild.data == value:
            print("Node Found")
        else:
            searchNode(rootNode.rightChild, value)


def getHeight(rootNode):
    if not rootNode:
        return 0
    return rootNode.height


def rightRotate(disbalancedNode):
    newRoot = disbalancedNode.leftChild
    disbalancedNode.leftChild = disbalancedNode.leftChild.rightChild
    newRoot.rightChild = disbalancedNode
    disbalancedNode.height = 1 + max(
        getHeight(disbalancedNode.leftChild), getHeight(disbalancedNode.rightChild)
    )
    newRoot.height = 1 + max(
        getHeight(newRoot.leftChild), getHeight(newRoot.rightChild)
    )
    return newRoot


def leftRotate(disbalancedNode):
    newRoot = disbalancedNode.rightChild
    disbalancedNode.rightChild = disbalancedNode.rightChild.leftChild
    newRoot.leftChild = disbalancedNode
    disbalancedNode.height = 1 + max(
        getHeight(disbalancedNode.leftChild), getHeight(disbalancedNode.rightChild)
    )
    newRoot.height = 1 + max(
        getHeight(newRoot.leftChild), getHeight(newRoot.rightChild)
    )
    return newRoot
