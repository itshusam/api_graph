from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)




class Product:
    _id_counter = 1 

    def __init__(self, name, price, quantity, category):
        self.id = Product._id_counter
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category
        Product._id_counter += 1  


inventory = []

def get_all_products():
    return inventory

def add_product(name, price, quantity, category):
    product = Product(name, price, quantity, category)
    inventory.append(product)
    return product

def update_product(product_id, name=None, price=None, quantity=None, category=None):
    for product in inventory:
        if product.id == product_id:
            if name:
                product.name = name
            if price is not None:  
                product.price = price
            if quantity is not None: 
                product.quantity = quantity
            if category:
                product.category = category
            return product
    return None

def delete_product(product_id):
    global inventory
    for product in inventory:
        if product.id == product_id:
            inventory.remove(product)
            return product
    return None
