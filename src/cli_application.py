import argparse
from datetime import datetime
import os

from .config import mapping_category, include_categories, day_gap, target_number_offers
from .file_handler import FileHandler
from .data_parser import DataParser
from .filter import OfferFilter, FilterFunctionManager
from .selector import OfferSelector, MerchantDistanceHeapCreationStrategy


class CliApplication:
    def __init__(self) -> None:
        self.parser = self._create_arg_parser()
        self.args = self.parser.parse_args()

    def _create_arg_parser(self):
        parser = argparse.ArgumentParser(
            description="Ascenda Travel Platform CLI Application"
        )
        parser.add_argument(
            "-d",
            "--checkin_date",
            help="Customer check-in date in YYYY-MM-DD format",
            required=True,
        )
        parser.add_argument(
            "-i",
            "--input_file_path",
            help="The path to the json file as the response from the Ascenda's external API",
            required=True,
        )
        parser.add_argument(
            "-o",
            "--output_file_path",
            default="output.json",
            help="The path to the output file (default: output.json)",
        )
        return parser

    def _check_paths(self):
        if not os.path.exists(self.args.input_file_path):
            print(
                f"Error: Input file path '{self.args.input_file_path}' does not exist."
            )
            return False

        output_dir = os.path.dirname(self.args.output_file_path)
        if output_dir != "" and not os.path.exists(output_dir):
            os.makedirs(output_dir)
            print(f"Created output directory: {output_dir}")

        return True

    def _check_date(self):
        try:
            datetime.strptime(self.args.checkin_date, "%Y-%m-%d")
        except ValueError:
            print("Error: Invalid date format. Please use YYYY-MM-DD.")
            return False
        return True

    def run(self):
        if not self._check_paths() or not self._check_date():
            return

        checkin_date = self.args.checkin_date
        input_file_path = self.args.input_file_path
        output_file_path = self.args.output_file_path

        offers_data = FileHandler.load_offers(input_path=input_file_path)
        offers_list = DataParser.parse_offers(offers_data=offers_data)

        offer_filter = OfferFilter(offers=offers_list)
        filtered_offers_list = (
            offer_filter.filter(
                FilterFunctionManager.category_filter_function(
                    mapping_category=mapping_category,
                    include_categories=include_categories,
                )
            )
            .filter(
                FilterFunctionManager.valid_to_date_filter_function(
                    checkin_date=datetime.strptime(checkin_date, "%Y-%m-%d").date(),
                    day_gap=day_gap,
                )
            )
            .execute()
        )

        target_offers = OfferSelector.select(
            filtered_offers_list,
            target_number_offers,
            MerchantDistanceHeapCreationStrategy(),
        )
        FileHandler.save_offers(offers=target_offers, output_path=output_file_path)
