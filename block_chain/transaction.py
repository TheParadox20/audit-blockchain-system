from operation import Operation
from account import Account
from hash import Hash
import json

class Transaction:
    """
    Class that allows to form a transaction containing user payments.
    """
    transactionID = ''
    operation = ''
    transaction = {}

    def __init__(self,sender,receiver,amount):
        self.operation = Operation(sender,receiver,amount).operation
        self.transactionID = Hash.hash_256(self.operation) 
        self.transaction = {
            'operations':json.dumps(self.operation),
            'transactionID':self.transactionID,
            'Signature':Account.signData(0,self.transactionID)
        }