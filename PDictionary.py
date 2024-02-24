#Here, the student defined dictioanry will be added using the 'DictAbstact' AssertionError
from LinkedList import LinkedList
from abstract import DiscAbstract

class PDictionary(DiscAbstract):

  def __init__(self, key=None, value=None):
    self.key = key
    self.key_llist = LinkedList()
    self.value = value
    self.value_llist = LinkedList()

  def len(self):
    count = self.key_llist.get_size();
    return count
    
  def contains(self, key):
    num = self.key_llist.get_size()
    for i in range(num):#traverse through the key list
      if key == self.key_llist.get_value(i):#check if given key is within our key list
        return True#returns true if it's in the list
    return False#else returns false

  def getitem(self, key):
    num = self.key_llist.get_size()
    for i in range(num):
      if PDictionary.contains(key):#check if given key is within our key list
        return self.value_llist.get_value(i)#return the value tied to it
    return None#otherwise, return None
        

  def setitem(self, key, value):
    for i in self.key_llist:
      if key == self.key_llist[i]:#check to see if key has been used already
        return "Key already has been used."
      
      elif key != self.key_llist[i]:
        self.key_llist.add_value(value) #if key hasn't been used, 
        self.value_llist.add_value(value)
        return self.value_llist[i]
      
  def pop(self, key):
    for i in self.key_llist:
      if key == self.key_llist[i]: # loop through keyllist to find matching key
        self.key_llist[i].remove_value() #remove key at i in key list
        self.value_llist[i].remove_value() #remove value at i in value list
      return "removed"
          