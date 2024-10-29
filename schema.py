from graphene import ObjectType, String, Float, Int, List, Field, Mutation, Schema, ID
from models import *


class Product(ObjectType):
    id = ID(required=True)
    name = String(required=True)
    price = Float(required=True)
    quantity = Int(required=True)
    category = String(required=True)

class Query(ObjectType):
    products = List(Product)

    def resolve_products(self, info):
        return get_all_products()

class CreateProduct(Mutation):
    class Arguments:
        name = String(required=True)
        price = Float(required=True)
        quantity = Int(required=True)
        category = String(required=True)

    product = Field(Product)

    def mutate(self, info, name, price, quantity, category):
        product = add_product(name, price, quantity, category)
        return CreateProduct(product=product)

class UpdateProduct(Mutation):
    class Arguments:
        id = ID(required=True)
        name = String()
        price = Float()
        quantity = Int()
        category = String()

    product = Field(Product)

    def mutate(self, info, id, name=None, price=None, quantity=None, category=None):
        product = update_product(int(id), name, price, quantity, category)
        return UpdateProduct(product=product)

class DeleteProduct(Mutation):
    class Arguments:
        id = ID(required=True)

    product = Field(Product)

    def mutate(self, info, id):
        product = delete_product(int(id))
        return DeleteProduct(product=product)


class Mutation(ObjectType):
    create_product = CreateProduct.Field()
    update_product = UpdateProduct.Field()
    delete_product = DeleteProduct.Field()


schema = Schema(query=Query, mutation=Mutation)
