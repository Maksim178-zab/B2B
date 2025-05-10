from B2B.managaments.auth import authenticate, register
from B2B.managaments.user_management import UserManagement
from B2B.managaments.admin_management import AdminManagement


class MainMenu:
    @staticmethod
    def show_auth_menu():
        """Меню аутентификации"""
        while True:
            print("\n=== B2B Платформа ===")
            print("1. Вход")
            print("2. Регистрация")
            print("0. Выход")

            choice = input("Выберите действие: ")

            if choice == "1":
                company = authenticate()
                if company:
                    if company.login == "admin":  # Проверка на администратора
                        MainMenu.show_admin_menu()
                    else:
                        MainMenu.show_user_menu(company)
            elif choice == "2":
                register()
            elif choice == "0":
                print("До свидания!")
                break
            else:
                print("Неверный выбор. Попробуйте снова.")

    @staticmethod
    def show_admin_menu():
        """Меню администратора"""
        while True:
            print("\n=== Административное меню ===")
            print("1. Управление компаниями")
            print("2. Управление товарами")
            print("3. Управление заказами")
            print("4. Просмотр статистики")
            print("0. Выход")

            choice = input("Выберите действие: ")

            if choice == "1":
                AdminManagement.manage_companies()
            elif choice == "2":
                AdminManagement.manage_products()
            elif choice == "3":
                AdminManagement.manage_orders()
            elif choice == "4":
                AdminManagement.show_statistics()
            elif choice == "0":
                print("Выход из административного меню")
                break
            else:
                print("Неверный выбор. Попробуйте снова.")

    @staticmethod
    def show_user_menu(company):
        """Меню пользователя после входа"""
        while True:
            print(f"\n=== Главное меню ({company.name}) ===")
            print("1. Мои товары")
            print("2. Добавить товар")
            print("3. Редактировать товар")
            print("4. Удалить товар")
            print("5. Просмотр товаров других компаний")
            print("6. Создать заказ")
            print("7. Мои заказы (как покупатель)")
            print("8. Мои заказы (как продавец)")
            print("0. Выход")

            choice = input("Выберите действие: ")

            if choice == "1":
                UserManagement.view_products(company.id)
            elif choice == "2":
                UserManagement.add_product(company.id)
            elif choice == "3":
                UserManagement.update_product(company.id)
            elif choice == "4":
                UserManagement.delete_product(company.id)
            elif choice == "5":
                UserManagement.browse_products(company.id)
            elif choice == "6":
                UserManagement.create_order(company.id)
            elif choice == "7":
                UserManagement.view_orders(company.id, as_buyer=True)
            elif choice == "8":
                UserManagement.view_orders(company.id, as_buyer=False)
            elif choice == "0":
                print(f"До свидания, {company.name}!")
                break
            else:
                print("Неверный выбор. Попробуйте снова.")