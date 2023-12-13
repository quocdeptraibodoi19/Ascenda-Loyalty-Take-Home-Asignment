import json
from typing import List

from .offer import Offer
from .data_parser import DataParser


class FileHandler:
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def _load_data(input_path: str):
        try:
            with open(input_path, "r") as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            print(f"File not found: {input_path}")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
        except (KeyError, ValueError) as e:
            print(f"Error parsing data: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        return None
    
    @staticmethod
    def load_offers(input_path: str):
        data = FileHandler._load_data(input_path)
        if data is None:
            return []
        return data.get("offers", [])

    @staticmethod
    def load_test_checkin_date(input_path: str):
        return FileHandler._load_data(input_path).get("checkin_date", "")
    
    @staticmethod
    def save_offers(offers: List[Offer], output_path: str):
        try:
            with open(output_path, "w") as file:
                serialized_data = DataParser.reverse_parse_offers(offers=offers)
                json.dump({"offers": serialized_data}, file, indent=2)
            print(f"Data saved successfully to {output_path}")
        except Exception as e:
            print(f"An error occurred while saving data: {e}")
