from typing import List
from datetime import date

from merchant import Merchant


class Offer:
    def __init__(self, id: int, title: str, description: str, category: int, valid_to: date, merchants: List[Merchant]) -> None:
        self._id  = id
        self._title = title
        self._description = description
        self._category = category
        self._valid_to = valid_to
        self._merchants = merchants
    
    @property
    def id(self) -> int:
        return self._id

    @property
    def title(self) -> str:
        return self._title
    
    @property
    def description(self) -> str:
        return self._description

    @property
    def category(self) -> int:
        return self._category   
    
    @property
    def valid_to(self) -> date:
        return self._valid_to
    
    @property
    def merchants(self) -> List[Merchant]:
        return self._merchants
