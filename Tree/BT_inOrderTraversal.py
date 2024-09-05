class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.leftChild = None
        self.rightChild = None


root_node = TreeNode("Drinks")
leftChild = TreeNode("Hot")
rightChild = TreeNode("Cold")
root_node.leftChild = leftChild
root_node.rightChild = rightChild

leftChild_l = TreeNode("Tea")
leftChild_r = TreeNode("Milk")
leftChild.leftChild = leftChild_l
leftChild.rightChild = leftChild_r

rightChild_l = TreeNode("Lassi")
rightChild_r = TreeNode("sharbat")
rightChild.leftChild = rightChild_l
rightChild.rightChild = rightChild_r


def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)


inOrderTraversal(root_node)
