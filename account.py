class Account:
    """
    Class for managing a wallet, creating operations and data signing.
    """
    accountID = '' #A unique value for identifying an account within the system. It can often be a public key or its hash value.
    wallet = [] # array that stores KeyPair objects that belong to the same account
    balance = 0.0 #value representing the number of coins belongs to the account

    def __init__(self) -> None:
        pass

    def genAccount(self):
        """
        Creates an account; Returns an object of the Account class. The first key pair is generated and assigned to the account
        """
        pass

    def addKeyPairToWallet(self):
        pass

    def updateBalance(self):
        pass

    def createPaymentOp(self):
        pass

    def getBalance(self):
        pass

    def printBalance(self):
        pass

    def signData(self):
        pass