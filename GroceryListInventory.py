class GroceryListInventory:

  #creating our list var for our lists, with one being used for the other to make a 2D array
  def __init__(self):
    self.__grocery_list = []# 'Picnic' 'Family Outing'
    self.__list_of_produce_lists = []#list of produce lists tied to a grocery list
    self.__produce_list = []#list of produce objects

  def create_grocery_list(self, list_to_add):
    self.__grocery_list.append(list_to_add)
    self.__list_of_produce_lists.append(self.__produce_list)

  #prints the names of all grocery lists
  def view_grocery_list(self):
    if self.__grocery_list:
      print("Here are all the grocery lists created:")
      for name in self.__grocery_list:
        print("* " + name)
    else:
      print("There are no grocery lists yet.")

  #takes string list name as param and deletes from grocery list dict
  def delete_grocery_list(self, list_to_delete):
    list_found = False#var used to tell user whether the list was found or not
    for name in self.__grocery_list:
      if name == list_to_delete:
        index = self.__grocery_list.index(list_to_delete)#get index of the grocery list
        del self.__list_of_produce_lists[index]#delete the respective produce list associated to the grocery index
        self.__grocery_list.remove(list_to_delete)#delete list name from grocery list
        list_found = True#since it was found, we changed this to true
    if list_found:
      print(list_to_delete + " was deleted.")
    else:
      print(list_to_delete + " was not found.")

  def add_to_grocery_list(self, list_name, produce):
    list_found = False#var used to tell user whether the list was found or not
    for name in self.__grocery_list:
      if name == list_name:
        index = self.__grocery_list.index(list_name)#get index of list found in grocery list
        list_to_add = self.__list_of_produce_lists[index]#fetching for respective list in our list of produce lists
        list_to_add.append(produce)
        self.__list_of_produce_lists[index] = list_to_add
        list_found = True
    if list_found:
      print(produce.get_generic_name() + " was added to " + list_name + ".")
    else:
      print(produce.get_generic_name() + " was not added.")

  def delete_from_grocery_list(self, list_name, produce):
    for name in self.__grocery_list:
     if name == list_name:
       index = self.__grocery_list.index(list_name)
       list_to_delete = self.__list_of_produce_lists[index]
       list_to_delete.remove(produce)
       print(produce.get_generic_name() + " was deleted")

  #not complete
  def view_item_in_grocery_list(self, list_name):
    for name in self.__grocery_list:
      if name == list_name:
        index = self.__grocery_list.index(list_name)
        print(self.__list_of_produce_lists())  
        
  def number_of_produce_in_list(self, list_name):
    print ("The list is: " + list_name)
    counter = 0 #counts the produce in list 
    index = 0 #index of list_name in grocery list
    for i in self.__rocery_list: #for every produce in grocery list
      if list_name == i:
        pass 
      index += 1
      counter += 1
      return counter
   