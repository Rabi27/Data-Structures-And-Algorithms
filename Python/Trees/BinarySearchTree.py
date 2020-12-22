class Node():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self,value):
        if value <= self.data:
            if self.left == None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if self.right == None:
                self.right = Node(value)
            else:
                self.right.insert(value)

    '''
    Depth First Traversals:
    1-Inorder
    2-Preorder
    3-PostOrder

    Inorder Traversal involes visiting the left substree first then the root 
    node followed by the right substree.

             A
            / \
           /   \
           B    C
          /\    /\
         /  \  /  \
        D    E F  G   
        Inorder Traversal: D->B->E->A->F->G->C

    Preorder traversal involes visiting the root node first followed 
    by the left substree and then the right substree.

             A
            / \
           /   \
           B    C
          /\    /\
         /  \  /  \
        D    E F  G
        PreOrder Traversal:A->B->D->E->C->F->G

    PostOrder Traversal involves visiting the root node at the last. First the left substree
    is visited followed by the right substree and finally the root node. 

             A
            / \
           /   \
           B    C
          /\    /\
         /  \  /  \
        D    E F  G
        PostOrder Traversal: D->E->B->F->G->C->A

    '''
    #Inorder traversal gives sorted nodes as output
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)

    def postorder(self,root):

        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data)

    def preorder(self,root):
        if root:
            print(root.data)
            self.preorder(root.left)
            self.preorder(root.right)

'''
Deletion of a node in a BST
case 1 : Node has no children. Its a leaf node.
case 2: Node has a single child.
case 3 : Node has two children.

case 1 : Just remove the link from the parent to the child. Parent node
will now point to null/None.

case 2: Replace the node with its only child.

case 3: Replace with the inorder successor so as to maintain the
inorder traversal of the tree.

'''

    

root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
print("Inorder Traversal:")
root.inorder(root)
print("Preorder Traversal:")
root.preorder(root)
print("Postorder Traversal:")
root.postorder(root)


            

        





