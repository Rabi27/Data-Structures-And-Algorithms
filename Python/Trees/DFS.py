#DFS without using Recursion
stack = [root]
res = []
while stack:
    node = stack.pop(0)
    stack.append(node.val)
    if node.right:
        stack.append(node.right)
    if node.left:
        stack.append(node.left)
    