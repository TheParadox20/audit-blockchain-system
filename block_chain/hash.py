import hashlib
class Hash:
    """
    Wrapper class for using a hash function
    """
    def hash_256(message):

        return hashlib.sha256(message).hexdigest() if type(message)==bytes else hashlib.sha256(message.encode('utf-8')).hexdigest()