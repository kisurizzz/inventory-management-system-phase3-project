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
    
category1 = Category("Electronics")
category1.save_to_db()
print(Category.all)