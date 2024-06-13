# Inventory management CLI-ORM project

a simple CLI program that uses ORM and python to manage inventory of products and goods.
 April 11 2024

By **Arnold Kisuri**

## Description

The Inventory Management System is a Command Line Interface (CLI) application designed to help businesses efficiently manage their inventory. This system provides a simple and intuitive way to keep track of products, categories, and sales. With this tool, users can perform various operations to ensure their inventory data is accurate and up-to-date.

### Key Features

Category Management:

* Create, view, update, and delete product categories.
* List all categories.

#### Product Management:

* Add new products with details such as name, price, stock, and category.
* View details of individual products.
* Update product information.
* Delete products.
* List all products.
* Filter and list products by category.

#### Sales Management:

* Record new sales transactions, specifying product, quantity, and sale date.
* View all sales records.

#### Database Management:

* Supports database operations with multiple related tables (categories, products, and sales).
* Ensures data integrity with foreign key constraints.

<https://github.com/kisurizzz/inventory-management-system-phase3-project.git>

## How to Use

### Requirements

* A computer with a terminal and python installed.
* Access to the internet.

### Installation Process

1. Clone this repository using

    ```bash
      git@github.com:kisurizzz/inventory-management-system-phase3-project.git
    ```

    or by downloading a ZIP file of the code.
  
2. The repository, if downloaded as a .zip file will need to be extracted to your preferred location.

3. Navigate to the project folder on your terminal.

4. Install dependencies using Pipenv: pipenv install.

5. Activate the virtual environment: pipenv shell

6. Execute the main script to start the CLI: python cli.py.

7. Follow the on-screen prompts to navigate through the various features of the inventory management system.

### Example Commands:

* Add a new category.
* List all products in a specific category.
* Record a new sale.

## Technologies Used

* Python
* SQL

## Support and Contact Details

Incase of any query, need for collaboration or issues with this code, feel free to reach me at
<arnold.kisuri@student.moringaschool.com>

## License

MIT License

Copyright &copy; 2024 Arnold Kisuri

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.