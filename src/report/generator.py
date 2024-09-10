from src.api.customers import get_customers
from src.api.invoices import get_invoices
from src.api.credits import get_credit_ledger
from src.utils.logging import log

def calculate_invoice_balance(invoices):
    return sum(invoice["total"] for invoice in invoices)

def calculate_credit_balance(ledger):
    if ledger is None:
        return 0
    return sum(entry["amount"] for entry in ledger["entries"])

def generate_report():
    log("Generating report...")
    customers = get_customers()
    report_data = []

    for customer in customers:
        customer_id = customer["id"]
        customer_name = customer["name"]
        
        try:
            invoices = get_invoices(customer_id)
            invoice_balance = calculate_invoice_balance(invoices)
            
            credit_ledger = get_credit_ledger(customer_id)
            credit_balance = calculate_credit_balance(credit_ledger)
            
            report_data.append({
                "Customer ID": customer_id,
                "Customer Name": customer_name,
                "Invoice Balance": invoice_balance / 100,  # Convert cents to dollars
                "Credit Balance": credit_balance / 100,  # Convert cents to dollars
                "Notes": "No credit ledger" if credit_ledger is None else ""
            })
        except Exception as e:
            log(f"Error processing customer {customer_id}: {str(e)}")
            report_data.append({
                "Customer ID": customer_id,
                "Customer Name": customer_name,
                "Invoice Balance": "Error",
                "Credit Balance": "Error",
                "Notes": str(e)
            })

    log(f"Generated report with {len(report_data)} entries")
    return report_data