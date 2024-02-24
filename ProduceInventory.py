from Produce import Produce
from abstract import *

class ProduceInventory(ProduceInventoryAbstract): 

  #creating our list variable to hold 'Produce' objects in constructor
  def __init__(self):
    self.__produce_list = []
    
  #Create a search feature for sku to find unique id's
  def search_sku(self,sku):
    for produce in self.__produce_list:
      if produce.get_sku() == sku:
        return produce
    return None
    
  #Create a search feature for brandName to find produces' specific brand id
  def search_brand_name(self,brand_name):
    for produce in self.__produce_list:
      if produce.get_brand_name() == brand_name:
        return produce
    return None

  def display_by_category(self, category):
    for produce in self.__produce_list:
      if produce.get_category() == category:
        print(produce.display_produce())
    return None
  
  #function takes in a file name intially
  def create_inventory(self, produce_information_file):

    #we access the file with produce items provided by the program
    with open(produce_information_file) as file:

      #for every line in file, we read it up till the trailing newline
      #create 'fields' array to hold every entry per line
      for rows in file:
        rows = rows.strip("\n")
        fields = rows.split(",")

        #produce objects are created then has its values set
        produce = Produce()
        #the format:Butter,Land O'Lakes Salted Butter,Dairy,3.79,1
        produce.set_generic_name(fields[0])
        produce.set_brand_name(fields[1])
        produce.set_category(fields[2])
        produce.set_price(float(fields[3]))
        produce.set_sku(int(fields[4]))

        #add 'produce' object to our produce list
        self.__produce_list.append(produce)

  #adds produce to the 'user_provided_produce' txt file
  def add_produce(self, generic_name, brand_name, category, price, sku):
    
    p1 = Produce()
    #setting object p attributes 
    p1.set_generic_name(generic_name)
    p1.set_brand_name(brand_name)
    p1.set_category(category)
    p1.set_price(float(price))
    p1.set_sku(int(sku))

    #new produce item added to list
    self.__produce_list.append(p1)

    #new produce item added to .txt file (two lines below created by Joshua)
    with open('user_provided_produce.txt', 'a') as f:
      f.write(generic_name + "," + brand_name + "," + category + "," + str(price) + "," + str(sku) + " \n")

  #Finding the object by the sku number and deleting the whole object
  def delete_produce(self):
    
    #given an sku num, if our search_sku function finds it, return thr produce object, 
    #otherwise returns None
    produce = ProduceInventory.search_sku(int(input("Enter product sku to delete: ")))

    if produce != None:
      self.__produce_list.remove(produce)
      print("Produce was deleted.")
    else:
      print("The produce was not found in list, thus, nothing was deleted.")
    
  #print out the entire array of all variables(even with added produce objects)
  def display_inventory(self):
    length = len(self.__produce_list)
    for i in range(length):
      print(self.__produce_list[i].display_produce())
      