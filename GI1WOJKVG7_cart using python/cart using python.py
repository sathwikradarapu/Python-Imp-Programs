class cart:
    def __init__(self):
        self.items={}
        self.price={"Book":10,"Pen":5}
    def add_items(self,item_name,quantity):
        self.items[item_name]=quantity
    def remove_items(self,item_name):
        del self.items[item_name]
    def update_items(self,item_name,quantity):
         self.items[item_name]=quantity
    def print_items(self):
        print(self.items)
    def print_price(self):
        total_price=0
        for item_name,quantity in self.items.items():
            total_price+=self.price[item_name]*quantity
        print(total_price)
cart_obj=cart()
cart_obj.add_items("Book",7)
cart_obj.print_items()
cart_obj.add_items("Pen",3)
cart_obj.print_items()
cart_obj.remove_items("Pen")
cart_obj.print_items()
cart_obj.update_items("Book",2)
cart_obj.print_items()
cart_obj.add_items("Pen",10)
cart_obj.print_items()
cart_obj.print_price()