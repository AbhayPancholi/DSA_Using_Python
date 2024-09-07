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


def Search(rootNode, nodeValue):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not customQueue.isEmpty():
            root = customQueue.dequeue()
            if root.value.data == nodeValue:
                return "Success"
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
        return "Not Found"


print(Search(root_node, "Juice"))
