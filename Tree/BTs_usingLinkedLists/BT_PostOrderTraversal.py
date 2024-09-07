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


def PostOrderTraversal(rootNode):
    if not rootNode:
        return
    PostOrderTraversal(rootNode.leftChild)
    PostOrderTraversal(rootNode.rightChild)
    print(rootNode.data)


PostOrderTraversal(root_node)
