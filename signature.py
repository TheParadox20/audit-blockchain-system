from ecdsa import SigningKey, VerifyingKey, BadSignatureError
class Signature:
    """
    Wrapper class for using digital signature
    """
    def isFile(self, path) -> bool:
        try:
            f = open(path)
            f.close()
            return True
        except:
            return False
    def __init__(self) -> None:
        pass

    def signData(self, privateKey, message) -> bytearray:
        if self.isFile(privateKey):
            privateKey = SigningKey.from_pem(open(privateKey).read())
        else: #if not file
            pass
        if self.isFile(message):
            message = open(message, 'rb').read()
        #write signature to file
        with open(b'DB/'+message+b'_signature.txt','wb') as f:
            f.write(privateKey.sign(message))
        return privateKey.sign(message)

    def verifySignature(self, signature, publicKey, message) -> bool:
        if self.isFile(signature):
            signature = open(signature,'rb').read()
        if self.isFile(publicKey):
            publicKey = VerifyingKey.from_pem(open(publicKey).read())
        if self.isFile(message):
            message = open(message,'rb').read()
        try:
            publicKey.verify(signature,message)
            return True
        except BadSignatureError:
            return False