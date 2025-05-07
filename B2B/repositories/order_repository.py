from B2B import db, Order

class OrdersRepository:
    @staticmethod
    def add(order):
        db.cursor.execute("""INSERT INTO Orders 
                          (buyer_id, seller_id, product_id, quantity, price)
                          VALUES(?,?,?,?,?)""",
                          (order.buyer_id, order.seller_id, order.product_id,
                           order.quantity, order.price))
        db.connection.commit()
        return db.cursor.lastrowid

    @staticmethod
    def get_all():
        db.cursor.execute("""SELECT order_id, buyer_id, seller_id, product_id, 
                          quantity, price, status FROM Orders""")
        return [Order(*row) for row in db.cursor.fetchall()]

    @staticmethod
    def get_by_id(order_id):
        db.cursor.execute("""SELECT * FROM Orders WHERE order_id=?""", (order_id,))
        row = db.cursor.fetchone()
        if row:
            return Order(*row)
        return None

    @staticmethod
    def update(order):
        db.cursor.execute("""UPDATE Orders SET 
                          quantity=?, price=?, status=?
                          WHERE order_id=?""",
                          (order.quantity, order.price, order.status, order.id))
        db.connection.commit()

    @staticmethod
    def delete(order_id):
        db.cursor.execute("DELETE FROM Orders WHERE order_id=?", (order_id,))
        db.connection.commit()

    @staticmethod
    def get_by_buyer(buyer_id):
        db.cursor.execute("""SELECT * FROM Orders WHERE buyer_id=?""", (buyer_id,))
        return [Order(*row) for row in db.cursor.fetchall()]

    @staticmethod
    def get_by_seller(seller_id):
        db.cursor.execute("""SELECT * FROM Orders WHERE seller_id=?""", (seller_id,))
        return [Order(*row) for row in db.cursor.fetchall()]