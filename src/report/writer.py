import csv
from src.utils.logging import log

def save_to_csv(data, filename):
    log(f"Saving report to {filename}...")
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ["Customer ID", "Customer Name", "Invoice Balance", "Credit Balance", "Notes"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for row in data:
            writer.writerow(row)
    log("Report saved successfully")