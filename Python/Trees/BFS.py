queue = [root]
res = []
while queue:

    level = []
    for i in range(len(queue)):
        node = queue.pop(0)
        level.append(node.val)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    res.append(level)

return res