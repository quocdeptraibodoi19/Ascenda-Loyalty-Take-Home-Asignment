from datetime import datetime
from typing import List

from .offer import Offer, Merchant

class DataParser:
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def parse_offer(offer_data: dict) -> Offer:
        return Offer(
                id=offer_data.get("id"),
                title=offer_data.get("title"),
                description=offer_data.get("description"),
                category=offer_data.get("category"),
                valid_to=datetime.strptime(offer_data.get("valid_to"), "%Y-%m-%d").date(),
                merchants=DataParser.parse_merchants(offer_data.get("merchants", []))
            )

    @staticmethod
    def parse_offers(offers_data: List[dict]) -> List[Offer]:
        return [DataParser.parse_offer(data) for data in offers_data]
    
    @staticmethod
    def reverse_parse_offer(offer: Offer) -> dict:
        return {
            "id": offer.id,
            "title": offer.title,
            "description": offer.description,
            "category": offer.category,
            "valid_to": offer.valid_to.strftime("%Y-%m-%d"),
            "merchants": DataParser.reverse_parse_merchants(offer.merchants)
        }

    @staticmethod
    def reverse_parse_offers(offers: List[Offer]) -> List[dict]:
        return [DataParser.reverse_parse_offer(offer) for offer in offers]
    
    @staticmethod
    def parse_merchant(merchant_data: dict) -> Merchant:
        return Merchant(
                id=merchant_data.get("id"),
                name=merchant_data.get("name"),
                distance=merchant_data.get("distance")
            )

    @staticmethod
    def parse_merchants(merchants_data: List[dict]) -> List[Merchant]:
        return [DataParser.parse_merchant(data) for data in merchants_data]

    @staticmethod
    def reverse_parse_merchant(merchant: Merchant) -> dict:
        return {
            "id": merchant.id,
            "name": merchant.name,
            "distance": merchant.distance
        }

    @staticmethod
    def reverse_parse_merchants(merchants: List[Merchant]) -> List[dict]:
        return [DataParser.reverse_parse_merchant(merchant) for merchant in merchants]
