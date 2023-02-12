from abc import ABC,abstractmethod
from dataclasses import dataclass
from enum import Enum
from typing import Final, Type
import uuid

class Priority(str,Enum):
    HIGH:Final[str] = 'high'
    MEDIUM:Final[str] = 'medium'
    LOW:Final[str]='low'

@dataclass
class SupportTicket:
    heading:str
    details:str
    priority:Priority

    def __post__init__(self):
        self.id = str(uuid.uuid4())
    
    def process(self):
        """
        Process ticket
        """
        print(f"Processing ticket with heading={self.heading}"
        f"details={self.details} and priority {self.priority}")

class TicketOrderingStrategy(ABC):

    def creating_ordering(self,tickets:list[SupportTicket]):
        """
        Selects tickets
        """

class FIFOOrderingStrategy(TicketOrderingStrategy):

    def creating_ordering(self, tickets: list[SupportTicket]):
        return tickets[:]

class LIFOOrderingStarategy(TicketOrderingStrategy):

    def creating_ordering(self, tickets: list[SupportTicket]):
        return reversed(tickets)
    
class PriorityOrderingStrategy(TicketOrderingStrategy):

    def creating_ordering(self, tickets: list[SupportTicket]):
        return sorted(tickets,key=lambda ticket:ticket.priority)


class CustomerSupport:

    def __init__(self) -> None:
        self.tickets = []
    
    def add_ticket(self,ticket:SupportTicket):
        self.tickets.append(ticket)

    def process_tickets(self,ordering_strategy:Type[TicketOrderingStrategy]):
        tickets = ordering_strategy().creating_ordering(self.tickets)

        for ticket in tickets:
            ticket.process()


if __name__ == '__main__':

    cs = CustomerSupport()
    cs.add_ticket(SupportTicket('VPN not working',details='VPN not working',priority=Priority.LOW))
    cs.add_ticket(SupportTicket('Kernal broken',details='IO not working',priority=Priority.HIGH))
    cs.add_ticket(SupportTicket('TCP blocked',details='TCP port blocked',priority=Priority.MEDIUM))

    cs.process_tickets(ordering_strategy=LIFOOrderingStarategy)
