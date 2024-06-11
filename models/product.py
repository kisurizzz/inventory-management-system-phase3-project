import sqlite3

CONN = sqlite3.connect('inventory.db')
CURSOR = CONN.cursor()


class Product:

    all = {}

    def __init__(self, name, price, stock, category_id, id = None) -> None:
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock
        self.category_id = category_id

    def __repr__(self):
        return (
            f"<Product ID {self.id}: Product - {self.name}, Price - Ksh {self.price}, Stock - {self.stock} " +
            f"Category ID: {self.category_id}>"
        )
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError(
                "Product name must be a non-empty string"
            )
    @property
    def price (self):
        return self._price
    
    @price.setter
    def price(self, price):
        if type(price) is int:
            self._price = price
        else:
            raise ValueError ('Price of product must be an integer ')
    @property
    def stock (self):
        return self._stock
    
    @stock.setter
    def stock(self, stock):
        if type(stock) is int:
            self._stock = stock
        else:
            raise AttributeError ('Stock of product must be an integer ')
        
    def save(self):
        """ Insert a new row with the name value of the current Procuct instance.
        Update object id attribute using the primary key value of the new row.
        Save the object in the local dictionary using the table row's PK as the dictionary key """
        sql = """
            INSERT INTO products (name, price, stock, category_id)
            VALUES (?, ?, ?, ?)
        """

        CURSOR.execute(sql, (self.name, self.price, self.stock, self.category_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
    
    @classmethod
    def create_product(cls, name, price, stock, category_id):
        """ Initialize a new product instance and save the object to the database """
        product = cls(name, price, stock, category_id)
        product.save()
        return product
    
    
    @classmethod
    def drop_table(cls):
        """ Drop the table that persists category instances """
        sql = """
            DROP TABLE IF EXISTS products;
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def instance_from_db(cls, row):
        """Return an product object having the attribute values from the table row."""

        # Check the dictionary for  existing instance using the row's primary key
        product = cls.all.get(row[0])
        if product:
            # ensure attributes match row values in case local instance was modified
            product.name = row[1]
            product.price = row[2]
            product.stock = row[3]
            product.category_id = row[4]
        else:
            # not in dictionary, create new instance and add to dictionary
            product = cls(row[1], row[2], row[3], row[4])
            product.id = row[0]
            cls.all[product.id] = product
        return product
    
    @classmethod
    def get_all_products(cls):
        """Return a list containing one product object per table row"""
        sql = """
            SELECT *
            FROM products
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_product_by_id(cls, id):
        """Return product object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM products
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        """Return product object corresponding to first table row matching specified name"""
        sql = """
            SELECT *
            FROM products
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    def update(self):
        """Update the table row corresponding to the current Product instance."""
        sql = """
            UPDATE products
            SET name = ?, price = ?, stock = ?, category_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.price, self.stock, self.category_id,self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Product instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM products
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        # Set the id to None
        self.id = None


# product2 = Product("mens jeans", 1200, 8, 2)
# product2.save()
# print(Product.all)