import time
from Blockchain import Blockchain
from EnergyTradingContract import EnergyTradingContract

# Example Usage
blockchain = Blockchain()

# Energy trading contract between Producer A and Consumer B
contract = EnergyTradingContract(blockchain, "Producer A", "Consumer B", energy_amount=100, price_per_unit=5, delivery_time=time.time() + 5)

contract.initiate_trade()
time.sleep(5)  # Wait for the delivery time to pass
contract.confirm_delivery()

# If delivery is not confirmed after a certain period, penalize the producer
time.sleep(5)  # Wait additional time to simulate late delivery
contract.penalize_producer()

# Display the blockchain
for block in blockchain.chain:
    print(block)
