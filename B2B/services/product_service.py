from B2B import ProductsRepository

class ProductsService:
    @staticmethod
    def add(product):
        return ProductsRepository.add(product)

    @staticmethod
    def get_all():
        return ProductsRepository.get_all()

    @staticmethod
    def get_by_id(product_id):
        return ProductsRepository.get_by_id(product_id)

    @staticmethod
    def update(product):
        return ProductsRepository.update(product)

    @staticmethod
    def delete(product_id):
        return ProductsRepository.delete(product_id)

    @staticmethod
    def get_by_company(company_id):
        return ProductsRepository.get_by_company(company_id)

    @staticmethod
    def search(name, company_id=None):
        return ProductsRepository.search(name, company_id)

    @staticmethod
    def get_other_products(company_id):
        return ProductsRepository.get_other_products(company_id)