from persistence.explorer import Explorer

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

class Blockchain:
    """
    class that allows to form a blockchain, a database of coins and existing transactions.
    """
    def __init__(self,block) -> None:
        try:
            open('persistence/db.bc')
        except:
            self.initBlockchain()
        finally:
            if self.validateBlock(block):
                self.appendBlock(block)

    def initBlockchain():
        with open('persistence/db.bc','wb') as f:
            f.write(dictToBytes({
            'blockSize':224,
            'previousHash': '',
            'numberOfTransactions':0,
            'blockNumber': 1,
            'nodeSignature':'',
            'transactions':{
                'operations':{
                    'senderID':'',
                    'receiverID':'',
                    'amount':0
                },
                'transactionID':'',
                'Signature':''
            }
            }))
        with open('persistence/state.bc','wb') as f:
            f.write(dictToBytes({
                'height':1,
                'checksum':Explorer.getChainState()
            }))
    
    def validateBlock(self,block):
        """
        Checks a block
        """
        return True
    
    def updateBlockHeight():
        with open('persistence/db.bc','wb') as f:
            print(f.tell())
            h =Explorer.getChainHeight()+1
            print(h)
            f.write(bytes(h))
    
    def appendBlock(self, block):
        with open('persistence/db.bc','ab') as f:
            f.write(dictToBytes(block))
        
        height = Explorer.getChainHeight()
        state = Explorer.getChainState()
        with open('persistence/state.bc','wb') as f:
            f.write(dictToBytes({
                'height':height+1,
                'checksum': state
            }))