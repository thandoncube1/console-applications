import java.util.*;

class LaggageManager {
    public static enum Size {
        SMALL, MEDIUM, LARGE, EXTRALARGE
    }
    
    public static Size getSizeProp(String option) {
        Size bagSize = null;
        
        if (option.equals("S")) {
            bagSize = Size.SMALL;
        } else if (option.equals("M")) {
            bagSize = Size.MEDIUM;
        } else if (option.equals("L")) {
            bagSize = Size.LARGE;
        } else if (option.equals("X")) {
            bagSize = Size.EXTRALARGE;
        }
        
        return bagSize;
    }
    
    public static void renderOption() {
        System.out.println("Select the option you want: ");
        System.out.println("Option: \n1. Small Laggage - (S)\n2. Medium Laggage - (M)\n3. Large Laggage - (L)\n4. Extra Large Laggage - (X)\n5. Exit the program - (E)");
    }
    
   public static void main(String[] args) {
     Scanner input = new Scanner(System.in);
     System.out.println("Welcome to the Baggage Manager");
     renderOption();
     String option;
     String endProgram;
     String showOptions;
     String choiceSet = "SMLXE";
     
     do {
         do {
             System.out.print("Please enter your option here: ");
             option = input.nextLine().strip().toUpperCase();
         } while (!choiceSet.trim().toUpperCase().contains(option));
         
         System.out.println("Size: " + option + " \nGet Size " + getSizeProp(option) + " \nAnother: " + choiceSet.trim().toUpperCase().contains(option));
         
         switch (getSizeProp(option)) {
             case SMALL:
                 System.out.println("Carry On Laggage - Place on the over head bin or under the seat.");
                 break;
             case MEDIUM:
                 System.out.println("Carry On Laggage - Place on the over head bin");
                 break;
             case LARGE:
                 System.out.println("Check In Laggage - Please weight and get the price tag on the bag.");
                 break;
             case EXTRALARGE:
                 System.out.println("Pay the Extra Large Fee ($) Pass by Security for a Safety check - Weight the Laggage and check in for Oversize.");
                 break;
            default:
                System.out.println("Option selected not available.");
                System.out.print("\nTo show option press (H) or Any key to Continue: ");
                showOptions = input.nextLine().strip().toUpperCase();
                if (showOptions.equals("H")) {
                    renderOption();
                }
         }
         
        System.out.print("\nWould you like to Continue (Y) or Exit (E): ");
        endProgram = input.nextLine().strip().toUpperCase();
        
         
     } while (!endProgram.equals("E"));

     input.close();
   }
}
