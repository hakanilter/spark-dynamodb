from decimal import Decimal
from dataclasses import dataclass


@dataclass
class Order:

    id: str
    customer_id: str
    product_id: str
    quantity: int
    total: str
    created_at: str
