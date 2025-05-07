from B2B import db, Company

class CompaniesRepository:
    @staticmethod
    def add(company):
        try:
            db.cursor.execute("""INSERT INTO Companies (name, email, login, password)
                VALUES(?,?,?,?)""",
                              (company.name, company.email, company.login, company.password))
            db.connection.commit()
            return db.cursor.lastrowid
        except sqlite3.IntegrityError:
            print("Ошибка: Логин уже существует")
            return None

    @staticmethod
    def get_by_id(company_id):
        db.cursor.execute("SELECT * FROM Companies WHERE company_id = ?", (company_id,))
        row = db.cursor.fetchone()
        if row:
            return Company(*row)
        return None

    @staticmethod
    def get_all():
        db.cursor.execute("SELECT company_id, name, email FROM Companies")
        return [Company(*row) for row in db.cursor.fetchall()]

    @staticmethod
    def update(company):
        db.cursor.execute("""UPDATE Companies SET name=?, email=?, password=? 
                          WHERE company_id=?""",
                          (company.name, company.email, company.password, company.id))
        db.connection.commit()

    @staticmethod
    def delete(company_id):
        db.cursor.execute("DELETE FROM Companies WHERE company_id=?", (company_id,))
        db.connection.commit()

    @staticmethod
    def authenticate(login, password):
        db.cursor.execute("""SELECT company_id, name, email FROM Companies 
                          WHERE login=? AND password=?""",
                          (login, password))
        row = db.cursor.fetchone()
        if row:
            return Company(*row)
        return None

    @staticmethod
    def search_by_name(name):
        db.cursor.execute("SELECT company_id FROM Companies WHERE name LIKE ?",
                          (f"%{name}%",))
        return [row[0] for row in db.cursor.fetchall()]