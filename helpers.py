# lib/helpers.py
from models.category import Category
from models.product import Product
from models.sale import Sale
from datetime import datetime

def helper_1():
    print("Performing useful function#1.")


def exit_program():
    print("Goodbye!")
    exit()

def list_categories():
    categories = Category.get_all()
    for category in categories:
        print(category)


def create_category():
    name = input("Enter the category's name: ")
    try:
        category = Category.create(name)
        print(f'Success: {category}')
    except Exception as exc:
        print("Error creating category: ", exc)

def find_category_by_name():
    name = input("Enter the category's name: ")
    category = Category.find_by_name(name)
    print(category) if category else print(
        f'category {name} not found')
    
def find_category_by_id():
    # use a trailing underscore not to override the built-in id function
    id_ = input("Enter the category's id: ")
    category = Category.find_by_id(id_)
    print(category) if category else print(f'category {id_} not found')

def update_category():
    id_ = input("Enter the category's id: ")
    if category := Category.find_by_id(id_):
        try:
            name = input("Enter the category's new name: ")
            category.name = name

            category.update()
            print(f'Success: {category}')
        except Exception as exc:
            print("Error updating category: ", exc)
    else:
        print(f'Category {id_} not found')

def delete_category():
    id_ = input("Enter the category's id: ")
    if category := Category.find_by_id(id_):
        category.delete()
        print(f'Category {id_} deleted')
    else:
        print(f'Category {id_} not found')


def list_category_products():
    id_ = input("Enter the category's id to list its products: ")
    if category := Category.find_by_id(id_):
        for product in category.products():
            print(product)
    else:
        print(f'Category {id_} not found')
    



## Product Functions

def create_product():
    name = input("Enter the product's name: ")
    price = int(input("Enter the product's price: "))
    stock = int(input("Enter the product's stock: "))
    category_id = int(input("Enter the product's category id: "))
    try:
        product = Product.create_product(name, price, stock, category_id)
        print(f'Success: {product}')
    except Exception as exc:
        print("Error creating product: ", exc)
    
def list_products():
    products = Product.get_all_products()
    for product in products:
        print(product)

def find_product_by_name():
    name = input("Enter the product's name: ")
    product = Product.find_by_name(name)
    print(product) if product else print(
        f'Product {name} not found')


def find_Product_by_id():
    id_ = input("Enter the Product's id: ")
    product = Product.find_product_by_id(id_)
    print(product) if product else print(f'Product {id_} not found')

def update_product():
    id_ = input("Enter the product's id: ")
    if product := Product.find_product_by_id(id_):
        try:
            name = input("Enter the product's new name: ")
            product.name = name
            
            price = int(input("Enter the product's new price: "))
            product.price = price

            stock = int(input("Enter the product's new available stock: "))
            product.stock = stock
            
            category_id = int(input("Enter the product's new category id: "))
            product.category_id = int(category_id)

            product.update()
            print(f'Success: {product},')
        except Exception as exc:
            print("Error updating product: ", exc)
    else:
        print(f'product {id_} not found')


def delete_product():
    id_ = input("Enter the product's id: ")
    if product := Product.find_product_by_id(id_):
        product.delete()
        print(f'product {id_} deleted')
    else:
        print(f'product {id_} not found')

##sales

def create_sale():
    product_sold_id = int(input("Enter the product's id: "))
    quantity_ = int(input("Enter the product's stock: "))
    sale_date_ = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    try:
        sale = Sale.create_sale(product_sold_id, quantity_, sale_date_ )
        print(f'Success: {sale}')
    except Exception as exc:
        print("Error creating new sale: ", exc)

def list_sales():
    sales = Sale.get_all_sales()
    for sale in sales:
        print(sale)


def find_sale_by_id():
    id_ = int(input("Enter the sales's id: "))
    sale = Sale.find_sale_by_id(id_)
    print(sale) if sale else print(f'Sale object {id_} not found')

def delete_sale():
    id_ = int(input("Enter the sale's id: "))
    if sale := Sale.find_sale_by_id(id_):
        sale.delete()
        print(f'sale {id_} deleted')
    else:
        print(f'sale {id_} not found')