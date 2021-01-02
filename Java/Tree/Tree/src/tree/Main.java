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
public class Main {
    
    public static void main(String[] args){
        
        Node root = new Node(5);
        
        Tree tree = new Tree(root);
        tree.insert(22, root);
        tree.insert(7, root);
        tree.insert(4, root);
        tree.insert(3, root);
        tree.insert(18, root);
        tree.insert(19, root);
 
        tree.inorder(root);
        //tree.postorder(root);
        //tree.preorder(root);
        System.out.println("Maximum Value of Tree:"+tree.maxima(root));
        System.out.println("Minimum Value of Tree:"+tree.minima(root));
        
    
    
    
    }
    
}
