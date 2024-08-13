import json
import time


class EnergyTradingContract:
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

    def penalize_producer(self):
        if time.time() >= self.delivery_time + 60:  # 60 seconds grace period
            penalty = self.escrow * 0.1
            self.blockchain.create_transaction({"from": "escrow", "to": self.consumer, "amount": self.escrow - penalty})
            self.blockchain.create_transaction({"from": "escrow", "to": self.producer, "amount": penalty})
            self.status = "Penalized"
            self.escrow = 0
            print(f"Producer penalized. {penalty} transferred to producer, rest returned to consumer.")

    def __str__(self):
        return json.dumps(self.__dict__, indent=4)