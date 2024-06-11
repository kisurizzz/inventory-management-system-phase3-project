# import CONN, CURSOR
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
    
# category1 = Category("Clothing")
# category1.save_to_db()
# print(Category.all)