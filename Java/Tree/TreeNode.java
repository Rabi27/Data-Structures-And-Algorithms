/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package iteratorpattern;

/**
 *
 * @author Rabi Siddique
 */
public class TreeNode {
    
    int data;
    TreeNode left, right;

    public TreeNode(int data) {
        this.data = data;
        this.left = null;
        this.right = null;
    }
    
   
    public void insert(int value){
        
        
        if(value <= data){
        
            if(left == null){
                left = new TreeNode(value);
            }
            else{
                left.insert(value);
            }
        }
        else{
            if(right == null){
                right = new TreeNode(value);
            }
            else{
                right.insert(value);
            }
        }
         
    }
    
    
   
    
}
