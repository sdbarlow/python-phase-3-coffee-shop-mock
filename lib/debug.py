#!/usr/bin/env python3
# import ipdb

from classes.customer import Customer
from classes.order import Order
from classes.coffee import Coffee

if __name__ == '__main__':
    print("HELLO! :) let's debug")
    Mocha = Coffee("mocha")
    Espresso = Coffee("espresso")
    Frape = Coffee("frape")
    Mark = Customer("mark")
    Seth = Customer("seth")
    neworder = Order(Seth, Mocha, 5)
    newordert = Order(Mark, Mocha, 9)
    newestorder = Order(Seth, Espresso, 9)
    neworderqqq = Order(Seth, Mocha, 5)
    Seth.create_order(Frape, 5)
    print(Mocha.orders())
    print(Order.all)
    print(neworder.coffee)
    print(Mocha.customers())
    print(Seth.coffees())
    print(Mocha.num_orders())
    print(Mocha.average_price())
    # ipdb.set_trace()
