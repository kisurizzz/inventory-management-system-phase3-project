# lib/helpers.py
from models.category import Category

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