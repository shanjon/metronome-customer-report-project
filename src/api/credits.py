from src.api.client import MetronomeClient
from src.utils.logging import log

def get_credit_ledger(customer_id):
    log(f"Fetching credit ledger for customer {customer_id}...")
    client = MetronomeClient()
    payload = {"customer_ids": [customer_id]}
    response = client.post("credits/listEntries", payload)
    data = response["data"]
    if not data or not data[0].get("ledgers"):
        log(f"No credit ledger entries found for customer {customer_id}")
        return None
    ledger = data[0]["ledgers"][0]
    log(f"Fetched credit ledger for customer {customer_id}")
    return ledger