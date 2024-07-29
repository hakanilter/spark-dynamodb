import arrow
import boto3
import random
from faker import Faker
from dataclasses import asdict
from typing import List, Dict, Any

from model.customer import Customer
from model.product import Product
from model.order import Order


class DataProducer:
    
    def __init__(self, num_customers:int=100, num_products:int=50, num_orders:int=1000):
        self.dynamodb = boto3.resource("dynamodb")

        self.faker = Faker()

        self.num_customers = num_customers
        self.num_products = num_products
        self.num_orders = num_orders

    def produce(self):
        # Generate customers
        customers = [self._generate_random_customer() for _ in range(self.num_customers)]

        # Generate products
        products = [self._generate_random_product() for _ in range(self.num_products)]

        # Generate orders   # TODO: Generate orders with multiple products
        orders = []
        for customer in customers:
            for product in products:
                if len(orders) == self.num_orders:
                    break
                orders.append(self._generate_random_order(customer, product))

        # Persist        
        self._batch_write_items("product", [asdict(p) for p in products])
        self._batch_write_items("customer", [asdict(c) for c in customers])
        self._batch_write_items("order", [asdict(o) for o in orders])

    def _generate_random_customer(self) -> Customer:
        return Customer(
            id=self.faker.uuid4(),
            name=self.faker.name(),
            email=self.faker.email(),
            created_at=arrow.utcnow().format("YYYY-MM-DD HH:mm:ss")
        )
    
    def _generate_random_product(self) -> Product:
        products = [
            "Quantum Resonance Device",
            "Eco-Friendly Water Bottle",
            "Wireless Charging Pad",
            "Solar-Powered Lantern",
            "Smart Home Thermostat",
            "Noise-Cancelling Headphones",
            "Ultra-HD Action Camera",
            "Digital Pressure Cooker",
            "Multi-Tool Pocket Knife",
            "Bluetooth Fitness Tracker",
        ]

        random_color = self.faker.color_name().capitalize()
        random_title = products[random.randint(0, len(products)-1)]

        return Product(
            id=self.faker.uuid4(),
            name=f"{random_title} {random_color}",
            desc=self.faker.text(),
            price=str(round(random.uniform(5.0, 100.0), 2)),
            created_at=arrow.utcnow().format("YYYY-MM-DD HH:mm:ss")
        )

    def _generate_random_order(self, customer, product) -> Order:
        quantity = random.randint(1,8)
        return Order(
            id=self.faker.uuid4(),
            customer_id=customer.id,
            product_id=product.id,
            quantity=quantity,
            total=str(float(quantity) * float(product.price)),
            created_at=arrow.utcnow().format("YYYY-MM-DD HH:mm:ss")
        )

    # Function to batch write items to DynamoDB
    def _batch_write_items(self, table_name: str, items: List[Dict[str, Any]]):
        # Split items into batches of 25
        batch_size = 25
        for i in range(0, len(items), batch_size):
            batch = items[i:i + batch_size]
            request_items = [{"PutRequest": {"Item": item}} for item in batch]
            
            response = self.dynamodb.batch_write_item(RequestItems={table_name: request_items})
            unprocessed_items = response.get("UnprocessedItems", {}).get(table_name, [])
            if unprocessed_items:
                raise Exception("Failed to persist")
            
            # Handle unprocessed items
            while unprocessed_items:
                print(f"Retrying {len(unprocessed_items)} unprocessed items...")
                response = self.dynamodb.batch_write_item(RequestItems={table_name: unprocessed_items})
                unprocessed_items = response.get("UnprocessedItems", {}).get(table_name, [])
                if unprocessed_items:
                    raise Exception("Failed to persist")


if __name__ == "__main__":
    DataProducer().produce()
