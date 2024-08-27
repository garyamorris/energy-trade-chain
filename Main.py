import time
from Blockchain import Blockchain
from EnergyTradingContract import EnergyTradingContract

# Example Usage
blockchain = Blockchain()

# Energy trading contract between Producer A and Consumer B
contract = EnergyTradingContract(blockchain, "Producer A", "Consumer B", energy_amount=100, base_price_per_unit=5, delivery_time=time.time() + 5)

# Initiating the Trade with dynamic pricing
contract.initiate_trade()

# Continuously update the price until delivery
contract.update_price_until_delivery()

# Confirming Energy Delivery after some time
time.sleep(1)  # Wait a little more to reach the delivery time
contract.confirm_delivery()

# If delivery is not confirmed after a certain period, penalise the producer
time.sleep(5)  # Wait additional time to simulate late delivery
contract.penalise_producer()

# Mine pending transactions
blockchain.mine_pending_transactions('Miner-address')

# Display the blockchain
for block in blockchain.chain:
    print(block)
