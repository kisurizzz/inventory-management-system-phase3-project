import sqlite3

CONN = sqlite3.connect('inventory.db')
CURSOR = CONN.cursor()


class Category:
    # Dictionary of objects saved to the database.
    all = {}

    def __init__(self, name, id=None):
        self.id = id
        self.name = name
    
    def __repr__(self) -> str:
        return f"Category {self.id} : {self.name}"
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError("Name of category must be a non-empty string")
    
    def save_to_db(self):
        """ Insert a new row with the name value of the current Category instance.
        Update object id attribute using the primary key value of the new row.
        Save the object in the local dictionary using the table row's PK as the dictionary key """
        sql = """
            INSERT INTO categories (name)
            VALUES (?)
        """

        CURSOR.execute(sql, (self.name,))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
    
    @classmethod
    def create(cls, name):
        """ Initialize a new category instance and save the object to the database """
        category = cls(name)
        category.save_to_db()
        return category
    
    @classmethod
    def instance_from_db(cls, row):
        """Return a category object having the attribute values from the table row."""

        # Check the dictionary for an existing instance using the row's primary key
        category = cls.all.get(row[0])
        if category:
            # ensure attributes match row values in case local instance was modified
            category.name = row[1]
        else:
            # not in dictionary, create new instance and add to dictionary
            category = cls(row[1])
            category.id = row[0]
            cls.all[category.id] = category
        return category
        
    @classmethod
    def get_all(cls):
        """Return a list containing a Category object per row in the table"""
        sql = """
            SELECT *
            FROM categories
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_name(cls, name):
        """Return a Category object corresponding to first table row matching specified name"""
        sql = """
            SELECT *
            FROM categories
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_id(cls, id):
        """Return a Category object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM categories
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    def update(self):
        """Update the table row corresponding to the current Category instance."""
        sql = """
            UPDATE categories
            SET name = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current category instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM categories
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        # Set the id to None
        self.id = None


    # def productsss(self):
    #     """Return list of products associated with current department"""
    #     from models.product import Product
    #     sql = """
    #         SELECT * FROM products
    #         WHERE category_id = ?
    #     """
    #     CURSOR.execute(sql, (self.id,),)

    #     rows = CURSOR.fetchall()
    #     return [
    #         Product.instance_from_db(row) for row in rows
    #     ]


    def products(self):
        """Return list of products associated with current department"""
        from models.product import Product

        sql = """
            SELECT * FROM products
            WHERE category_id = ?
        """
        CURSOR.execute(sql, (self.id,),)

        rows = CURSOR.fetchall()
        return [
            Product.instance_from_db(row) for row in rows
        ]
    
    # @classmethod
    # def products(cls, id):
    #     """
    #     Property method to retrieve the products of a category.
    #     """
    #     # from models.product import Product

    #     sql = """
    #         SELECT DISTINCT products.id, products.name, products.price, products.stock, products.category_id
    #         FROM products 
    #         INNER JOIN categories ON products.category_id = categories.id
    #         WHERE categories.id = ?
    #     """

    #     row = CURSOR.execute(sql, (id,)).fetchone()
    #     return cls.instance_from_db(row) if row else None




    
# category1 = Category("Clothing")
# category1.save_to_db()
# print(Category.all)