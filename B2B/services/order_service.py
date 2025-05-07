from B2B import OrdersRepository

class OrdersService:
    @staticmethod
    def create(order):
        return OrdersRepository.add(order)

    @staticmethod
    def get_all():
        return OrdersRepository.get_all()

    @staticmethod
    def get_by_id(order_id):
        return OrdersRepository.get_by_id(order_id)

    @staticmethod
    def update(order):
        return OrdersRepository.update(order)

    @staticmethod
    def delete(order_id):
        return OrdersRepository.delete(order_id)

    @staticmethod
    def get_buyer_orders(buyer_id):
        return OrdersRepository.get_by_buyer(buyer_id)

    @staticmethod
    def get_seller_orders(seller_id):
        return OrdersRepository.get_by_seller(seller_id)