class BTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def preorder(node):
    if node:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)

def inorder(node):
    if node:
        inorder(node.left)
        print(node.data, end=" ")
        inorder(node.right)

def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=" ")


root = BTNode(1)
root.left = BTNode(2)
root.right = BTNode(3)
root.left.left = BTNode(4)
root.left.right = BTNode(5)

print("Preorder:")
preorder(root)
print("\nInorder:")
inorder(root)
print("\nPostorder:")
postorder(root)
