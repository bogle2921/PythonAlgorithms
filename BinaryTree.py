class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)
    
    def printTree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorderPrint(tree.root, "")
        elif traversal_type == "inorder":
            return self.inorderPrint(tree.root, "")
        elif traversal_type == "postorder":
            return self.postorderPrint(tree.root, "")
        else:
            print("That type is not supported")
            return False
    
    def preorderPrint(self, start, traversal):
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorderPrint(start.left, traversal)
            traversal = self.preorderPrint(start.right, traversal)
        return traversal
    
    def inorderPrint(self, start, traversal):
        if start:
            traversal = self.inorderPrint(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorderPrint(start.right, traversal)
        return traversal
    
    def postorderPrint(self, start, traversal):
        if start:
            traversal = self.inorderPrint(start.left, traversal)
            traversal = self.inorderPrint(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.right.right.right = Node(8)

print(tree.printTree("preorder"))
print(tree.printTree("inorder"))
print(tree.printTree("postorder"))
        