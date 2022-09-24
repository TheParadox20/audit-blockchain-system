from block_chain.account import Account
from block_chain.hash import Hash
from block_chain.block import Block
import json

class Transaction:
    """
    Class that allows to form a transaction containing user payments.
    """
    transactionID = ''
    transaction = {}

    def __init__(self,operation):
        self.transactionID = Hash.hash_256(operation) 
        self.transaction = {
            'operations':operation,
            'transactionID':self.transactionID,
            'Signature':Account.signData(self.transactionID,0)
        }
        Block(self.transaction)