class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
    
    def add_child(self, child):
        self.children.append(child)
    
    def display(self, level=0):
        print(" " * level * 2 + str(self.data))
        for child in self.children:
            child.display(level + 1)

root = TreeNode("Root")
child1 = TreeNode("Child 1")
child2 = TreeNode("Child 2")

root.add_child(child1)
root.add_child(child2)
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
    
    def add_child(self, child):
        self.children.append(child)
    
    def display(self, level=0):
        print(" " * level * 2 + str(self.data))
        for child in self.children:
            child.display(level + 1)


root = TreeNode("Root")
child1 = TreeNode("Child 1")
child2 = TreeNode("Child 2")

root.add_child(child1)
root.add_child(child2)
child1.add_child(TreeNode("Grandchild 1"))

root.display()
