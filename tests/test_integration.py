import unittest
from unittest.mock import patch
import os

from src.cli_application import CliApplication
from src.file_handler import FileHandler


class TestIntegration(unittest.TestCase):
    def test_test_case_1(self):
        self.run_test_case(
            input_test_file="test_data/input_testcase_1.json",
            expected_output_file="test_data/expected_output_testcase_1.json",
            output_file="output_test_data/output_testcase_1.json",
        )

    def test_test_case_2(self):
        self.run_test_case(
            input_test_file="test_data/input_testcase_2.json",
            expected_output_file="test_data/expected_output_testcase_2.json",
            output_file="output_test_data/output_testcase_2.json",
        )

    def test_test_case_3(self):
        self.run_test_case(
            input_test_file="test_data/input_testcase_3.json",
            expected_output_file="test_data/expected_output_testcase_3.json",
            output_file="output_test_data/output_testcase_3.json",
        )

    def test_test_case_4(self):
        self.run_test_case(
            input_test_file="test_data/input_testcase_4.json",
            expected_output_file="test_data/expected_output_testcase_4.json",
            output_file="output_test_data/output_testcase_4.json",
        )

    def test_test_case_5(self):
        self.run_test_case(
            input_test_file="test_data/input_testcase_5.json",
            expected_output_file="test_data/expected_output_testcase_5.json",
            output_file="output_test_data/output_testcase_5.json",
        )

    def test_test_case_6(self):
        self.run_test_case(
            input_test_file="test_data/input_testcase_6.json",
            expected_output_file="test_data/expected_output_testcase_6.json",
            output_file="output_test_data/output_testcase_6.json",
        )

    def run_test_case(
        self, input_test_file: str, expected_output_file: str, output_file: str
    ):
        checkin_date = FileHandler.load_test_checkin_date(input_test_file)

        with patch(
            "sys.argv",
            [
                "ascenda_travel_platform.py",
                "-i",
                input_test_file,
                "-d",
                checkin_date,
                "-o",
                output_file,
            ],
        ):
            CliApplication().run()

        self.assertTrue(os.path.isfile(output_file))
        self.assertEqual(
            FileHandler.load_offers(expected_output_file),
            FileHandler.load_offers(output_file),
        )
