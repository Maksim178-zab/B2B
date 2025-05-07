import sqlite3


class Database:
    def __init__(self, db_name='C:/Users/Пользователь/code/git-lessons/B2B/core/Bis2Bis.db'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self._create_tables()

    def _create_tables(self):
        """Создает таблицы при инициализации"""
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS Companies(
            company_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100) NOT NULL,
            login TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
            )""")

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS Products(
            product_id INTEGER PRIMARY KEY AUTOINCREMENT,
            company_id INTEGER NOT NULL,
            name VARCHAR(100) NOT NULL,
            description TEXT,
            price DECIMAL(10,2) NOT NULL,
            category VARCHAR(50),
            stock INTEGER DEFAULT 0,
            is_available BOOLEAN DEFAULT TRUE,

            FOREIGN KEY (company_id) 
                REFERENCES Companies(company_id) 
                ON DELETE CASCADE)
            """)

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS Orders(
            order_id INTEGER PRIMARY KEY AUTOINCREMENT,
            buyer_id INTEGER NOT NULL,
            seller_id INTEGER NOT NULL,
            product_id INTEGER NOT NULL,
            quantity INTEGER DEFAULT 1,
            price DECIMAL(10,2) NOT NULL,
            status VARCHAR(20) DEFAULT 'new',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY (buyer_id) REFERENCES Companies(company_id),
            FOREIGN KEY (seller_id) REFERENCES Companies(company_id),
            FOREIGN KEY (product_id) REFERENCES Products(product_id) ON DELETE SET NULL)""")

        self.connection.commit()

    def close(self):
        """Закрывает соединение с БД"""
        self.connection.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


# Глобальный экземпляр для простого доступа
db = Database()