import sqlite3
from datetime import datetime

CONN = sqlite3.connect('inventory.db')
CURSOR = CONN.cursor()

class Sale:

    all = {}

    def __init__(self, product_id, quantity_sold, sale_date = None, id = None):
        self.id = id
        self.product_id = product_id
        self.quantity_sold = quantity_sold
        self.sale_date = sale_date or datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def __repr__(self):
        return f'SaleID {self.id} - productID {self.product_id},  Quantity sold: {self.quantity_sold},  sale Date : {self.sale_date}'
    
    def save(self):
        """ Insert a new row with the sale_id value of the current Sale instance.
        Update object id attribute using the primary key value of the new row.
        Save the object in the local dictionary using the table row's PK as the dictionary key """
        sql = """
            INSERT INTO sales (product_id, quantity_sold, sale_date) VALUES (?, ?, ?)
        """

        CURSOR.execute(sql, (self.product_id, self.quantity_sold, self.sale_date))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
    
    @classmethod
    def create_sale(cls, product_id,quantity_sold, sale_date = None):
        """ Initialize a new sale instance and save the object to the database """
        new_sale = cls(product_id, quantity_sold, sale_date)
        new_sale.save()
        return new_sale

    @classmethod
    def instance_from_db(cls, row):
        """Return a sale object having the attribute values from the table row."""

        # Check the dictionary for  existing instance using the row's primary key
        sale = cls.all.get(row[0])
        if sale:
            # ensure attributes match row values in case local instance was modified
            sale.product_id = row[1]
            sale.quantity_sold = row[2]
            sale.sale_date = row[3]
        else:
            # not in dictionary, create new instance and add to dictionary
            sale = cls(row[1], row[2], row[3])
            sale.id = row[0]
            cls.all[sale.id] = sale
        return sale
    
    @classmethod
    def get_all_sales(cls):
        """Return a list containing one sale object per table row"""
        sql = """
            SELECT *
            FROM sales
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_sale_by_id(cls, id):
        """Return sale object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM sales
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    def delete(self):
        """Delete the table row corresponding to the current sale instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM sales
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        # Set the id to None
        self.id = None
        
    

