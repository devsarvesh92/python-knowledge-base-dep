######################################
# S - > Single Responsiblity prin -> Class and Function should have one resp
# O -> Open close principle
# L -> Liskov substitution
# I -> Interface segration
# D -> Dependency Inversion
######################################

from abc import ABC, abstractmethod

class Order:

    def __init__(self) -> None:
        self.items = []
    
    def add_item(self,item:str,quantity:int,price:float)->None:
        self.items.append({'item':item,'quantity':quantity,'price':price})
    
    def total_prize(self):
        return sum([item['quantity']*item['price'] for item in self.items])

    def pay(self,payment_type:str):
        match payment_type:

            case 'credit':
                print(f'paying {self.total_prize()} by credit card')

            case 'debit':
                print(f'paying {self.total_prize()} by debit card')


class AuthProcessor(ABC):

    @abstractmethod
    def auth(self,security_code:str):
        pass

class SMSAuthProcessor(AuthProcessor):

    def __init__(self) -> None:
        pass
        

    def auth(self,security_code:str):
        return True

class PaymentProcessor(ABC):

    @abstractmethod
    def pay(self,order:Order):
        pass


class CreditPaymentProcessor(PaymentProcessor):

    def __init__(self,security_code:str,auth_processor:AuthProcessor) -> None:
        self.security_code = security_code
        self.auth_processor = auth_processor

    def pay(self,order:Order):
        if self.auth_processor.auth(security_code=self.security_code):
            print(f'Paying {order.total_prize()} by credit card and {self.security_code=}')

class DebitPaymentProcessor(PaymentProcessor):
    def __init__(self,security_code:str) -> None:
        self.security_code = security_code

    def pay(self,order:Order):
        print(f'Paying {order.total_prize()} by debit card and {self.security_code=}')

class PaypalPaymentProcessor(PaymentProcessor):
    def __init__(self,email_address:str) -> None:
        self.email_address = email_address

    def pay(self,order:Order):
        print(f'Paying {order.total_prize()} by Paypal and {self.email_address=}')


o = Order()
o.add_item(item='pen',quantity=1,price=10)
o.add_item(item='pencil;',quantity=1,price=20)

payment_processor = CreditPaymentProcessor(security_code=12,auth_processor=SMSAuthProcessor())
payment_processor.pay(order=o)


            
        

