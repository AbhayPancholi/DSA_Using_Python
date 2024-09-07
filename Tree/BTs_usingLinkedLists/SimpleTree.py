class TreeNode:
    def __init__(self, data, children=None) -> None:
        self.data = data
        self.children = children or []

    def __str__(self, level=0) -> str:
        ret = " " * level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret

    def AddChild(self, TreeNode):
        self.children.append(TreeNode)


tree = TreeNode("Drinks")
cold = TreeNode("Cold")
hot = TreeNode("hot")
tree.AddChild(cold)
tree.AddChild(hot)
print(tree)
