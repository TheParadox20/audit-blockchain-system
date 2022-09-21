class Signature:
    """
    Wrapper class for using digital signature
    """
    def __init__(self) -> None:
        pass

    def signData(self, privateKey, message) -> bytearray:
        pass

    def verifySignature(self, signature, publicKey, message) -> bool:
        pass