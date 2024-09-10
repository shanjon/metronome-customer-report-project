from src.api.client import MetronomeClient
from src.utils.logging import log

def get_customers():
    log("Fetching customers...")
    client = MetronomeClient()
    response = client.get("customers")
    customers = response["data"]
    log(f"Fetched {len(customers)} customers")
    return customers