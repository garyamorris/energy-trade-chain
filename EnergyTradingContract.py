import json
import random
import time


class EnergyTradingContract:
    """
    Represents a contract for energy trading between a producer and a consumer.

    Args:
        blockchain (Blockchain): The blockchain instance used for creating transactions.
        producer (str): The address of the producer.
        consumer (str): The address of the consumer.
        energy_amount (float): The amount of energy being traded.
        base_price_per_unit (float): The base price per unit of energy.
        delivery_time (float): The delivery time in seconds since the epoch.

    Attributes:
        blockchain (Blockchain): The blockchain instance used for creating transactions.
        producer (str): The address of the producer.
        consumer (str): The address of the consumer.
        energy_amount (float): The amount of energy being traded.
        base_price_per_unit (float): The base price per unit of energy.
        price_per_unit (float): The current price per unit of energy.
        delivery_time (float): The delivery time in seconds since the epoch.
        status (str): The status of the trade (e.g., "Pending", "In Escrow", "Completed", "Penalised").
        escrow (float): The amount of money held in escrow.
        total_price (float): The total price of the trade.

    Methods:
        __init__(self, blockchain, producer, consumer, energy_amount, base_price_per_unit, delivery_time): Initializes the EnergyTradingContract object.
        calculate_dynamic_price(self): Simulates dynamic pricing based on a random market condition.
        initiate_trade(self): Initiates the trade by calculating the total price and placing it in escrow.
        update_price_until_delivery(self): Periodically updates the price until the delivery time is reached.
        confirm_delivery(self): Confirms the delivery and releases the escrowed amount to the producer if the delivery time has been reached.
        penalise_producer(self): Penalizes the producer if the delivery time has passed with a grace period.
        __str__(self): Returns a JSON string representation of the contract object.
    """

    def __init__(self, blockchain, producer, consumer, energy_amount, base_price_per_unit, delivery_time):
        self.blockchain = blockchain
        self.producer = producer
        self.consumer = consumer
        self.energy_amount = energy_amount
        self.base_price_per_unit = base_price_per_unit
        self.price_per_unit = base_price_per_unit
        self.delivery_time = delivery_time
        self.status = "Pending"
        self.escrow = 0
        self.total_price = 0

    def calculate_dynamic_price(self):
        """Simulates dynamic pricing based on a random market condition."""
        market_factor = random.uniform(0.9, 1.1)  # Simulate market fluctuation
        self.price_per_unit = self.base_price_per_unit * market_factor
        print(f"Dynamic pricing updated: {self.price_per_unit} per unit.")

    def initiate_trade(self):
        self.calculate_dynamic_price()
        self.total_price = self.energy_amount * self.price_per_unit
        self.blockchain.create_transaction({"from": self.consumer, "to": "escrow", "amount": self.total_price})
        self.escrow = self.total_price
        self.status = "In Escrow"
        print(f"Trade initiated. {self.total_price} placed in escrow at {self.price_per_unit} per unit.")

    def update_price_until_delivery(self):
        """Periodically update the price until the delivery time is reached."""
        while time.time() < self.delivery_time:
            self.calculate_dynamic_price()
            self.total_price = self.energy_amount * self.price_per_unit
            print(f"Updated total price: {self.total_price} (escrow remains the same).")
            time.sleep(1)  # Simulate periodic market updates every 2 seconds

    def confirm_delivery(self):
        if time.time() >= self.delivery_time:
            amount_to_release = self.total_price  # Use the updated total price
            self.blockchain.create_transaction({
                "from": "escrow",
                "to": self.producer,
                "amount": amount_to_release
            })
            self.status = "Completed"
            self.escrow = 0
            print(
                f"Delivery confirmed. {amount_to_release} released to producer."
            )
        else:
            print("Delivery time has not been reached.")

    def penalise_producer(self):
        if time.time() >= self.delivery_time + 10:  # 10 seconds grace period
            penalty = self.escrow * 0.1
            self.blockchain.create_transaction({"from": "escrow", "to": self.consumer, "amount": self.escrow - penalty})
            self.blockchain.create_transaction({"from": "escrow", "to": self.producer, "amount": penalty})
            self.status = "Penalised"
            self.escrow = 0
            print(f"Producer penalised. {penalty} transferred to producer, rest returned to consumer.")

    def __str__(self):
        return json.dumps(self.__dict__, indent=4)
    def __init__(self, blockchain, producer, consumer, energy_amount, base_price_per_unit, delivery_time):
        self.blockchain = blockchain
        self.producer = producer
        self.consumer = consumer
        self.energy_amount = energy_amount
        self.base_price_per_unit = base_price_per_unit
        self.price_per_unit = base_price_per_unit
        self.delivery_time = delivery_time
        self.status = "Pending"
        self.escrow = 0
        self.total_price = 0

    def calculate_dynamic_price(self):
        """Simulates dynamic pricing based on a random market condition."""
        market_factor = random.uniform(0.9, 1.1)  # Simulate market fluctuation
        self.price_per_unit = self.base_price_per_unit * market_factor
        print(f"Dynamic pricing updated: {self.price_per_unit} per unit.")

    def initiate_trade(self):
        self.calculate_dynamic_price()
        self.total_price = self.energy_amount * self.price_per_unit
        self.blockchain.create_transaction({"from": self.consumer, "to": "escrow", "amount": self.total_price})
        self.escrow = self.total_price
        self.status = "In Escrow"
        print(f"Trade initiated. {self.total_price} placed in escrow at {self.price_per_unit} per unit.")

    def update_price_until_delivery(self):
        """Periodically update the price until the delivery time is reached."""
        while time.time() < self.delivery_time:
            self.calculate_dynamic_price()
            self.total_price = self.energy_amount * self.price_per_unit
            print(f"Updated total price: {self.total_price} (escrow remains the same).")
            time.sleep(1)  # Simulate periodic market updates every 2 seconds

    def confirm_delivery(self):
        if time.time() >= self.delivery_time:
            amount_to_release = self.total_price  # Use the updated total price
            self.blockchain.create_transaction({
                "from": "escrow",
                "to": self.producer,
                "amount": amount_to_release
            })
            self.status = "Completed"
            self.escrow = 0
            print(
                f"Delivery confirmed. {amount_to_release} released to producer."
            )
        else:
            print("Delivery time has not been reached.")

    def penalise_producer(self):
        if time.time() >= self.delivery_time + 10:  # 10 seconds grace period
            penalty = self.escrow * 0.1
            self.blockchain.create_transaction({"from": "escrow", "to": self.consumer, "amount": self.escrow - penalty})
            self.blockchain.create_transaction({"from": "escrow", "to": self.producer, "amount": penalty})
            self.status = "Penalised"
            self.escrow = 0
            print(f"Producer penalised. {penalty} transferred to producer, rest returned to consumer.")

    def __str__(self):
        return json.dumps(self.__dict__, indent=4)
