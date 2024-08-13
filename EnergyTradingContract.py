import json
import time


class EnergyTradingContract:
    """
    Represents a contract for energy trading between a producer and a consumer.

    Args:
        blockchain (Blockchain): The blockchain instance used for creating transactions.
        producer (str): The address of the producer.
        consumer (str): The address of the consumer.
        energy_amount (float): The amount of energy being traded.
        price_per_unit (float): The price per unit of energy.
        delivery_time (float): The delivery time in seconds since the epoch.

    Attributes:
        blockchain (Blockchain): The blockchain instance used for creating transactions.
        producer (str): The address of the producer.
        consumer (str): The address of the consumer.
        energy_amount (float): The amount of energy being traded.
        price_per_unit (float): The price per unit of energy.
        delivery_time (float): The delivery time in seconds since the epoch.
        status (str): The status of the trade (e.g., "Pending", "In Escrow", "Completed", "penalised").
        escrow (float): The amount of money held in escrow.

    Methods:
        initiate_trade(): Initiates the trade by creating a transaction and placing the total price in escrow.
        confirm_delivery(): Confirms the delivery and releases the escrowed amount to the producer if the delivery time has been reached.
        penalise_producer(): penalises the producer if the delivery time has passed with a grace period.
        __str__(): Returns a JSON string representation of the contract object.
    """

    """
    Initiates the trade by creating a transaction and placing the total price in escrow.
    """

    """
    Confirms the delivery and releases the escrowed amount to the producer if the delivery time has been reached.
    """

    """
    penalises the producer if the delivery time has passed with a grace period.
    """

    """
    Returns a JSON string representation of the contract object.
    """
    def __init__(self, blockchain, producer, consumer, energy_amount, price_per_unit, delivery_time):
        self.blockchain = blockchain
        self.producer = producer
        self.consumer = consumer
        self.energy_amount = energy_amount
        self.price_per_unit = price_per_unit
        self.delivery_time = delivery_time
        self.status = "Pending"
        self.escrow = 0

    def initiate_trade(self):
        total_price = self.energy_amount * self.price_per_unit
        self.blockchain.create_transaction({"from": self.consumer, "to": "escrow", "amount": total_price})
        self.escrow = total_price
        self.status = "In Escrow"
        print(f"Trade initiated. {total_price} placed in escrow.")

    def confirm_delivery(self):
        if time.time() >= self.delivery_time:
            self.blockchain.create_transaction({"from": "escrow", "to": self.producer, "amount": self.escrow})
            self.status = "Completed"
            self.escrow = 0
            print(f"Delivery confirmed. {self.escrow} released to producer.")
        else:
            print("Delivery time has not been reached.")

    def penalise_producer(self):
        if time.time() >= self.delivery_time + 60:  # 60 seconds grace period
            penalty = self.escrow * 0.1
            self.blockchain.create_transaction({"from": "escrow", "to": self.consumer, "amount": self.escrow - penalty})
            self.blockchain.create_transaction({"from": "escrow", "to": self.producer, "amount": penalty})
            self.status = "Penalised"
            self.escrow = 0
            print(f"Producer penalised. {penalty} transferred to producer, rest returned to consumer.")

    def __str__(self):
        return json.dumps(self.__dict__, indent=4)