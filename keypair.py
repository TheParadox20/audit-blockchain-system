from ecdsa import SigningKey, SECP256k1, VerifyingKey
from ecdsa.util import randrange_from_seed__trytryagain
from hashlib import sha256

class Keypair:
    """
    Class for working with keys
    """
    privateKey = 0
    privateKeyString = 0
    serialized_privateKey=0
    serialized_publicKey = 0

    def __init__(self,seed):
        self.seed = seed 

    def genKeyPair(self):
        """
        Generates keys, which returns an object of the KeyPair class.
        """
        self.privateKey = SigningKey.from_secret_exponent(randrange_from_seed__trytryagain(self.seed,SECP256k1.order),curve=SECP256k1,hashfunc=sha256)
        self.publicKey = self.privateKey.verifying_key
        self.serialized_privateKey = self.privateKey.to_pem()
        self.serialized_publicKey = self.publicKey.to_pem()
    
    def deserialize(self, key, mode='private', hash=sha256):
        """
        Takes in 
        """
        return SigningKey.from_pem(key, hashfunc=hash) if mode=='private' else VerifyingKey.from_pem(key)
    
    def keyToFile(self):
        file = open('keys/admin.txt','wb')
        file.write(self.serialized_privateKey)
        file.write(b'\x00')#Split private and public key
        file.write(self.serialized_publicKey)
        file.close()

#EXAMPLE
alpha = Keypair('Good Train House Koala')
alpha.genKeyPair()
alpha.keyToFile()