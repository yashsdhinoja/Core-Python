class Product: # class define
    marketplace = "Global_Market" # attribute class

    def __init__(self, product_name, category, starting_price): # constructor
        self.product_name = product_name
        self.category = category
        self.__starting_price = starting_price # private attribute

    def updates(self, discount_amount): # instance
        self.__starting_price -= discount_amount
        print(f"You Purchase :{self.product_name} in that Product price is:{discount_amount}, with Discount : {self.__starting_price}")

    @staticmethod
    def support():
        print("If Any Issues call on Generic Customer suppport helpine Message: +91 1236547890")    

P1 = Product("David Off Coffee","Rich Aroma",799)
P2 = Product("Nesscafe Coffee","Gold",890)

print(Product.marketplace)
print("="*30)

P1.updates(12)
P1.support()

print("="*30)

P2.updates(32)
P2.support()

print("="*30)