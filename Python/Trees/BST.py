class Node:

    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self,root,value):

        if value < root.value:
            if not root.left:
                self.left = Node(value)
            else:
                self.left.insert(self.left,value)
        else:
            if not root.right:
                self.right = Node(value)
            else:
                self.right.insert(self.right,value)

    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.value)
            self.inorder(root.right)

    def preorder(self,root):
        if root:
            print(root.data)
            self.inorder(root.left)
            self.inorder(root.right)

    def postorder(self,root):
        if root:
            self.inorder(root.left)
            self.inorder(root.right)
            print(root.data)

    def minValueNode(self,node):
        current = node
    
        while(current.left is not None):
            current = current.left
    
        return current


    def delete(self,root,value):

        if not root:
            return None

        if value < root.value:
            root.left = self.delete(root.left,value)
        elif value > root.value:
            root.right = self.delete(root.right,value)
        else:

            if not root.left:
                temp = root.right
                root = None
                return temp
            elif not root.right:
                temp = root.left
                root = None
                return temp

            temp = self.minValueNode(root.right)
            root.data = temp.data
            root.right = self.delete(root.right,root.value)

        return root

    



root = Node(34)
root.insert(root,37)
root.insert(root,55)
root.insert(root,3)
root.insert(root,2)
print("Inorder Traversal:")
root.inorder(root)
root.delete(root,3)
print("Inorder Traversal after Deletion:")
root.inorder(root)








        

