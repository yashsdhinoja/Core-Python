class MobileDevices:
    # CLASS ATTRIBUTE: Shared across all objects
    device_category = "Mobile Devices"

    # CONSTRUCTOR
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    # INSTANCE METHOD: Modifies instance data and prints the updated total
    def apply_discount(self, discount_amount):
        self.price -= discount_amount
        print(f"Discount applied: Rs. {discount_amount}")
        print(f"Updated total amount: Rs. {self.price}")

    # STATIC METHOD
    @staticmethod 
    def store_policy():
        print("All phones have a 14-day return policy.")

# OBJECT CREATION (2 Objects)
M1 = MobileDevices("iPhone", "14 Pro Max", 120000)
M2 = MobileDevices("Samsung", "S23 Ultra", 110000)

# TESTING METHODS
print(MobileDevices.device_category)
print(M1.brand)
M1.apply_discount(5000)  # Calls discount method
M1.store_policy()        # Calls static method