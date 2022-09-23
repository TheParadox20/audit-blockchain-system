from persistence.explorer import Explorer

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

    def createOperation(self):
        self.operation = {
            'senderID':self.sender,
            'receiverID':self.receiver,
            'amount':self.amount
        }

    def verifyOperation(self):
        balance = Explorer.getAccountBalance(self.sender)
        if balance<self.amount:
            return True
        return False