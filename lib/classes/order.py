
class Order:
    all = []
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        self.all.append(self)
    def get_price(self):
        return self._price
    def set_price(self, input):
        if 1 <= input <= 10:
            self._price = input
        else:
            raise Exception ("price must be between 1 and 10")
    price = property(get_price, set_price)
    def get_customer(self):
        return self._customer
    def set_customer(self, customer):
        from .customer import Customer
        if isinstance(customer, Customer):
            self._customer = customer
        else:
            raise Exception ("Customer must be an instance of customer")
    customer = property(get_customer, set_customer)
    def get_coffee(self):
        return self._coffee
    def set_coffee(self, coffee):
        from .coffee import Coffee
        if isinstance(coffee, Coffee):
            self._coffee = coffee
        else:
            raise Exception ("Coffee must be an instance of Coffee")
    coffee = property(get_coffee, set_coffee)


