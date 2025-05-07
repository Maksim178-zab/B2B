from B2B import db, Product

class ProductsRepository:
    @staticmethod
    def add(product):
        db.cursor.execute("""INSERT INTO Products 
                          (company_id, name, description, price, category, stock, is_available)
                          VALUES (?,?,?,?,?,?,?)""",
                          (product.company_id, product.name, product.description,
                           product.price, product.category, product.stock, product.is_available))
        db.connection.commit()
        return db.cursor.lastrowid

    @staticmethod
    def get_all():
        db.cursor.execute("""SELECT product_id, company_id, name, description, 
                          price, category, stock, is_available FROM Products""")
        return [Product(*row) for row in db.cursor.fetchall()]

    @staticmethod
    def get_by_id(product_id):
        db.cursor.execute("""SELECT * FROM Products WHERE product_id=?""", (product_id,))
        row = db.cursor.fetchone()
        if row:
            return Product(*row)
        return None

    @staticmethod
    def update(product):
        db.cursor.execute("""UPDATE Products SET 
                          name=?, description=?, price=?, category=?, 
                          stock=?, is_available=? 
                          WHERE product_id=?""",
                          (product.name, product.description, product.price,
                           product.category, product.stock, product.is_available, product.id))
        db.connection.commit()

    @staticmethod
    def delete(product_id):
        db.cursor.execute("DELETE FROM Products WHERE product_id=?", (product_id,))
        db.connection.commit()

    @staticmethod
    def get_by_company(company_id):
        db.cursor.execute("""SELECT * FROM Products WHERE company_id=?""", (company_id,))
        return [Product(*row) for row in db.cursor.fetchall()]

    @staticmethod
    def search(name, company_id=None):
        query = "SELECT * FROM Products WHERE name LIKE ?"
        params = (f"%{name}%",)

        if company_id:
            query += " AND company_id=?"
            params += (company_id,)

        db.cursor.execute(query, params)
        return [Product(*row) for row in db.cursor.fetchall()]

    @staticmethod
    def get_other_products(company_id):
        """Получить товары других компаний"""
        db.cursor.execute("""SELECT p.product_id, p.company_id, c.name as company_name, 
                          p.name, p.description, p.price, p.stock
                          FROM Products p
                          JOIN Companies c ON p.company_id = c.company_id
                          WHERE p.company_id != ? AND p.is_available = TRUE
                          ORDER BY p.name""", (company_id,))
        return db.cursor.fetchall()