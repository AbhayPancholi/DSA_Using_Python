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
rightchild_r = TreeNode("Sharbat")

rightchild.leftChild = rightchild_l
rightchild.rightChild = rightchild_r


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


LevelOrderTraversal(root_node)
