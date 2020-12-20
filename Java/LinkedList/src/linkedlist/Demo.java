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
public class Demo {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        
        LinkedList list = new LinkedList();
        list.insertItem(12);
        list.insertItem(13);
        list.insertItem(34);
        list.insertStart(66);
        list.insertStart(99);
        System.out.println("Length of List:"+list.getLength(list));
        list.insertStart(89);
        System.out.println("Length of List:"+list.getLength(list));
        list.insertAtPosition(123, 3);
        list.insertAtPosition(3, 3);
        list.insertAtPosition(53, 5);
        list.printList(list);
        System.out.println("Element:"+list.getElementByIndex(4));
        
    }
    
}
