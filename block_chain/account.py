import hashlib
from keypair import Keypair
from signature import Signature
from persistence.explorer import Explorer
from hash import Hash

class Account:
    """
    Class for managing a wallet, creating operations and data signing.
    """
    accountID = '' #A unique value for identifying an account within the system. It can often be a public key or its hash value.
    wallet = [] # array that stores KeyPair objects that belong to the same account
    balance = 0.0 #value representing the number of coins belongs to the account

    def __init__(self):
        pass

    def genAccount(self,seed):
        """
        Creates an account; Returns an object of the Account class. The first key pair is generated and assigned to the account
        """
        userKeys = Keypair(seed)
        userKeys.genKeyPair()
        self.accountID=Hash.hash_256(userKeys.privateKey.to_string())
        Account.wallet.append({
            'key':userKeys,
            'ID':hashlib.sha256(userKeys.privateKey.to_string()).hexdigest()
        })

    def addKeyPairToWallet(self,seed):
        keys = Keypair(seed)
        Account.wallet.append({
            'key':keys,
            'ID':hashlib.sha256(keys.privateKey.to_string()).hexdigest()
        })

    def updateBalance(self):
        pass

    def createPaymentOp(self):
        pass

    def getBalance(self,ID):
        pass

    def printBalance(self):
        pass

    def signData(self,message,index):
        if index>len(Account.wallet):
            print('\tKey doesn\'t exist in space')
            return
        pen = Signature()
        return pen.signData(Account.wallet[index]['keys'].privateKey,message)