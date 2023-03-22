from classes.order import Order

class Coffee:
    def __init__(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            raise Exception ("name must be a string")
    def get_name(self):
        return self._name
    def set_name(self, name):
        print("name cannot be changed")
    name = property(get_name, set_name)
    def orders(self):
        new_list = []
        for orders in Order.all:
            print(orders.coffee)
            if isinstance(orders.coffee, Coffee):
                new_list.append(orders)
        return new_list
    def customers(self):
        new_list = []
        from .customer import Customer
        for orders in Order.all:
            if isinstance(orders.coffee, Coffee) and isinstance(orders.customer, Customer):
                if orders.customer.name not in new_list:
                    new_list.append(orders.customer.name)
        return new_list
    def num_orders(self):
        count = 0
        for orders in Order.all:
            if orders.coffee == self:
                count += 1
        return count
    def average_price(self):
        price_list = []
        count = 0
        for orders in Order.all:
            if orders.coffee == self:
                price_list.append(orders.price)
                count += 1
        return sum(price_list)/count
                
        


    