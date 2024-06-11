# lib/helpers.py
from models.category import Category

def helper_1():
    print("Performing useful function#1.")


def exit_program():
    print("Goodbye!")
    exit()

def create_category():
    name = input("Enter the category's name: ")
    try:
        category = Category.create(name)
        print(f'Success: {category}')
    except Exception as exc:
        print("Error creating category: ", exc)