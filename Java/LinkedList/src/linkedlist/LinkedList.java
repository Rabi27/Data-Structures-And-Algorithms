/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package linkedlist;

/**
 *
 * @author Rabi Siddique
 */
public class LinkedList {
    Node head;
    
   
    public void insertItem(int value){
        
        Node newNode = new Node(value);
        
        if(head == null){
            
            head = newNode;
        }
        else{
            Node temp = head;
            while(temp.next != null){
                temp = temp.next;
            }
            temp.next = newNode;
        }
            
    }
    
    public void insertStart(int value){
        Node newNode = new Node(value);
        
        if(head == null){
            head = newNode;
        }
        else{
            Node temp = head;
            head = newNode;
            head.next = temp;
        }
    }
    
    
    public void insertAtPosition(int value,int position){
        Node newNode = new Node(value);
        Node temp = head;
        
        for(int i=1;i<position-1;i++){
            temp = temp.next;
        }
        
        newNode.next = temp.next;
        temp.next = newNode;
    }
    
    public int getLength(LinkedList list){
        int length = 0;
        Node temp = head;
        
        while(temp != null){
            temp = temp.next;
            length = length + 1;
        }
    
        return length;
    
    }
    
   public int getElementByIndex(int index){
       int element = 0;
       Node temp = head;
       
       for(int i=0;i<=index;i++){
           element = temp.value;
           temp = temp.next;
       }
       
       return element;
   }
    
    public void printList(LinkedList list){
        
        Node current = list.head;
        
        System.out.println("LinkedList:");
        while(current != null){
            
            System.out.println(current.value);
            current = current.next;
        
        }
    
    }
    
}
