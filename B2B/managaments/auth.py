from B2B.core.models import Company
from B2B import CompaniesService

ADMIN_LOGIN = "admin"
ADMIN_PASSWORD = "admin123"


def authenticate():
    """Аутентификация пользователя"""
    print("\n--- Вход в систему ---")
    login = input("Логин: ")
    password = input("Пароль: ")

    # Проверка администратора
    if login == ADMIN_LOGIN and password == ADMIN_PASSWORD:
        admin_company = Company(id=0, name="ADMIN", email="admin@system", login=ADMIN_LOGIN, password=ADMIN_PASSWORD)
        print("\nДобро пожаловать, Администратор!")
        return admin_company

    # Проверка обычного пользователя
    company = CompaniesService.authenticate(login, password)
    if company:
        print(f"\nДобро пожаловать, {company.name}!")
        return company
    else:
        print("Неверный логин или пароль")
        return None


def register():
    """Регистрация новой компании"""
    print("\n--- Регистрация компании ---")
    company = Company(
        name=input("Название компании: "),
        email=input("Email: "),
        login=input("Логин: "),
        password=input("Пароль: ")
    )

    company_id = CompaniesService.register(company)
    if company_id:
        print(f"Компания успешно зарегистрирована! ID: {company_id}")
        return company_id
    else:
        print("Ошибка регистрации. Возможно, логин уже занят.")
        return None