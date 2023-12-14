# Ascenda-Loyalty-Take-Home-Asignment

## Requirements
- Python 3.x
- Git

## Setup
1. Clone the project from Github to your local machine
2. Navigate to the project directory
3. Create a virtual environment (optional but recommended): ```python -m venv .env```
4. Activate the virtual environment:
    - On Windows: ```.env\Scripts\activate```
    - On Unix or MacOS: ```source .env/bin/activate```
5. Install dependencies: ```pip install -r requirements.txt```

## Usage
Run the CLI application using the following command:
```python
    python ascenda_travel_platform.py -i <input_file_path> -d <checkin_date>
```
or
```python
    python ascenda_travel_platform.py --input_file_path <input_file_path> --checkin_date <checkin_date>
```
- `<input_file_path>`:Path to the JSON file as the response from Ascenda's external API.
- `<checkin_date>`: Customer check-in date in YYYY-MM-DD format.


Optional:
- `-o, --output_file_path`:  Path to the output file (default: output.json).

## Test
1. Navigate to the `tests` folder
2. Run the tests using the command:
```python
    pytest test_integration.py
```

