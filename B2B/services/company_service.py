from B2B import CompaniesRepository

class CompaniesService:

    @staticmethod
    def register(company):
        return CompaniesRepository.add(company)

    @staticmethod
    def get_all():
        return CompaniesRepository.get_all()

    @staticmethod
    def get_by_id(company_id):
        return CompaniesRepository.get_by_id(company_id)

    @staticmethod
    def update(company):
        return CompaniesRepository.update(company)

    @staticmethod
    def delete(company_id):
        return CompaniesRepository.delete(company_id)

    @staticmethod
    def authenticate(login, password):
        return CompaniesRepository.authenticate(login, password)

    @staticmethod
    def search_by_name(name):
        return CompaniesRepository.search_by_name(name)