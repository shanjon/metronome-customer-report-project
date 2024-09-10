# Metronome Customer Report Project
This project is a [Metronome API](https://docs.metronome.com/api/) client that generates a customer summary report. It fetches data about customers, their invoices, and credit balances from the Metronome API, processes this information, and creates a CSV report.

## Project Structure
```
metronome-customer-report-project/
│
├── src/                  # Source code directory
│   ├── api/              # API interaction modules
│   │   ├── client.py     # Base API client
│   │   ├── customers.py  # Customer data retrieval
│   │   ├── invoices.py   # Invoice data retrieval
│   │   └── credits.py    # Credit data retrieval
│   │
│   ├── utils/            # Utility modules
│   │   ├── config.py     # Configuration management
│   │   └── logging.py    # Logging utilities
│   │
│   └── report/           # Report generation modules
│       ├── generator.py  # Report data generation
│       └── writer.py     # CSV writing utilities
│
├── main.py               # Main execution script
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

### Key Components
`main.py`: The entry point of the application. It orchestrates the entire process of generating and saving the report.

`src/`: Contains all the source code for the project, organized into subdirectories:
- `api/`: Handles all interactions with the Metronome API.
    - `client.py`: Manages HTTP requests to the API.
    - `customers.py`: Functions for fetching customer data.
    - `invoices.py`: Functions for fetching invoice data.
    - `credits.py`: Functions for fetching credit data.

- `utils/`: Provides utility functions used throughout the project.
    - `config.py`: Manages application configuration, including API credentials.
    - `logging.py`: Provides logging functionality for tracking execution and errors.

- `report/`: Contains logic for generating and writing the report.
    - `generator.py`: Orchestrates data collection and processing for the report.
    - `writer.py`: Handles writing the processed report data to a CSV file.

`requirements.txt`: Lists the Python packages required to run the application








<br><br><br><br>

## Project Structure and Key Components
The project contains a root directory, and 
### `README.md`
- Explanation of repository and project approach.

### `main.py`
- This is the entry point of the application.
- It orchestrates the entire process by calling functions to retrieve customer data, generate the report, and save it to a CSV file.
- It also handles top-level error management and logging.

### `requirements.txt`
- Lists the Python packages required to run the application (in this case, just the requests library).

### `src/__init__.py`
Definition of `src/` subdirectory.
- Marks the src directory as a Python package.
- Allows easy importing from subpackages.

### `src/api/`
This directory contains all API-related functionality.

- #### `client.py`
    - Defines the `MetronomeClient` class, which handles HTTP requests to the Metronome API.
    - Manages authentication and provides methods for GET and POST requests.

#### `customers.py`
- Contains the get_customers() function to fetch customer data from the API.

#### `invoices.py`
- Contains the get_invoices() function to fetch invoice data for a specific customer.

#### `credits.py`
- Contains the get_credit_ledger() function to fetch credit ledger data for a specific customer.

#### `__init__.py`
- Exposes the main functions from customers, invoices, and credits modules for easy importing.

### `src/utils/`
- Contains utility functions used throughout the project.

#### `config.py`
- Manages the configuration for the application, including API base URL and token.
- Provides functions to load and access the configuration.

#### `logging.py`
- Provides a simple logging function used throughout the application.

#### `__init__.py`
- Exposes the utility functions for easy importing.

### `src/report/`
- Contains the logic for generating and writing the report.

#### `generator.py`
- Contains the generate_report() function, which orchestrates data collection and processing for the report.
- Calculates invoice and credit balances for each customer.

#### `writer.py`
- Contains the save_to_csv() function, which writes the report data to a CSV file.

#### `__init__.py`
- Exposes the main functions from generator and writer modules for easy importing.

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
python3 -m venv venv
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

The program will execute and generate a CSV file in the same directory with a name like `customer_summary_report_YYYYMMDD_HHMMSS.csv`.