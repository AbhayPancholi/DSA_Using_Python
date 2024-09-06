import QueueLinkedList as queue


class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.leftChild = None
        self.rightChild = None


root_node = TreeNode("Drinks")
leftchild = TreeNode("Hot")
rightchild = TreeNode("Cold")

root_node.leftChild = leftchild
root_node.rightChild = rightchild

leftchild_l = TreeNode("Tea")
leftchild_r = TreeNode("Coffee")

leftchild.leftChild = leftchild_l
leftchild.rightChild = leftchild_r

rightchild_l = TreeNode("Lassi")
# rightchild_r = TreeNode("Sharbat")

rightchild.leftChild = rightchild_l
# rightchild.rightChild = rightchild_r


def LevelOrderTraversal(rootNode):
    if not rootNode:
        return
    customqueue = queue.Queue()
    customqueue.enqueue(rootNode)
    while not customqueue.isEmpty():
        root = customqueue.dequeue()
        print(root.value.data)

        if root.value.leftChild is not None:
            customqueue.enqueue(root.value.leftChild)

        if root.value.rightChild is not None:
            customqueue.enqueue(root.value.rightChild)


def FindDeepestNode(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not customQueue.isEmpty():
            root = customQueue.dequeue()
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)

        deepestNode = root.value
        return deepestNode


def deleteDeepestNode(rootNode, dNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not customQueue.isEmpty():
            root = customQueue.dequeue()
            if root.value == dNode:
                root.value = None
                return
            if root.value.leftChild:
                if root.value.leftChild == dNode:
                    root.value.leftChild = None
                    return
                else:
                    customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild:
                if root.value.rightChild == dNode:
                    root.value.rightChild = None
                    return
                else:
                    customQueue.enqueue(root.value.rightChild)


def deleteNode(rootNode, node):
    if not rootNode:
        return "The binary tree does not exist"
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not customQueue.isEmpty():
            root = customQueue.dequeue()
            if root.value.data == node:
                dNode = FindDeepestNode(rootNode)
                root.value.data = dNode.data
                deleteDeepestNode(rootNode, dNode)
                return "The node has been successfully deleted"

            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
        return "Failed to delete the node"


deleteNode(root_node, "Hot")
LevelOrderTraversal(root_node)
