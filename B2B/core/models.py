class Company:
    def __init__(self, id=None, name=None, email=None, login=None, password=None):
        self.id = id
        self.name = name
        self.email = email
        self.login = login
        self.password = password

    def __str__(self):
        return f"Компания: {self.name} (ID: {self.id})"


class Product:
    def __init__(self, id=None, company_id=None, name=None, description=None,
                 price=None, category=None, stock=None, is_available=None):
        self.id = id
        self.company_id = company_id
        self.name = name
        self.description = description
        self.price = price
        self.category = category
        self.stock = stock
        self.is_available = is_available

    def __str__(self):
        return (f"Товар {self.name} (ID: {self.id})\n"
                f"Описание: {self.description}\n"
                f"Цена: {self.price} руб., Остаток: {self.stock} шт.\n"
                f"Категория: {self.category}, Доступен: {'Да' if self.is_available else 'Нет'}")


class Order:
    def __init__(self, id=None, buyer_id=None, seller_id=None, product_id=None,
                 quantity=None, price=None, status=None):
        self.id = id
        self.buyer_id = buyer_id
        self.seller_id = seller_id
        self.product_id = product_id
        self.quantity = quantity
        self.price = price
        self.status = status

    def __str__(self):
        return (f"Заказ №{self.id}\n"
                f"Покупатель: {self.buyer_id}, Продавец: {self.seller_id}\n"
                f"Товар: {self.product_id}, Количество: {self.quantity}\n"
                f"Сумма: {self.price} руб., Статус: {self.status}")