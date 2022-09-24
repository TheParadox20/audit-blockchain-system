from persistence.explorer import Explorer

def dictToBytes(dic) -> bytes:
    dump =b'{'
    for key in dic:
        dump+=bytes(f"'{key}': ",'utf-8')
        if type(dic[key])==bytes:
            dump+=b"'"+dic[key]+b"'"
        if type(dic[key])==int:
            dump+=bytes(str(dic[key]),'utf-8')
        if type(dic[key])==str:
            dump+=b"'"+bytes(dic[key],'utf-8')+b"'"
        if type(dic[key])==dict:
            dump+=dictToBytes(dic[key])
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

    def initBlockchain(self):
        with open('persistence/db.bc','wb') as f:
            f.write(b'0\n')
    
    def validateBlock(self,block):
        """
        Checks a block
        """
        return True
    
    def appendBlock(self,block):
        with open('persistence/db.bc','ab') as f:
            f.write(dictToBytes(block)+b'\n')
            