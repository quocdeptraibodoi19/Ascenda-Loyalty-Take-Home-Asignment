from typing import List, Dict, Callable
from datetime import date, timedelta

from offer import Offer

# This class is following the lazy evaluation pattern 
class OfferFilter:
    def __init__(self, offers: List[Offer]) -> None:
        self._offers = offers
        self._filters = []
    
    def filter(self, filter_func: Callable[[Offer], bool]):
        self._filters.append(filter_func)
        return self
    
    def execute(self) -> List[Offer]:
        result = self._offers
        for func in self._filters:
            result = list(filter(func, result))
        return result

# This class follows Singleton pattern since it doesn't maintain states and it just provides the needed information for the outsiders
class FilterFunctionManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(FilterFunctionManager, cls).__new__(cls)
        return cls._instance
    
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def valid_to_date_filter_function(checkin_date: date, day_gap: int) -> Callable[[Offer], bool]:
        def filter_func(offer: Offer):
            return offer.valid_to >= checkin_date + timedelta(days=day_gap)
        return filter_func

    @staticmethod
    def category_filter_function(mapping_category: Dict[str, int], include_categories: List[str]) -> Callable[[Offer], bool]:
        def filter_func(offer: Offer):
            include_category_ids = []
            for category in include_categories:
                include_category_ids.append(mapping_category[category])
            return offer.category in include_category_ids
        return filter_func
