# Metronome Customer Report Project
This project is a [Metronome API](https://docs.metronome.com/api/) client that generates a customer summary report. It fetches data about customers, their invoices, and credit balances from the Metronome API, processes this information, and creates a summarized CSV report.

## Project Structure
```
metronome-customer-report-project/
│
├── src/                  # Source code directory
│   ├── __init__.py       # Makes src a package, simplifies imports
│   │
│   ├── api/              # API interaction modules
│   │   ├── __init__.py   # Exposes main functions from API modules
│   │   ├── client.py     # Base API client
│   │   ├── customers.py  # Customer data retrieval
│   │   ├── invoices.py   # Invoice data retrieval
│   │   └── credits.py    # Credit data retrieval
│   │
│   ├── utils/            # Utility modules
│   │   ├── __init__.py   # Exposes utility functions
│   │   ├── config.py     # Configuration management
│   │   └── logging.py    # Logging utilities
│   │
│   └── report/           # Report generation modules
│       ├── __init__.py   # Exposes report generation functions
│       ├── generator.py  # Report data generation
│       └── writer.py     # CSV writing utilities
│
├── main.py               # Main execution script
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

### Key Components
- `main.py`: The entry point of the application. It orchestrates the entire process of generating and saving the report.

- `src/`: Contains all the source code for the project, organized into subdirectories:
    - `__init__.py`: Makes `src` a Python package, allowing for top-level imports like `from src import api, utils, report`.
    - `api/`: Handles all interactions with the Metronome API.
        - `__init__.py`: Simplifies imports by exposing main functions from API modules.
        - `client.py`: Manages HTTP requests to the API.
        - `customers.py`: Functions for fetching customer data.
        - `invoices.py`: Functions for fetching invoice data.
        - `credits.py`: Functions for fetching credit data.

    - `utils/`: Provides utility functions used throughout the project.
        - `__init__.py`: Exposes utility functions for easy importing.
        - `config.py`: Manages application configuration, including API credentials.
        - `logging.py`: Provides logging functionality for tracking execution and errors.

    - `report/`: Contains logic for generating and writing the report.
        - `__init__.py`: Exposes main functions for report generation and writing.
        - `generator.py`: Orchestrates data collection and processing for the report.
        - `writer.py`: Handles writing the processed report data to a CSV file.

- `requirements.txt`: Lists the Python packages required to run the application

## How it works
1. The application starts in `main.py`.
2. It loads the configuration and checks for the API token.
3. It calls `generate_report()` from the report module, which:
    - Fetches all customers using the API client.
    - For each customer, fetches their invoices and credit ledger.
    - Calculates the invoice balance and credit balance.
    - Compiles all this information into a list of dictionaries.
4. The generated report data is then passed to `save_to_csv()`, which writes it to a CSV file.
5. Throughout the process, logging messages are printed to track progress and any issues.

## Metronome APIs used
- [`List customers`](https://docs.metronome.com/api/#operation/listCustomers)
- [`List invoices`](https://docs.metronome.com/api/#operation/listInvoices)
- [`List credit ledger entries`](https://docs.metronome.com/api/#operation/listCreditLedgerEntries)

## Assumptions
- The current invoice balance is calculated as the sum of all entries returned by the `List invoices` API endpoint where `status` is equal to `FINALIZED`.
- The current credit balance is calculated as the sum of all credit additions (denoted as positive `amount` values) and all credit deductions (denoted as negative `amount` values) returned by the `List credit ledger entries` API endpoint.

## How to execute
1. Clone the repository
```
git clone https://github.com/shanjon/metronome-customer-report-project
cd metronome-customer-report-project
```

2. Set up a virtual environment
```
python -m venv venv
```

3. Activate the virtual environment
- _On Windows:_
```
venv\Scripts\activate
```
- _On macOS and Linux:_
```
source venv/bin/activate
```

4. Install required packages
```
pip install -r requirements.txt
```

5. Set your Metronome API token
- _On Windows (Command Prompt):_
```
set METRONOME_API_TOKEN=your_api_token_here
```
- _On macOS and Linux:_
```
export METRONOME_API_TOKEN=your_api_token_here
```

6. Run the program
```
python main.py
```

The program will execute and generate a CSV file in the same directory with a name like `customer_summary_report_YYYYMMDD_HHMMSS.csv` - _see example `example_report.csv`._

## Challenges
- Trying to understand which API endpoints were relevant to the assignment and how to calculate invoice balance, current credit balance (see [Assumptions](https://github.com/shanjon/metronome-customer-report-project?tab=readme-ov-file#assumptions))
- General organization of the project - for example, determining whether to generate the invoice balance and credit balance as part of the same function that calls their respective APIs, or if it should be its own separate subdirectory/set of functions
- Testing each component of the project in isolation - I initially wrote a single script with all functionality and then once it was working organized it into packages/subdirectories