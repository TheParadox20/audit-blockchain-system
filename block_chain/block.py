from base64 import encode
from persistence.explorer import Explorer
from block_chain.blockchain import Blockchain
from block_chain.hash import Hash

class Block:
    """
    Class to form a block with transactions
    """
    blockID = ''
    prevHash = ''
    transactionSet = []
    block = {}

    def __init__(self,transaction):
        self.getPreviousHash()
        self.getPreviousHash()
        self.block = {
            'blockSize':self.calculateBlockSize(),
            'previousHash':self.prevHash,
            'numberOfTransactions':1,
            'blockNumber':self.getChainHeight()+1,
            'nodeSignature':'',
            'transactions':transaction
        }
        #Append to block
        Blockchain(self.block)

    def createBlock(self):
        pass

    def calculateBlockSize(self):
        pass

    def getChainHeight(self) -> int:
        pass

    def getPreviousHash(self):
        pass

def dicToBytes(dic) -> bytes:
    dump =b'{'
    for key in dic:
        dump+=bytes(f"'{key}' : ",'utf-8')
        if type(dic[key])==bytes:
            dump+=b"'"+dic[key]+b"'"
        if type(dic[key])==int:
            dump+=bytes(str(dic[key]),'utf-8')
        if type(dic[key])==str:
            dump+=b"'"+bytes(dic[key],'utf-8')+b"'"
        if type(dic[key])==dict:
            dump+=dicToBytes(dic)
    dump+=b'}'
    return dump
