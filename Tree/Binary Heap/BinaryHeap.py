class Heap:
    def __init__(self, size) -> None:
        self.customList = (size + 1) * [None]
        self.heapSize = 0
        self.maxSize = size + 1


def peekHeap(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.customList[1]


def HeapSize(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.heapSize


def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        for i in range(1, rootNode.heapSize + 1):
            print(rootNode.customList[i])


def preOrderTraversal(rootNode, index):
    if index == 0 or index > rootNode.heapSize:
        return
    print(rootNode.customList[index])
    preOrderTraversal(rootNode, index * 2)
    preOrderTraversal(rootNode, index * 2 + 1)


def inOrderTraversal(rootNode, index):
    if index == 0 or index > rootNode.heapSize:
        return
    preOrderTraversal(rootNode, index * 2)
    print(rootNode.customList[index])
    preOrderTraversal(rootNode, index * 2 + 1)


def postOrderTraversal(rootNode, index):
    if index == 0 or index > rootNode.heapSize:
        return
    preOrderTraversal(rootNode, index * 2)
    preOrderTraversal(rootNode, index * 2 + 1)
    print(rootNode.customList[index])


def heapifyTreeInsert(rootNode, index, heapType):
    parentIndex = int(index / 2)
    if index <= 1:
        return
    if heapType == "Min":
        if rootNode.customList[index] < rootNode.customList[parentIndex]:
            rootNode.customList[index], rootNode.customList[parentIndex] = (
                rootNode.customList[parentIndex],
                rootNode.customList[index],
            )
            heapifyTreeInsert(rootNode, parentIndex, heapType)
    if heapType == "Max":
        if rootNode.customList[index] > rootNode.customList[parentIndex]:
            rootNode.customList[index], rootNode.customList[parentIndex] = (
                rootNode.customList[parentIndex],
                rootNode.customList[index],
            )
            heapifyTreeInsert(rootNode, parentIndex, heapType)


def insertNode(rootNode, nodeValue, heapType):
    if rootNode.heapSize + 1 == rootNode.maxSize:
        return "The heap is full"
    rootNode.customList[rootNode.heapSize + 1] = nodeValue
    rootNode.heapSize += 1
    heapifyTreeInsert(rootNode, rootNode.heapSize, heapType)
    return "the value has been successfully inserted"


newBinaryHeap = Heap(5)
insertNode(newBinaryHeap, 4, "Max")
insertNode(newBinaryHeap, 5, "Max")
insertNode(newBinaryHeap, 2, "Max")
insertNode(newBinaryHeap, 1, "Max")
print(HeapSize(newBinaryHeap))
preOrderTraversal(newBinaryHeap, 1)
