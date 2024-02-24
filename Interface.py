from GroceryListInventory import GroceryListInventory#J
from ProduceInventory import ProduceInventory#J

class Interface:#J
  @staticmethod
  def grocery_inventory_cl():

    print("***************************************************")
    print("Welcome to the Grocery shopping list")
    print("[1] - Create Grocery List")
    print("[2] - View Grocery List(s)")
    print("[3] - Delete a Grocery List")
    print("[4] - Add Produce to Grocery List")
    print("[5] - Delete Produce from Grocery List")
    print("[6] - View Produce Within a List")
    print("[7] - Display Produce by Category")
    print("[8] - Add a Produce to the User Produce List")
    print("[9] - View Produce List Provided by the Program and User")
    print("[10] - View Number of Produce in a List")
    print("[11] - View Total Cost for Products in a List")
    print("[12] - Quit Program")
    print("***************************************************")

    g_inventory = GroceryListInventory()
    p_inventory_1 = ProduceInventory()
    p_inventory_1.create_inventory("program_provided_produce.txt")#for program provided produce
    p_inventory_2 = ProduceInventory()
    p_inventory_2.create_inventory("user_provided_produce.txt")#for user provided produce
  
    option = 0
    while(option != 12):
      option = int(input("Option: "))

      if option == 1:#create grocery list
        list_to_add = input("Enter the name of your grocery list:\n")
        g_inventory.create_grocery_list(list_to_add)

      elif option == 2:#view grocery list
        g_inventory.view_grocery_list()

      elif option == 3:#delete grocery list
        list_to_delete = input("Enter the name of the grocery list you wish to delete: ")
        g_inventory.delete_grocery_list(list_to_delete)

      elif option == 4:#add produce to grocery list
        list_name = input("Enter the name of the grocery list you would like to add to:\n")
        print("Please select which produce you would like to add:")
        produce_option = int(input("[1] - Program Provided Produce\n[2] - User Provided Produce\nEnter Option: "))
        if produce_option == 1:
          p_inventory_1.display_inventory()
          sku = int(input("Enter the sku number of the produce: "))
          produce = p_inventory_1.search_sku(sku)
          if produce != None:
            g_inventory.add_to_grocery_list(list_name, produce)
          else:
            print("Produce not found by given sku. Please try again.")
        elif produce_option == 2:
          p_inventory_2.display_inventory()
          sku = int(input("Enter the sku number of the produce: "))
          produce = p_inventory_2.search_sku(sku)
          if produce != None:
            g_inventory.add_to_grocery_list(list_name, produce)
            print(produce.get_generic_name() + " was added.")
          else:
            print("Produce not found. Please try again.")
        else:
          print("Incorrect value received. Please try again.")
          
      elif option == 5:#delete a produce object from the grocery list
        current_list = input("Enter the name of the list you want to delete from: ")#get grocery list name
        #search for list corresponding to that grocery list
        
        #within the list, find produce user is trying to delete
        #delete produce from that list
        sku = int(input("Enter the sku of the produce you want to delete: "))
        produce = p_inventory_1.search_sku(sku)
        g_inventory.delete_from_grocery_list(current_list, produce)

        #TODO: ERROR HERE
      elif option == 6:#Display all produce items within a grocery list
        current_list = input("Enter the name of the list to display: ")
        g_inventory.view_item_in_grocery_list(current_list)
        print("Option 6 worked! \n" + current_list + " was displayed.")
        
      elif option == 7:#Display all produce items with a specific category desired by user
        category = input("Enter the produce category you want to view: ")#Ex- Dairy
        p_inventory_1.display_by_category(category)#displays all produce that are dairy
        p_inventory_2.display_by_category(category)
        
      elif option == 8:#add produce to user produce FILE
        generic_name = input("Enter the name of the produce: ")
        brand_name = input("Enter the brand name of the produce: ")
        category = input("Enter the category of the produce item: ")
        price = input("Enter the price of the produce: ")
        sku = input("Enter the sku of the produce item: ")
        p_inventory_1.add_produce(generic_name,brand_name,category,price,sku)

      elif option == 9:#display all file entries
        print("All produce provided by program: ")
        p_inventory_1.display_inventory()
        print("All produce provided by user: ")
        p_inventory_2.display_inventory()

      elif option == 10:#View number of produce in a list
        
        #display number here
        print("Number of Produce in List: ")
        counts = [[produce.count(item), item] for item in set(produce)]
        print(counts)
        

      elif option == 11:#total cost of products in the list
        print("Total Cost of Produce in this List: ")
        total=0
        for each_item in items:
          t=(each_item["price"])
          total=total+t
          print(total)
      
      elif option == 12:
        print("Good Bye...")
        exit()
      else:
        print("Invalid option, please try again.")
