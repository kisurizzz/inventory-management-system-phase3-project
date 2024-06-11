from connection  import CONN, CURSOR


def create_tables():

    CURSOR.execute('''
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        );
    ''')
   
    CURSOR.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR NOT NULL,
            price INTEGER NOT NULL,
            stock INTEGER,
            category_id INTEGER,
            FOREIGN KEY (category_id) REFERENCES categories (id)
        );
    ''')

    CURSOR.execute('''
        CREATE TABLE IF NOT EXISTS sales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER NOT NULL,
            quantity_sold INTEGER NOT NULL,
            sale_date DATETIME NOT NULL,
            FOREIGN KEY (product_id) REFERENCES products(id)
        );
    ''')

    CONN.commit()
    CONN.close()


def drop_table():
    """ Drop the table that persists product instances """
    sql = """
        DROP TABLE IF EXISTS products;
    """
    CURSOR.execute(sql)
    CONN.commit()

drop_table()

create_tables()

