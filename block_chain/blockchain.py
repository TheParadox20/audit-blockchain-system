class Blockchain:
    """
    class that allows to form a blockchain, a database of coins and existing transactions.
    """
    def __init__(self) -> None:
        try:
            open('../persistence/db.bc')
        except:
            self.initBlockchain()

    def initBlockchain(self):
        with open('../persistence/db.bc','wb') as f:
            pass
    
    def validateBlock(self):
        """
        Checks a block then adds to history
        """
        with open('../persistence/db.bc','wb') as f:
            pass