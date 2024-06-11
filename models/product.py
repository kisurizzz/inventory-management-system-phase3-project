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
            f"<Product {self.id}: {self.name}, {self.price}, " +
            f"Product ID: {self.category_id}>"
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
            raise AttributeError ('Price of product must be an integer ')
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
    def create(cls, name, price, stock, category_id):
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
    

# product1 = Product("soda", 80, 120, 4)
# product1.save()
# print(Product.all)