#LAB-7
#Binary Search Tree Node Search
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def search_tree(node, value):
    if node is None:
        return False
    if node.value == value:
        return True
    return search_tree(node.left, value) or search_tree(node.right, value)

root = Node(10)
root.left = Node(8)
root.right = Node(20)
root.left.left = Node(7)
root.left.right = Node(9)
root.right.right = Node(21)
root.right.left = Node(15)

a = int(input("Enter the value you want to search for: "))

if search_tree(root, a):
    print("Searching element is found.")
else:
    print("Searching element is not found.")




#Leaf Node Sum in a Tree
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
def print_tree(node):
    if node is not None:
        print(node.value)
        print_tree(node.left)
        print_tree(node.right)
def sum_leaf_nodes(node):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return node.value
    return sum_leaf_nodes(node.left) + sum_leaf_nodes(node.right)

root = Node(10)
root.left = Node(8)
root.right = Node(20)
root.left.left = Node(7)
root.left.right = Node(9)
root.right.right = Node(21)
root.right.left = Node(15)
print_tree(root)
leaf_sum = sum_leaf_nodes(root)
print("Sum of leaf nodes:", leaf_sum)




#Spinal (Zig-Zag) Order Tree Traversa
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def spiral_traversal(root):
    if not root:
        return

    
    current_level = []
    next_level = []

    
    left_to_right = True

    current_level.append(root)

    while current_level:
        node = current_level.pop()
        print(node.value, end=" ")

        if left_to_right:
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        else:
            if node.right:
                next_level.append(node.right)
            if node.left:
                next_level.append(node.left)

        if not current_level:
            current_level, next_level = next_level, current_level
            left_to_right = not left_to_right


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.left.left=TreeNode(8)
root.left.left.right=TreeNode(9)
root.left.right = TreeNode(5)
root.left.right.right = TreeNode(11)
root.left.right.left = TreeNode(10)
root.right.right = TreeNode(7)
root.right.right.right = TreeNode(15)
root.right.right.left = TreeNode(14)
root.right.left=TreeNode(6)
root.right.left.left=TreeNode(12)
root.right.left.right=TreeNode(13)




print("Spiral Order Traversal:")
spiral_traversal(root)
