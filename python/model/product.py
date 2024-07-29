from decimal import Decimal
from dataclasses import dataclass


@dataclass
class Product:

    id: str
    name: str
    desc: str
    price: str
    created_at: str
