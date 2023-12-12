from typing import List
import heapq

from .offer import Offer
from .merchant import Merchant

class MerchantSelector:
    def __init__(self, merchants: List[Merchant]) -> None:
        self._merchants = merchants
    
    def select(self) -> Merchant:
        best_merchant = None
        for merchant in self._merchants:
            # Assummed that if there are 2 merchants whose distances are equal => choosing the first merchant to appear in the API.
            if best_merchant is None or best_merchant.distance > merchant.distance:
                best_merchant = merchant
        return best_merchant
    
class OfferSelector:
    def __init__(self, target_num_offers: int, included_categories: List[int], offers: List[Offer]) -> None:
        self._offers = offers
        self._included_categories = included_categories
        self._target_num_offers = target_num_offers

    def selectByCategory(self, category: int) -> List[Offer]:
        best_offer = None
        for offer in self._offers:
            if offer.category == category:
                # Assummed that if there are 2 offers of the same category having their best merchant equal to each other -> choosing the first offer to appear in the API.
                if best_offer is None or best_offer.merchants[0].distance > offer.merchants[0].distance:
                    best_offer = offer
        return best_offer

    def select(self) -> List[Offer]:
        offer_heap = []
        for category in self._included_categories:
            offer = self.selectByCategory(category=category)
            if offer is not None:
                heapq.heappush(offer_heap, (offer.merchants[0].distance, offer))
        
        result = []
        cur_target = self._target_num_offers
        while cur_target > 0:
            result.append(heapq.heappop(offer_heap)[1])
            cur_target -= 1
        return result

        


        


        

        


