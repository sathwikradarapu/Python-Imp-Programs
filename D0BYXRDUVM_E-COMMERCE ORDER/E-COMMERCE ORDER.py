class product:
    def __init__(self,Name,Price,Deal_Price,Rating):
         self.Name=Name
         self.Price=Price
         self.Deal_Price=Deal_Price
         self.Rating=Rating
         self.you_saved=Price-Deal_Price
    def display_product_Details(self):
        print("Product:{}".format(self.Name))
        print("Price:{}".format(self.Price))
        print("Deal Price:{}".format(self.Deal_Price))
        print("Rating:{}".format(self.Rating))
        print("You Saved:{}".format(self.you_saved))
class ElectronicItem(product):
    def __init__(self,Name,Price,Deal_Price,Rating,warranty_in_months):
        super().__init__(Name,Price,Deal_Price,Rating)
        self.warranty_in_months=warranty_in_months
    def display_product_Details(self):
        super().display_product_Details()
        print("warranty:{} months".format(self.warranty_in_months))
        print("")
class GroceryItem(product):
    def __init__(self,Name,Price,Deal_Price,Rating,Expiry_date):
        super().__init__(Name,Price,Deal_Price,Rating)
        self.Expiry_date=Expiry_date
    def display_product_Details(self):
        super().display_product_Details()
        print("Expiry Date:{}".format(self.Expiry_date))
        print("")
class order:
    delivery_charges={
        "Prime":100,
        "Normal":0
    }
    def __init__(self,delivery_method,delivery_address):
        self.delivery_method=delivery_method
        self.delivery_address=delivery_address
        self.items_in_cart=[]
    def add_items(self,product,quantity):
        item=(product,quantity)
        self.items_in_cart.append(item)
    def display_order_details(self):
        print("Delivery Method:{}".format(self.delivery_method))
        print("Delivery Address:{}".format(self.delivery_address))
        for product,quantity in self.items_in_cart:
            product.display_product_Details()
            print("quantity:{}".format(quantity))
            print("")
e=ElectronicItem("Tv",40000,38000,4.5,24)
g=GroceryItem("Chocolate",100,90,5,"10/2024")
my_order=order("Normal","Karimnagar")
my_order.add_items("Tv",1)
my_order.add_items("Chocolate",3)
my_order.display_order_details()