from B2B.core.models import Product, Order
from B2B import ProductsService, OrdersService


class UserManagement:
    @staticmethod
    def add_product(company_id):
        """Добавление нового продукта"""
        print("\n--- Добавление нового товара ---")
        try:
            product = Product(
                company_id=company_id,
                name=input("Название товара: "),
                description=input("Описание (необязательно): ") or None,
                price=float(input("Цена за единицу: ")),
                category=input("Категория: "),
                stock=int(input("Количество на складе: ")),
                is_available=True
            )
            product_id = ProductsService.add(product)
            if product_id:
                print(f"Товар успешно добавлен! ID: {product_id}")
            return product_id
        except ValueError:
            print("Ошибка ввода числового значения")
            return None

    @staticmethod
    def update_product(company_id):
        """Обновление информации о продукте"""
        print("\n--- Обновление товара ---")
        products = ProductsService.get_by_company(company_id)
        if not products:
            print("У вас нет товаров для редактирования")
            return

        print("Ваши товары:")
        for idx, product in enumerate(products, 1):
            print(f"{idx}. {product.name} (ID: {product.id})")

        try:
            choice = int(input("Выберите номер товара для редактирования: ")) - 1
            if 0 <= choice < len(products):
                product = products[choice]
                print(f"\nТекущие данные товара:\n{product}")

                # Запрашиваем новые данные
                new_name = input(f"Новое название [{product.name}]: ") or product.name
                new_desc = input(f"Новое описание [{product.description}]: ") or product.description
                new_price = float(input(f"Новая цена [{product.price}]: ") or product.price)
                new_category = input(f"Новая категория [{product.category}]: ") or product.category
                new_stock = int(input(f"Новое количество [{product.stock}]: ") or product.stock)
                available = input(f"Доступен для заказа (да/нет) [{'да' if product.is_available else 'нет'}]: ")
                new_available = available.lower() == 'да' if available else product.is_available

                # Обновляем продукт
                updated_product = Product(
                    id=product.id,
                    company_id=company_id,
                    name=new_name,
                    description=new_desc,
                    price=new_price,
                    category=new_category,
                    stock=new_stock,
                    is_available=new_available
                )

                ProductsService.update(updated_product)
                print("Товар успешно обновлен!")
            else:
                print("Неверный выбор товара")
        except ValueError:
            print("Ошибка ввода. Введите число.")

    @staticmethod
    def delete_product(company_id):
        """Удаление продукта"""
        print("\n--- Удаление товара ---")
        products = ProductsService.get_by_company(company_id)
        if not products:
            print("У вас нет товаров для удаления")
            return

        print("Ваши товары:")
        for idx, product in enumerate(products, 1):
            print(f"{idx}. {product.name} (ID: {product.id})")

        try:
            choice = int(input("Выберите номер товара для удаления: ")) - 1
            if 0 <= choice < len(products):
                product = products[choice]
                confirm = input(f"Вы уверены, что хотите удалить товар '{product.name}'? (да/нет): ")
                if confirm.lower() == 'да':
                    ProductsService.delete(product.id)
                    print("Товар успешно удален")
                else:
                    print("Удаление отменено")
            else:
                print("Неверный выбор товара")
        except ValueError:
            print("Ошибка ввода. Введите число.")

    @staticmethod
    def view_products(company_id):
        """Просмотр своих товаров"""
        print("\n--- Ваши товары ---")
        products = ProductsService.get_by_company(company_id)
        if products:
            for product in products:
                print(f"\n{product}")
        else:
            print("У вас пока нет товаров")

    @staticmethod
    def browse_products(company_id):
        """Просмотр товаров других компаний"""
        print("\n--- Товары других компаний ---")
        products = ProductsService.get_other_products(company_id)
        if products:
            for idx, product in enumerate(products, 1):
                print(f"\n{idx}. Компания: {product[2]}")
                print(f"Товар: {product[3]}")
                print(f"Описание: {product[4]}")
                print(f"Цена: {product[5]} руб., Остаток: {product[6]} шт.")
            return products
        else:
            print("Нет доступных товаров")
            return []

    @staticmethod
    def create_order(company_id):
        """Создание нового заказа"""
        print("\n--- Создание заказа ---")
        products = UserManagement.browse_products(company_id)
        if not products:
            return

        try:
            choice = int(input("Выберите номер товара для заказа: ")) - 1
            if 0 <= choice < len(products):
                selected = products[choice]
                max_quantity = selected[6]  # stock

                try:
                    quantity = int(input(f"Введите количество (доступно {max_quantity}): "))
                    if quantity <= 0:
                        print("Количество должно быть положительным")
                        return
                    if quantity > max_quantity:
                        print("Недостаточно товара на складе")
                        return

                    total_price = quantity * selected[5]  # price

                    order = Order(
                        buyer_id=company_id,
                        seller_id=selected[1],  # company_id продавца
                        product_id=selected[0],  # product_id
                        quantity=quantity,
                        price=total_price,
                        status="new"
                    )

                    order_id = OrdersService.create(order)
                    if order_id:
                        print(f"Заказ успешно создан! Номер заказа: {order_id}")
                        print(f"Сумма к оплате: {total_price} руб.")
                except ValueError:
                    print("Ошибка ввода количества")
            else:
                print("Неверный выбор товара")
        except ValueError:
            print("Ошибка ввода. Введите число.")

    @staticmethod
    def view_orders(company_id, as_buyer=True):
        """Просмотр заказов"""
        if as_buyer:
            print("\n--- Ваши заказы (как покупатель) ---")
            orders = OrdersService.get_buyer_orders(company_id)
        else:
            print("\n--- Ваши заказы (как продавец) ---")
            orders = OrdersService.get_seller_orders(company_id)

        if orders:
            for order in orders:
                print(f"\n{order}")
        else:
            role = "покупателя" if as_buyer else "продавца"
            print(f"У вас нет заказов в роли {role}")