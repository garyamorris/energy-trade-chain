from Block import Block


import time


class Blockchain:
    """
    A class representing a blockchain.

    Attributes:
        chain (list): A list of blocks in the blockchain.
        difficulty (int): The number of leading zeros required in the block hash for mining.
        pending_transactions (list): A list of pending transactions.
        mining_reward (int): The reward given to the miner for mining a block.

    Methods:
        __init__(): Initializes a new instance of the Blockchain class.
        create_genesis_block(): Creates the genesis block of the blockchain.
        get_latest_block(): Returns the latest block in the blockchain.
        mine_pending_transactions(miner_address): Mines a new block with the pending transactions.
        proof_of_work(block): Performs the proof of work algorithm to find a valid block hash.
        create_transaction(transaction): Adds a new transaction to the pending transactions list.
        is_chain_valid(): Checks if the blockchain is valid.
    """
    
    """
    Initializes a new instance of the Blockchain class.

    The chain is initialized with the genesis block.
    The difficulty is set to 2, meaning the block hash must have 2 leading zeros for mining.
    The pending_transactions list is initially empty.
    The mining_reward is set to 100.
    """

    """
    Creates the genesis block of the blockchain.

    Returns:
        Block: The genesis block.
    """

    """
    Returns the latest block in the blockchain.

    Returns:
        Block: The latest block.
    """

    """
    Mines a new block with the pending transactions.

    Args:
        miner_address (str): The address of the miner who will receive the mining reward.
    """


    """
    Performs the proof of work algorithm to find a valid block hash.

    Args:
        block (Block): The block to perform the proof of work on.

    Returns:
        Block: The block with a valid hash.
    """

    """
    Adds a new transaction to the pending transactions list.

    Args:
        transaction (dict): The transaction to add to the pending transactions list.
    """

    """
    Checks if the blockchain is valid.

    Returns:
        bool: True if the blockchain is valid, False otherwise.
    """

    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 2
        self.pending_transactions = []
        self.mining_reward = 100

    def create_genesis_block(self):
        return Block(0, "0", [], time.time())

    def get_latest_block(self):
        return self.chain[-1]

    def mine_pending_transactions(self, miner_address):
        block = Block(len(self.chain), self.get_latest_block().hash, self.pending_transactions, time.time())
        block = self.proof_of_work(block)

        self.chain.append(block)
        self.pending_transactions = [
            {"from": None, "to": miner_address, "amount": self.mining_reward}
        ]

    def proof_of_work(self, block):
        while block.hash[:self.difficulty] != '0' * self.difficulty:
            block.nonce += 1
            block.hash = block.calculate_hash()
        return block

    def create_transaction(self, transaction):
        self.pending_transactions.append(transaction)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True