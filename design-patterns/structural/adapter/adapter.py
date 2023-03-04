#################
# client -> Adapter -> Adaptee
#################


from abc import ABC,abstractmethod


class AbsstractAdapter(ABC):

    @abstractmethod
    def send_request(self):
        pass

class Adaptee:

    def request(self)->str:
        return "Hey this is result"
    
class Adapter(AbsstractAdapter):

    def __init__(self,adaptee:Adaptee):
        self.adaptee = adaptee


    def send_request(self):
        return self.adaptee.request()
    

if __name__ == "__main__":
    adaptee = Adaptee()
    adapter = Adapter(adaptee=adaptee)
    print(adapter.send_request())