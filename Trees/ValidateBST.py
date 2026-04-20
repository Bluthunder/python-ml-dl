
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isValidBST_recursive(root : TreeNode)-> bool:

    def validate(node, min_val, max_val):

        if not node:
            return True

        if node.val <= min_val or node.val >= max_val:
            return False

        return (validate(node.left, min_val, node.val ) and
                    validate(node.right, node.val, max_val))

    return validate(root, float('-inf'), float('-inf'))


def isValidBST_iterative(root: TreeNode)-> bool:
    stack = [(root, float('-inf'), float('inf'))]

    while stack:
        node, min_val, max_val = stack.pop()
        if not node:
            continue
        if node.val <= min_val or node.val >= max_val:
            return False
        stack.append((node.left,  min_val,  node.val))
        stack.append((node.right, node.val, max_val))

    return True


if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(6)

    print(isValidBST_recursive(root))
    print(isValidBST_iterative(root))
