import java.util.Scanner;
import java.util.LinkedList;

public class ShoppingList {
   public static void main (String[] args) {
      Scanner scnr = new Scanner(System.in);

      // TODO: Declare a LinkedList called shoppingList of type ListItem
		LinkedList<ListItem> ShoppingList = new LinkedList<ListItem>();

      String item;
      
      // TODO: Scan inputs (items) and add them to the shoppingList LinkedList
      //       Read inputs until a -1 is input
      item = scnr.nextLine();
      /**
       * !item.equals("-1)
       * item.compareTo("-1") != 0
       */
      while (item.equals("-1")) {
        ShoppingList.add(new ListItem(item));
        item = scnr.nextLine();
     }
     
      // TODO: Print the shoppingList LinkedList using the printNodeData() method
    for (int i = 0; i < ShoppingList.size(); i++) {
       ShoppingList.get(i).printNodeData();
    }

   }
}