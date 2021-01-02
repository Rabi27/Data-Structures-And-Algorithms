/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package tree;

/**
 *
 * @author Rabi Siddique
 */
public class Tree {
    
    Node root;

    public Tree(Node root) {
        this.root = root;
    }
    
    public void insert(int data,Node root){
        
        Node newNode = new Node(data);
        
        if(data<root.data){
            if(root.left == null)root.left = newNode;
            else{
                insert(data,root.left);
            }
        }
        else{
            if(root.right == null)root.right = newNode;
            else{
                insert(data,root.right);
            }
        
        }
    }
    
    public void inorder(Node root){
        
        if(root != null){
        inorder(root.left);
        System.out.println(root.data+" ");
        inorder(root.right);
        
        }
    }
    
        public void preorder(Node root){
        
        if(root != null){
        System.out.println(root.data+" ");
        inorder(root.left);
        inorder(root.right);
        }
    }
        
        public void postorder(Node root){
        
        if(root != null){
        inorder(root.left);
        inorder(root.right);
        System.out.println(root.data);
        }
    }
        
        public int minima(Node root){
            Node temp = root;
            
            while(temp.left != null){
                temp = temp.left;
            }
            
            return temp.data;
        }
        
        public int maxima(Node root){
            Node temp = root;
            
            while(temp.right != null){
                temp = temp.right;
            }
            
            return temp.data;
        }
        
        public void delete(int data){
        
        
            
        
        }
    
}
