from abc import abstractmethod
from abc import ABC

class ProduceInventoryAbstract(ABC):

  #Create a search feature for sku to find unique id's
  @abstractmethod
  def search_sku(self,sku):
    pass
    
  #Create a search feature for brandName to find produces' specific brand id
  @abstractmethod
  def search_brand_name(self,brand_name):
    pass
    
  @abstractmethod
  def display_by_category(self, category):
    pass
  
  @abstractmethod
  def create_inventory(self, produce_information_file):
    pass
  #adds produce to the 'user_provided_produce' txt file
    
  @abstractmethod
  def add_produce(self, generic_name, brand_name, category, price, sku):
    pass
  #Finding the object by the sku number and deleting the whole object
  @abstractmethod
  def delete_produce(self): 
    pass
    #given an sku num, if our search_sku function finds it, return thr produce object, 
    #otherwise returns None

  #print out the entire array of all variables(even with added produce objects)
  @abstractmethod
  def display_inventory(self):
    pass

class GroceryListInventoryAbstract(ABC):

  @abstractmethod
  def create_grocery_list(self, list_to_add): 
    pass
    
  @abstractmethod
  def view_grocery_list(self):
    pass
    
  @abstractmethod
  def delete_grocery_list(self, list_to_delete):
    pass
  
  @abstractmethod
  def add_to_grocery_list(self, list_name, produce):
    pass
    
  @abstractmethod
  def delete_from_grocery_list(self, list_name, produce):
    pass
  
  @abstractmethod
  def view_item_in_grocery_list(self, list_name): 
    pass

  @abstractmethod
  def number_of_produce_in_list(self, list_name):
    pass

class DiscAbstract(ABC):

  #return num of items stored in dictionary
  @abstractmethod
  def __len__(self):
    pass

  #returns true or false depending if key is in dictionary
  @abstractmethod
  def __contains__(self, key):
    pass

  #returns value tied to given key
  @abstractmethod
  def __getitem__(self, key):
    pass

  #if key is in dictionary, value tied to key is modified
  #otherwise, if key not in dictionary, it is ADDED to dictionary
  #NOTE:There MUST NOT be any DUPLICATE KEYS added
  @abstractmethod
  def __setitem__(self, key, value):
    pass

  #if key is in dictionary, remove key and value tied to it from dictionary
  @abstractmethod
  def pop(self, key):
    pass