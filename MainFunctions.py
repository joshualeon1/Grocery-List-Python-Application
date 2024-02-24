from Produce import Produce
from ProduceInventory import ProduceInventory
from Interface import Interface
from LinkedList import LinkedList
from PDictionary import PDictionary

def main_step_three():

  #creating a new produced object
  p1 = Produce()
  
  #Asking the user for produce info
  genericName = input("Enter generic product name:")
  brandName = input("Enter brand name:")
  category = input("Enter product category:")
  price = input("Enter product price:")
  sku = input("Enter product sku:")

  #setting object p attributes
  p1.set_generic_name(genericName)
  p1.set_brand_name(brandName)
  p1.set_category(category)
  p1.set_price(float(price))
  p1.set_sku(int(sku))

  print("Product Info: " + p1.get_generic_name() + "," +
    p1.get_brand_name() + ", " + str(p1.get_sku()) + ", " +
    p1.get_category() + ", " + str(p1.get_price()))

def main_step_four(): 

  #creating our produce inventory object
  p_inventory = ProduceInventory()
  p_inventory.create_inventory("program_provided_produce.txt")

  sku = int(input("Enter SKU number: "))

  produce = p_inventory.search_sku(sku)

  if produce == None:
    print("Produce not found.")
  else:
    print("Product Info:\n" + produce.get_generic_name() + " | " +
      produce.get_brand_name() + " | " + str(produce.get_sku()) + " | " +
      produce.get_category() + " | " + str(produce.get_price()))

  #lines 48-57 are to test search_brandName function
  brand = input("Enter the brand Name: ")

  produce_2 = p_inventory.search_brandName(brand)

  if produce_2 == None:
    print("Produce not found.")
  else:
    print("Product Info:\n" + produce_2.get_generic_name() + " | " +
      produce_2.get_brand_name() + " | " + str(produce_2.get_sku()) + " | " +
      produce_2.get_category() + " | " + str(produce_2.get_price()))

  #testing additonal functions created
  p_inventory.add_produce()
  p_inventory.display_inventory()
  p_inventory.delete_produce()
  p_inventory.display_inventory()

#insert new function below
def main_step_five():
  Interface.grocery_inventory_cl()

def test_linkedlist():
  llist = LinkedList()
  llist.add_value("Yes")
  llist.add_value("No")
  llist.add_value("Maybe")
  llist.add_value("For sure")
  llist.print_list()
  print("--------------------")
  llist.add_value("Perhaps", 3)
  llist.print_list()
  print("--------------------")
  llist.remove_value(2)
  llist.print_list()
  print("--------------------")
  print(llist.get_value(3))

def test_dictionary():
  pDict = PDictionary()
  pDict.setitem("a", 123)