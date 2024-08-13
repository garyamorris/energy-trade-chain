import hashlib
import json


class Block:
    """
    Initializes a new instance of the Block class.

    Args:
        index (int): The index of the block.
        previous_hash (str): The hash of the previous block.
        transactions (list): The list of transactions in the block.
        timestamp (float): The timestamp of when the block was created.
        nonce (int, optional): The nonce value used for mining. Defaults to 0.
    """

    """
    Calculates the hash of the block.

    Returns:
        str: The calculated hash value.
    """

    """
    Returns a string representation of the block.

    Returns:
        str: The string representation of the block.
    """
    def __init__(self, index, previous_hash, transactions, timestamp, nonce=0):
        self.index = index
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.timestamp = timestamp
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()

    def __str__(self):
        return json.dumps(self.__dict__, indent=4)