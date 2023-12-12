import argparse
from datetime import datetime

from .fileHandler import FileHandler
from .dataParser import DataParser
from .offerFilter import OfferFilter, FilterFunctionManager
from .offerSelector import MerchantSelector, OfferSelector


class CliApplication:
    def __init__(self) -> None:
        self.parser = self._create_arg_parser()
        self.args = self.parser.parse_args()

    def _create_arg_parser(self):
        parser = argparse.ArgumentParser(
            description="Ascenda Travel Platform CLI Application"
        )
        parser.add_argument(
            "-d", "--checkin_date", help="Customer check-in date in YYYY-MM-DD format"
        )
        parser.add_argument(
            "-i",
            "--input_file_path",
            help="The path to the json file as the response from the Ascenda's external API",
        )
        parser.add_argument(
            "-o",
            "--output_file_path",
            default="output.json",
            help="The path to the output file (default: output.json)",
        )
        return parser

    def run(self):
        checkin_date = self.args.checkin_date
        input_file_path = self.args.input_file_path
        output_file_path = self.args.output_file_path

        offers_data = FileHandler.load_data(input_path=input_file_path)
        offers_list = DataParser.parse_offers(offers_data=offers_data)

        offer_filter = OfferFilter(offers=offers_list)
        filtered_offers_list = (
            offer_filter.filter(
                FilterFunctionManager.category_filter_function(
                    mapping_category={
                        "Restaurant": 1,
                        "Retail": 2,
                        "Hotel": 3,
                        "Activity": 4,
                    },
                    include_categories=["Restaurant", "Retail", "Activity"],
                )
            )
            .filter(
                FilterFunctionManager.valid_to_date_filter_function(
                    checkin_date=datetime.strptime(checkin_date, "%Y-%m-%d").date(),
                    day_gap=5,
                )
            )
            .execute()
        )

        transformed_offer = []
        for offer in filtered_offers_list:
            selected_merchant = MerchantSelector(offer.merchants).select()
            if selected_merchant is not None:
                offer.merchants = [selected_merchant]
                transformed_offer.append(offer)

        offerSelector = OfferSelector(
            target_num_offers=2, included_categories=[1, 2, 4], offers=transformed_offer
        )
        target_offers = offerSelector.select()

        FileHandler.save_data(offers=target_offers, output_path=output_file_path)
