import hashlib
import json

def dictToBytes(dic: dict) -> bytes:
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

class Explorer:
    """
    Reads data from the database, db.bc
    """
    databasePath = 'persistence/db.bc'
    def __init__(self):
        pass
    
    def getBlock(startIndex):
        #First get size of entire block
        with open('persistence/db.bc','rb') as f:
            f.seek(startIndex+len('{"blockSize": '))
            size = b''
            while 1:
                char = f.read(1)
                if char==b',':
                    break
                size += char
            size = int(size)-1
            f.seek(startIndex)
            block = f.read(size)
            return block, size
    
    def blockToDict(self,jsonString: bytes, isTransaction=False,isOperation=False):
        if isTransaction:
            # print(jsonString)
            keys = [b'operations',b'transactionID',b'Signature']
        elif isOperation:
            # print(jsonString)
            keys = [b'senderID',b'receiverID',b'amount']
        else:
            keys = [b'blockSize',b'previousHash',b'numberOfTransactions',b'blockNumber',b'nodeSignature',b'transactions']
        keyIndexes = []
        omega = {}
        for i in keys:
            keyIndexes.append(jsonString.index(b'"'+i+b'": '))
        keyIndexes.append(len(jsonString)+1)
        for i, key in enumerate(keys):
            
            if key==b'transactions': #if the key is transactions
                property = self.blockToDict(jsonString[keyIndexes[i]+len(key)+4:len(jsonString)-1],isTransaction=True)
            elif key==b'operations':
                property = self.blockToDict(jsonString[keyIndexes[i]+len(key)+4:keyIndexes[i+1]-2],isOperation=True)
            else:
                property = jsonString[keyIndexes[i]+len(key)+4:keyIndexes[i+1]-2]
            omega[key.decode('utf-8')] = property
        return omega
    
    def getLastBlockID(self):
        #Return hash of previous block
        pass

    def getChainState():
        file = "persistence/db.bc" # Location of the file (can be set a different way)
        BLOCK_SIZE = 65536 # The size of each read from the file

        file_hash = hashlib.sha256() # Create the hash object, can use something other than `.sha256()` if you wish
        with open(file, 'rb') as f: # Open the file to read it's bytes
            fb = f.read(BLOCK_SIZE) # Read from the file. Take in the amount declared above
            while len(fb) > 0: # While there is still data being read from the file
                file_hash.update(fb) # Update the hash
                fb = f.read(BLOCK_SIZE) # Read the next block from the file

        return (file_hash.hexdigest()) # Get the hexadecimal digest of the hash

    def getAccountBalance(self,accountID):
        #Goes through blockchain and pulls every past transaction and calculates current balance
        #Go through every block extracting transaction information related to the ID
        inputs = []
        outputs = []
        cursor = 0
        for i in range(0,Explorer.getChainHeight()):
            block =  Explorer.getBlock(cursor)[0]
            block = self.blockToDict(block)
            amount = (block['transactions']['operations']['amount'])
            if accountID == block['transactions']['operations']['senderID'].decode('utf-8')[1:65]:
                outputs.append(float(amount[:len(amount)-1]))
            if accountID == block['transactions']['operations']['receiverID'].decode('utf-8')[1:65]:
                inputs.append(float(amount[:len(amount)-1]))
            cursor+=Explorer.getBlock(cursor)[1]
        return sum(inputs)-sum(outputs)
    
    def getChainHeight() -> int:
        with open('persistence/state.bc','rb') as f:
            state = f.read()
            state = json.loads(state)
        return state['height']

    def readChain(self):
        f = open('','')
        while 1:
            data = f.read(200)
            if not data:
                break
            print(data)
