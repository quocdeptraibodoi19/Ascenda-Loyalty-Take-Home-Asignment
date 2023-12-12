import json
from datetime import datetime
from typing import List

from offer import Offer, Merchant

# This class follows Singleton pattern since it doesn't maintain states and it just provides the needed information for the outsiders
class InputParser:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(InputParser, cls).__new__(cls)
        return cls._instance
    
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def str2date(dateString: str) -> datetime.date:
        return datetime.strptime(dateString, "%Y-%m-%d").date()

    @staticmethod
    def inputedJson2OfferList(input_file_path: str) -> List[Offer]:
        offers_list = []
        try:
            with open(input_file_path, 'r') as file:
                json_data = file.read()
                data = json.loads(json_data)

                for offer_data in data.get("offers", []):
                    offer_id = offer_data.get("id")
                    offer_title = offer_data.get("title")
                    offer_description = offer_data.get("description")
                    offer_category = offer_data.get("category")
                    offer_valid_to_str = offer_data.get("valid_to")
                    offer_valid_to = InputParser.str2date(offer_valid_to_str)

                    merchant_list = []
                    for merchant_data in offer_data.get("merchants", []):
                        merchant_id = merchant_data.get("id")
                        merchant_name = merchant_data.get("name")
                        merchant_distance = merchant_data.get("distance")

                        merchant = Merchant(id=merchant_id, name=merchant_name, distance=merchant_distance)
                        merchant_list.append(merchant)
                    
                    offer = Offer(
                        id= offer_id,
                        title= offer_title,
                        description= offer_description,
                        category= offer_category,
                        valid_to= offer_valid_to,
                        merchants= merchant_list
                    )
                    offers_list.append(offer)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        finally:
            return offers_list