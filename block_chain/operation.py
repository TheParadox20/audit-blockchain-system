# from ..persistence.explorer import Explorer
import json
from block_chain.transaction import Transaction
from persistence.explorer import Explorer

explorer = Explorer()

class Operation:
    """
    Class that allows creation of a payment operation
    """
    sender = ''
    receiver = ''
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
        balance = explorer.getAccountBalance(self.sender)
        print('Your Balance is:',balance)
        print('Transacting:',self.amount)
        if balance>self.amount or self.sender=='a138447742c24a0c65bd128d878a26127f07ba112be5c9a30e3ceb1a76fd39f4': #if from faucet address verify operation
            return True
        print('!!\tLow Balance\t!!')
        return False
        #Signature verification done at block level

