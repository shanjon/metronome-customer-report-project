from src.api.client import MetronomeClient
from src.utils.logging import log

def get_invoices(customer_id):
    log(f"Fetching invoices for customer {customer_id}...")
    client = MetronomeClient()
    response = client.get(f"customers/{customer_id}/invoices?status=FINALIZED")
    invoices = response["data"]
    log(f"Fetched {len(invoices)} invoices for customer {customer_id}")
    return invoices