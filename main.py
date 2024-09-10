from src.report import generate_report, save_to_csv
from src.utils import log, load_config
import sys
from datetime import datetime

if __name__ == "__main__":
    config = load_config()
    if not config.get("API_TOKEN"):
        log("Error: API_TOKEN is not set in the configuration")
        sys.exit(1)

    try:
        report_data = generate_report()
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"customer_summary_report_{timestamp}.csv"
        save_to_csv(report_data, filename)
        log(f"Report generated and saved as {filename}")
    except Exception as e:
        log(f"An error occurred: {str(e)}")
        sys.exit(1)