# from ..persistence.explorer import Explorer
import json
from block_chain.transaction import Transaction

class Operation:
    """
    Class that allows creation of a payment operation
    """
    sender = 0
    receiver = 0
    amount = 0.0
    operation = {}
    
    def __init__(self,sender,receiver,amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        if self.verifyOperation():
            self.createOperation()
            Transaction(json.dumps(self.operation))

    def createOperation(self):
        self.operation = {
            'senderID':self.sender,
            'receiverID':self.receiver,
            'amount':self.amount
        }

    def verifyOperation(self):
        return True
        balance = Explorer.getAccountBalance(self.sender)
        if balance<self.amount:
            return True
        return False

