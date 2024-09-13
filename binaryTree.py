class Node:

    def __init__(self, data):
        self.value = data
        self.right = None
        self.left = None

class BinaryTree:

    def __init__(self, data):
        self.root = Node(data)

    def insertLeft(self, currentNode, data):
        newnode = Node(data)
        if currentNode.left is None:
            currentNode.left = newnode
        else:
            newnode.left = currentNode.left
            currentNode.left = newnode

    def insertRight(self, currentNode, data):
        newnode = Node(data)
        if currentNode.right is None:
            currentNode.right = newnode
        else: 
            newnode.right = currentNode.right
            currentNode.right = newnode

def inorder(node):

    if node:
        inorder(node.left)
        print(node.value, end="->")
        inorder(node.right)

def preOrder(node):

    if node:

        print(node.value, end="->")
        preOrder(node.left)
        preOrder(node.right)

def postOrder(node):

    if node:
        postOrder(node.left)
        postOrder(node.right)
        print(node.value, end="->")

data = BinaryTree(5)
data.insertLeft(data.root, 1)
data.insertRight(data.root,2)

data.insertLeft(data.root.left, 3)
data.insertRight(data.root.right, 7)


# inorder(data.root)
# preOrder(data.root)
# postOrder(data.root)

def sumOfTree(node):

    if not node: return 0
    return node.value + sumOfTree(node.left) + sumOfTree(node.right)

def maxValue(node):

    if not node:
        return -1

    leftmax = maxValue(node.left)
    rightmax = maxValue(node.right)

    return max(node.value, leftmax, rightmax)

def size(node):

    if not node: return 0
    return 1 + size(node.left) + size(node.right)

def levelOfTree(node):

    if not node: return 0

    leftLevel = levelOfTree(node.left)
    rightLevel = levelOfTree(node.right)

    return max(leftLevel, rightLevel) + 1

def height(node):

    return levelOfTree(node) - 1

# print(levelOfTree(data.root))
# print(height(data.root))

def invertImage(node):

    if node:

        node.left, node.right = node.right, node.left
        invertImage(node.left)
        invertImage(node.right)

    return node


data = BinaryTree(1)
data.insertLeft(data.root, 2)
data.insertRight(data.root, 3)
data.insertLeft(data.root.left, 4)
data.insertRight(data.root.left, 5)
data.insertLeft(data.root.right, 6)
data.insertRight(data.root.right, 7)


# inorder(data.root)

# data.root = invertImage(data.root)
# print("")
# inorder(data.root)

def inorder(node):

    if node:

        inorder(node.left)
        print(node.value)
        inorder(node.right)

# print(inorder(data.root))

data1 = BinaryTree(1)
data1.insertLeft(data1.root, 2)
data1.insertRight(data1.root, 3)

data2 = BinaryTree(1)
data2.insertLeft(data2.root, 2)
data2.insertRight(data2.root, 3)

def isSame(data1, data2):

    if data1 is None and data2 is None:
        return True
    if (data1 is None and data2) or (data1 and not data2): return False
    return data1.value == data2.value and (isSame(data1.left, data2.left)) and (isSame(data1.right, data2.right))

# print(isSame(data1.root, data2.root))

import math
def isSymmetric(node):

    def inorder(node):

        if not node:

            result.append(-1)
        if node:

            inorder(node.left)
            result.append(node.value)
            inorder(node.right)

    result = []
    inorder(node)

    if len(result) % 2 == 0:
        return False
    mid = len(result)//2
    left = result[:mid]
    right = result[mid+1:]
    return left == right[::-1]


# name = []
# name.append(None)
# print(name)

result = []

def inorder(node):
    if not node:
        result.append(None)
        return
    inorder(node.left)
    result.append(node.value)
    inorder(node.right)

# inorder(data.root)
# print(result)
result1 = []
def inorder1(node):

    if node:

        inorder1(node.left)
        result1.append(node.value)
        inorder1(node.right)

# inorder1(data.root)
# print(result1)


def symmetricTree(node):

    if not node:
        return True
    
    def mirror(left, right):

        if not left.right and right.left:
            return True
        if not left.right or right.left:
            return False
        
        return left.value == right.value and mirror(left.left, right.right) and mirror(left.right, right.left)
    
    return mirror(node.left, node.right)
# print(symmetricTree(data.root))

def level(node):

    if not node: return 0

    return 1 + max(level(node.left), level(node.right))

inorder(data.root)
# print(result)
# print(level(data.root))

def level(node):

    if not node: return 0

    return 1 + max(level(node.left), level(node.right))

# print(level(data1.root))

def diameter(root, max=0):

    if not root: return 0

    left = level(root.left)
    right = level(root.right)

    return left + right

def result(node):

    return max(diameter(node), diameter(node.left), diameter(node.right))

def isExist(node, target):

    if not node: return False
    if node.value == target: 
        return True
    return isExist(node.left) or isExist(node.right)

def lowestCommon(node, p, q):

    if isExist(node.left, p) and isExist(node.right, q):
        return node
    if isExist(node.left, p) and isExist(node.left, q):
        return

def paths(node, string=""):
    
    if not node: return print(string)

    paths(node.left, string + str(node.value))
    paths(node.right, string + str(node.value))

def paths(node, string=""):

    if not node: return 

    if not node.left or not node.right: return print(string + str(node.value))

    paths(node.left, string + str(node.value))
    paths(node.right, string + str(node.value))

ritesh = BinaryTree(1)
ritesh.insertLeft(ritesh.root, 2)
ritesh.insertRight(ritesh.root, 3)
ritesh.insertLeft(ritesh.root.left, 4)
ritesh.insertRight(ritesh.root.left, 5)
ritesh.insertLeft(ritesh.root.right, 6)
ritesh.insertRight(ritesh.root.right, 7)

def size(node):

    if not node: return 0

    return 1 + size(node.left) + size(node.right)

def pathSum(node, target):

    if not node:
        return False
    
    if not node.left and not node.right and target == node.value:
        return True

    return pathSum(node.left, target-node.value) or pathSum(node.right, target-node.value)


def inorder(node):

    if node: 

        inorder(node.left)
        print(node.value)
        inorder(node.right)

inorder(data.root)
result = pathSum(data.root, 17)

def leftSum(root, position=0):

    if not root: return 0
    if not root.left and not root.right: return 0
    return root.left.value + leftSum(root.left, position=1) + leftSum(root.right, position=0)


