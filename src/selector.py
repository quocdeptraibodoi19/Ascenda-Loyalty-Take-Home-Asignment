from typing import List
import heapq

from .offer import Offer
from .merchant import Merchant


class MerchantSelector:
    def __init__(self) -> None:
        pass

    @staticmethod
    def select_nearest_merchant(merchants: List[Merchant]):
        return min(merchants, key=lambda x: x.distance)


class HeapCreationStrategy:
    def heap_create(self, offers: List[Offer]):
        raise NotImplementedError("Subclasses must implement this method.")


# This is for the future when our selection logic is not only limitted to merchant distance, we can still resuse this approach
class MerchantDistanceHeapCreationStrategy(HeapCreationStrategy):
    def heap_create(self, offers: List[Offer]):
        offer_heap = []
        for offer in offers:
            best_merchant = MerchantSelector.select_nearest_merchant(offer.merchants)
            offer.merchants = [best_merchant]
            heapq.heappush(offer_heap, (best_merchant.distance, offer))
        return offer_heap


class OfferSelector:
    def __init__(self) -> None:
        pass

    @staticmethod
    def select(
        offers: List[Offer],
        target_number_offers: int,
        heap_creation_strategy: HeapCreationStrategy,
    ):
        is_vis_category = {}
        offer_heap = heap_creation_strategy.heap_create(offers)

        result = []
        while len(offer_heap) > 0 and len(result) != target_number_offers:
            top_candidate = heapq.heappop(offer_heap)[1]
            if is_vis_category.get(top_candidate.category) is None:
                result.append(top_candidate)
                is_vis_category[top_candidate.category] = 1

        return result
