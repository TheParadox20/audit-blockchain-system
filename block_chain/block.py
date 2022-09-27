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
        self.prevHash = self.getPreviousHash()
        self.getPreviousHash()
        self.block = {
            'blockSize':0,
            'previousHash':self.prevHash,
            'numberOfTransactions':1,
            'blockNumber':Explorer.getChainHeight()+1,
            'nodeSignature':'',
            'transactions':transaction
        }
        size = self.calculateBlockSize()
        self.block['blockSize'] = size+len(str(size))
        #Append to block
        Blockchain(self.block)

    def createBlock(self):
        pass

    def calculateBlockSize(self):
        return len(dictToBytes(self.block))

    def getPreviousHash(self):
        cursor = 0
        for i in range(0,Explorer.getChainHeight()):
            block =  Explorer.getBlock(cursor)[0]
            if i == Explorer.getChainHeight()-1:
                return Hash.hash_256(block)
            cursor+=Explorer.getBlock(cursor)[1]

def dictToBytes(dic) -> bytes:
    dump =b'{'
    for i, key in enumerate(dic):
        dump+=bytes(f"\"{key}\": ",'utf-8')
        if type(dic[key])==bytes:
            dump+=b"\""+dic[key]+b"\""
        if type(dic[key])==int:
            dump+=bytes(str(dic[key]),'utf-8')
        if type(dic[key])==str:
            dump+=b"\""+bytes(dic[key],'utf-8')+b"\""
        if type(dic[key])==dict:
            dump+=dictToBytes(dic[key])
        if i!=len(dic)-1:
            dump+=b', '
    dump+=b'}'
    return dump