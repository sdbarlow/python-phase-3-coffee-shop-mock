# from classes.order import Order

class Customer:
    def __init__(self, name):
        self.name = name
    def get_name(self):
        return self._name
    def set_name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        else:
            raise Exception ("Name must be a string between 1 and 15 characters long")
    name = property(get_name, set_name)
    def orders(self):
        new_list = []
        from .order import Order
        for orders in Order.all:
            if isinstance(orders.customer, Customer):
                new_list.append(orders)
        return new_list
    def coffees(self):
        new_list = []
        from .order import Order
        for orders in Order.all:
            if isinstance(orders.customer, Customer):
                if orders.coffee.name not in new_list:
                    new_list.append(orders.coffee.name)
        return new_list
    def create_order(self, coffee, price):
        from. order import Order
        return Order(self, coffee, price)
            

    



        

                