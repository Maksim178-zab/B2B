from B2B import CompaniesService, ProductsService, OrdersService

class AdminManagement:
    @staticmethod
    def manage_companies():
        """Управление компаниями в системе"""
        while True:
            print("\n--- Управление компаниями ---")
            print("1. Просмотр всех компаний")
            print("2. Поиск компании по названию")
            print("3. Блокировка компании")
            print("4. Удаление компании")
            print("0. Назад")

            choice = input("Выберите действие: ")

            if choice == "1":
                AdminManagement.view_all_companies()
            elif choice == "2":
                AdminManagement.search_company()
            elif choice == "3":
                AdminManagement.block_company()
            elif choice == "4":
                AdminManagement.delete_company()
            elif choice == "0":
                break
            else:
                print("Неверный выбор. Попробуйте снова.")

    @staticmethod
    def view_all_companies():
        """Просмотр всех зарегистрированных компаний"""
        print("\n--- Список всех компаний ---")
        companies = CompaniesService.get_all()
        if companies:
            for company in companies:
                print(f"ID: {company.id}, Название: {company.name}, Email: {company.email}")
        else:
            print("В системе нет зарегистрированных компаний")

    @staticmethod
    def search_company():
        """Поиск компании по названию"""
        name = input("Введите название компании (или часть названия): ")
        company_ids = CompaniesService.search_by_name(name)
        if company_ids:
            print("\nНайденные компании:")
            for company_id in company_ids:
                company = CompaniesService.get_by_id(company_id)
                print(f"ID: {company.id}, Название: {company.name}")
        else:
            print("Компании с таким названием не найдены")

    @staticmethod
    def block_company():
        """Блокировка компании"""
        company_id = input("Введите ID компании для блокировки: ")
        try:
            company_id = int(company_id)
            company = CompaniesService.get_by_id(company_id)
            if company:
                # В реальной системе здесь должна быть логика блокировки
                # Например, добавление поля is_blocked в модель Company
                print(f"Компания '{company.name}' заблокирована")
            else:
                print("Компания с таким ID не найдена")
        except ValueError:
            print("ID компании должен быть числом")

    @staticmethod
    def delete_company():
        """Удаление компании"""
        company_id = input("Введите ID компании для удаления: ")
        try:
            company_id = int(company_id)
            company = CompaniesService.get_by_id(company_id)
            if company:
                confirm = input(f"Вы уверены, что хотите удалить компанию '{company.name}'? (да/нет): ")
                if confirm.lower() == 'да':
                    CompaniesService.delete(company_id)
                    print("Компания успешно удалена")
                else:
                    print("Удаление отменено")
            else:
                print("Компания с таким ID не найдена")
        except ValueError:
            print("ID компании должен быть числом")

    @staticmethod
    def manage_products():
        """Управление товарами в системе"""
        while True:
            print("\n--- Управление товарами ---")
            print("1. Просмотр всех товаров")
            print("2. Поиск товара по названию")
            print("3. Блокировка товара")
            print("4. Удаление товара")
            print("0. Назад")

            choice = input("Выберите действие: ")

            if choice == "1":
                AdminManagement.view_all_products()
            elif choice == "2":
                AdminManagement.search_product()
            elif choice == "3":
                AdminManagement.block_product()
            elif choice == "4":
                AdminManagement.delete_product()
            elif choice == "0":
                break
            else:
                print("Неверный выбор. Попробуйте снова.")

    @staticmethod
    def view_all_products():
        """Просмотр всех товаров в системе"""
        print("\n--- Список всех товаров ---")
        products = ProductsService.get_all()
        if products:
            for product in products:
                company = CompaniesService.get_by_id(product.company_id)
                print(f"ID: {product.id}, Название: {product.name}")
                print(f"Компания: {company.name if company else 'Неизвестна'}")
                print(f"Цена: {product.price}, Остаток: {product.stock}\n")
        else:
            print("В системе нет товаров")

    @staticmethod
    def search_product():
        """Поиск товара по названию"""
        name = input("Введите название товара (или часть названия): ")
        products = ProductsService.search(name)
        if products:
            print("\nНайденные товары:")
            for product in products:
                company = CompaniesService.get_by_id(product.company_id)
                print(f"ID: {product.id}, Название: {product.name}")
                print(f"Компания: {company.name if company else 'Неизвестна'}\n")
        else:
            print("Товары с таким названием не найдены")

    @staticmethod
    def block_product():
        """Блокировка товара"""
        product_id = input("Введите ID товара для блокировки: ")
        try:
            product_id = int(product_id)
            product = ProductsService.get_by_id(product_id)
            if product:
                product.is_available = False
                ProductsService.update(product)
                print(f"Товар '{product.name}' заблокирован и больше не доступен для заказа")
            else:
                print("Товар с таким ID не найден")
        except ValueError:
            print("ID товара должен быть числом")

    @staticmethod
    def delete_product():
        """Удаление товара"""
        product_id = input("Введите ID товара для удаления: ")
        try:
            product_id = int(product_id)
            product = ProductsService.get_by_id(product_id)
            if product:
                confirm = input(f"Вы уверены, что хотите удалить товар '{product.name}'? (да/нет): ")
                if confirm.lower() == 'да':
                    ProductsService.delete(product_id)
                    print("Товар успешно удален")
                else:
                    print("Удаление отменено")
            else:
                print("Товар с таким ID не найден")
        except ValueError:
            print("ID товара должен быть числом")

    @staticmethod
    def manage_orders():
        """Управление заказами в системе"""
        while True:
            print("\n--- Управление заказами ---")
            print("1. Просмотр всех заказов")
            print("2. Поиск заказов по компании")
            print("3. Изменение статуса заказа")
            print("4. Отмена заказа")
            print("0. Назад")

            choice = input("Выберите действие: ")

            if choice == "1":
                AdminManagement.view_all_orders()
            elif choice == "2":
                AdminManagement.search_orders_by_company()
            elif choice == "3":
                AdminManagement.change_order_status()
            elif choice == "4":
                AdminManagement.cancel_order()
            elif choice == "0":
                break
            else:
                print("Неверный выбор. Попробуйте снова.")

    @staticmethod
    def view_all_orders():
        """Просмотр всех заказов в системе"""
        print("\n--- Список всех заказов ---")
        orders = OrdersService.get_all()
        if orders:
            for order in orders:
                buyer = CompaniesService.get_by_id(order.buyer_id)
                seller = CompaniesService.get_by_id(order.seller_id)
                product = ProductsService.get_by_id(order.product_id)

                print(f"\nЗаказ №{order.id}")
                print(f"Покупатель: {buyer.name if buyer else 'Неизвестен'}")
                print(f"Продавец: {seller.name if seller else 'Неизвестен'}")
                print(f"Товар: {product.name if product else 'Товар удален'}")
                print(f"Количество: {order.quantity}, Сумма: {order.price}")
                print(f"Статус: {order.status}")
        else:
            print("В системе нет заказов")

    @staticmethod
    def search_orders_by_company():
        """Поиск заказов по компании"""
        company_id = input("Введите ID компании: ")
        try:
            company_id = int(company_id)
            company = CompaniesService.get_by_id(company_id)
            if company:
                print(f"\nЗаказы компании '{company.name}':")

                print("\nКак покупатель:")
                buyer_orders = OrdersService.get_buyer_orders(company_id)
                if buyer_orders:
                    for order in buyer_orders:
                        print(f"Заказ №{order.id} - Сумма: {order.price} - Статус: {order.status}")
                else:
                    print("Нет заказов как покупатель")

                print("\nКак продавец:")
                seller_orders = OrdersService.get_seller_orders(company_id)
                if seller_orders:
                    for order in seller_orders:
                        print(f"Заказ №{order.id} - Сумма: {order.price} - Статус: {order.status}")
                else:
                    print("Нет заказов как продавец")
            else:
                print("Компания с таким ID не найдена")
        except ValueError:
            print("ID компании должен быть числом")

    @staticmethod
    def change_order_status():
        """Изменение статуса заказа"""
        order_id = input("Введите ID заказа: ")
        try:
            order_id = int(order_id)
            order = OrdersService.get_by_id(order_id)
            if order:
                print(f"\nТекущий статус заказа №{order.id}: {order.status}")
                print("Доступные статусы: new, processing, shipped, delivered, cancelled")
                new_status = input("Введите новый статус: ")

                if new_status.lower() in ['new', 'processing', 'shipped', 'delivered', 'cancelled']:
                    order.status = new_status.lower()
                    OrdersService.update(order)
                    print("Статус заказа успешно обновлен")
                else:
                    print("Неверный статус")
            else:
                print("Заказ с таким ID не найден")
        except ValueError:
            print("ID заказа должен быть числом")

    @staticmethod
    def cancel_order():
        """Отмена заказа"""
        order_id = input("Введите ID заказа для отмены: ")
        try:
            order_id = int(order_id)
            order = OrdersService.get_by_id(order_id)
            if order:
                confirm = input(f"Вы уверены, что хотите отменить заказ №{order.id}? (да/нет): ")
                if confirm.lower() == 'да':
                    order.status = 'cancelled'
                    OrdersService.update(order)
                    print("Заказ успешно отменен")
                else:
                    print("Отмена заказа отменена")
            else:
                print("Заказ с таким ID не найден")
        except ValueError:
            print("ID заказа должен быть числом")

    @staticmethod
    def show_statistics():
        """Показать статистику системы"""
        print("\n--- Статистика системы ---")

        # Количество компаний
        companies = CompaniesService.get_all()
        print(f"Всего компаний: {len(companies)}")

        # Количество товаров
        products = ProductsService.get_all()
        print(f"Всего товаров: {len(products)}")

        # Количество заказов
        orders = OrdersService.get_all()
        print(f"Всего заказов: {len(orders)}")

        # Статистика по статусам заказов
        if orders:
            status_counts = {}
            for order in orders:
                status_counts[order.status] = status_counts.get(order.status, 0) + 1

            print("\nСтатусы заказов:")
            for status, count in status_counts.items():
                print(f"{status}: {count}")