import hashlib
from block_chain.keypair import Keypair
from block_chain.signature import Signature
from persistence.explorer import Explorer
from block_chain.hash import Hash

explorer = Explorer()
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
            'keys':userKeys,
            'ID':hashlib.sha256(userKeys.privateKey.to_string()).hexdigest()
        })

    def addKeyPairToWallet(self,seed):
        keys = Keypair(seed)
        Account.wallet.append({
            'keys':keys,
            'ID':hashlib.sha256(keys.privateKey.to_string()).hexdigest()
        })

    def updateBalance(self,accountID):
        self.balance = self.getBalance(accountID)
        

    def createPaymentOp(self):#Done in Operation class
        pass

    def getBalance(self,accountID):
        #Go through every block extracting transaction information related to the ID
        inputs = []
        outputs = []
        cursor = 0
        for i in range(0,Explorer.getChainHeight()):
            block =  Explorer.getBlock(cursor)[0]
            block = explorer.blockToDict(block)
            if accountID == block['transactions']['operations']['senderID']:
                outputs.append(float(block['transactions']['operations']['amount']))
            if accountID == block['transactions']['operations']['receiverID']:
                inputs.append(float(block['transactions']['operations']['amount']))
            cursor+=Explorer.getBlock(cursor)[1]
        return sum(inputs)-sum(outputs)

    def printBalance(self,ID):
        print(self.getBalance(ID))

    def signData(message,index):
        if index>len(Account.wallet):
            print('\tKey doesn\'t exist in space')
            return
        pen = Signature()
        return pen.signData(Account.wallet[index]['keys'].privateKey,message)