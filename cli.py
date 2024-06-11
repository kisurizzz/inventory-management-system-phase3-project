#cli.py


from helpers import (
    exit_program,
    helper_1,
    create_category,
    list_categories,
    find_category_by_name,
    find_category_by_id,
    update_category,
    delete_category,
    create_product,
    list_products,
    find_Product_by_id,
    find_product_by_name,
    update_product,
    delete_product
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_categories()
        elif choice == "2":
            find_category_by_name()
        elif choice == "3":
            find_category_by_id()
        elif choice == '4':
            create_category()
        elif choice == '5':
            update_category()
        elif choice == '6':
            delete_category()
        elif choice == '7':
            list_products()
        elif choice == '8':
            find_product_by_name()
        elif choice == '9':
            find_Product_by_id()
        elif choice == '10':
            create_product()
        elif choice == '11':
            update_product()
        elif choice == '12':
            delete_product()
        elif choice == "14":
            helper_1()
        else:
            print("Invalid choice")


def menu():
    print('*** Suris Inventory Manager ***')
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all category")
    print("2. Find category by name")
    print("3. Find category by id")
    print("4: Create new category")
    print("5: Update category")
    print("6: Delete category")
    print("7. List all products")
    print("8. Find products by name")
    print("9. Find product by id")
    print("10: Create new product")
    print("11: Update product")
    print("12: Delete product")
    print("13: List all products in a category")
    print("13: List all products in a sold")


if __name__ == "__main__":
    main()
