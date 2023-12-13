from typing import List
import heapq

from .offer import Offer
from .merchant import Merchant

class MerchantSelector:
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def selectNearestMerchant(merchants: List[Merchant]):
        return min(merchants, key=lambda x: x.distance)

class HeapCreationStrategy:
    def heapCreate(self, offers: List[Offer]):
        raise NotImplementedError("Subclasses must implement this method.")
    
# This is for the future when our selection logic is not only limitted to merchant distance, we can still resuse this approach
class MerchantDistanceHeapCreationStrategy(HeapCreationStrategy):
    def heapCreate(self, offers: List[Offer]):
        offerHeap = []
        for offer in offers:
            bestMerchant = MerchantSelector.selectNearestMerchant(offer.merchants)
            offer.merchants = [bestMerchant]
            heapq.heappush(offerHeap, (bestMerchant.distance, offer))
        return offerHeap
    
class OfferSelector:
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def select(offers: List[Offer], targetNumberOffers: int, heapCreationStrategy: HeapCreationStrategy):
        isVisCategory = {}
        offerHeap = heapCreationStrategy.heapCreate(offers)
    
        result = []
        while len(offerHeap) > 0  and len(result) != targetNumberOffers:
            topCandidate = heapq.heappop(offerHeap)[1]
            if isVisCategory.get(topCandidate.category) is None:
                result.append(topCandidate)
                isVisCategory[topCandidate.category] = 1
        
        return result
            