class Node:

  def __init__(self, data=None, next=None):#if nothing is passed, set to None
    self.data = data
    self.next = next

class LinkedList:

  count = None#global variable to be used for adding/removing at certain indexes
  
  #here, head is the node object, set to None of nothing is passed in
  def __init__(self, head=None):
    self.head = head

  def print_list(self):
    value = self.head#set value equal to Node that was set to head
    
    while value is not None:#so long as value isn't empty(meaning list wasn't already empty nor have we reached the end)
      print(value.data)#print value tied to the Node
      value = value.next#set value to the next Node in list

  #Note:if no index is given, adds to end of list, else, adds to given index
  def add_value(self, data, index=None):
    global count#for global variables in python, you need to explicitly set the scope
    
    if index is None:#if no index given, add at end of list
      #if list is empty, head is set to Node with given value, and return
      if self.head == None:
        self.head = Node(data)
        count = 1#if it's the first entry, set count to 1
        return
  
      #if not empty
      current = self.head#will be used to append a Node at end of list
  
      while current:#so long as current isn't empty
        #at each iteration, check if we finally reach end of list, if so, current will now point to our new Node
        if current.next is None:
          current.next = Node(data)
          count += 1#everytime we add a new Node, we add 1 to count for index use
          break
  
        #otherwise, if we haven't reach the end, we move on to the next node by setting the current Node equal to the next
        current = current.next

    else:
      index = int(index)#making sure index is a number
      if (index >= 0) and (index < count):#checking that index given is within range
        if index == 0:#if adding at first index (front)
          temp = self.head#temporarily store head Node in temp
          self.head = Node(data)#set head to new Node with given data
          #have head point to previous head Node(since the latter's 'next' wasn't changed, should still point to same Node)
          self.head.next = temp
          count += 1
        else:
          current = self.head#store first Node here
          num = 1#used as counter
          while num <= index:#until num isn't higher than index given
            temp = current.next#store the Node pointed by current Node here in temp
            if num == index:#if we're at the given position we add the new Node
              current.next = Node(data)#the Node added and pointed to by current Node
              temp2 = current.next#new Node added stored here
              temp2.next = temp#new Node now points to next Node current used to point at and we're done
              count += 1
              return
            else:
              current = current.next#move on to the next Node
              num += 1#increment num by 1
      else:
        print(str(index) + " is invalid.")

  #if not index is given, function removes from the end, else, removes at given index
  def remove_value(self, index=None):
    global count#for global variables in python, you need to explicitly set the scope

    if index is None:#if no index given, remove from end of list
      #if list is empty, head should be None, and there's nothing to remove
      if self.head == None:
        print("Nothing to remove.")
        return
  
      #if it's the only entry, we set the head to None, thus removing it
      if self.head.next is None:
        self.head = self.head.next
        count -= 1#decrement from count when removing
  
      #else we create current variable to keep track of which Node we're at
      current = self.head.next#since we know that head isn't point to None, we set current to that second Node
      previous = self.head#used in while loop in order to remove last entry
      
      while current.next is not None:
        previous = current#error?
        current = current.next#that next Node is set to current
  
      #since the while loop will continue until we reach the last entry
      previous.next = None#previous will point to None rather than the next(last) Node
      count -= 1#decrement from count when removing
      
    else:
      index = int(index)#making sure index is a number
      if (index >= 0) and (index < count):#checking that index given is within range
        if index == 0 and count >= 2:#if removing at first index (front) and list has at least 2 entries
          self.head = self.head.next#the Node pointed to by Head is now new Head
          count -= 1
        elif index == 0 and count == 1:#removing at first index and there is only 1 entry
          self.head = None#removing Node at index 0
          count -= 1
        else:#removing at an index greater than 1 (more than 2 entires)
          previous = self.head#store first Node here
          num = 1#used as counter
          while num <= index:#until num isn't higher than index given
            if num == index:#if we're at the given position we add the new Node
              temp = previous.next#Node to remove stored here
              previous.next = temp.next#Node being pointed to by Node to remove is now pointed by the previous Node
              count -= 1
              return
            else:
              previous = previous.next#move on to the next Node
              num += 1#increment num by 1
      else:
        print(str(index) + " is invalid.")

  #returns value at given index
  def get_value(self, index):
    global count#for global variables in python, you need to explicitly set the scope
    
    if (index > count) or (index < 0) or (count == None):
      return "There are no values in the list or index is out of bounds."

    #in cause the value of the first index needs to be returned
    if index == 0:
      return self.head.data

    #for values at indexes greater than 0
    current = self.head#set current to the first Node (Index 0)
    for i in range(index):#we traverse index num of times until we arrive at the correct Node
      current = current.next#set the Node here to value

    return current.data#return the value at given index

  #Note:This function was added to make looping through linked list simpler
  #returns an int for count, otherwise, 'None' as the list would be empty
  def get_size(self):
    global count
    return count
  