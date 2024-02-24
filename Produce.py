class Produce:
  
  def __init__(self):
    self.__generic_name = ""
    self.__brand_name = ""
    self.__category = ""
    self.__price = 0.00
    self.__sku = 0

  #Creating getters and setters 
  def get_generic_name(self):
      return self.__generic_name
  
  def set_generic_name(self, generic_name):
      self.__generic_name = generic_name
  
  def get_brand_name(self):
      return self.__brand_name
  
  def set_brand_name(self, brand_name):
      self.__brand_name = brand_name
  
  def get_category(self):
      return self.__category
  
  def set_category(self, category):
      self.__category = category
  
  def get_price(self):
      return self.__price
  
  def set_price(self, price):
    assert price > 0.0, "price can not be negative"
    self.__price = price
  
  def get_sku(self):
    return self.__sku
  
  def set_sku(self, sku):
    assert sku > 0, "sku number can not be negative"
    self.__sku = sku

  def display_produce(self):
    return "Produce Information: " + self.__generic_name + " | " + self.__brand_name + " | " + self.__category + " | " + str(self.__price) + " | " + str(self.__sku)
