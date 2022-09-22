from email import message
from account import Account
from block import Block
from blockchain import Blockchain
from hash import Hash
from keypair import Keypair
from operation import Operation
from signature import Signature
from transaction import Transaction

def test_test():
    assert 'hello' == 'hello'

def test_keyGeneration():
    alpha_key1 = Keypair('Good Train House Koala')
    alpha_key1.genKeyPair()
    alpha_key2 = Keypair('Good Train House Koala')
    alpha_key2.genKeyPair()
    omega = Keypair('Hola Train House Koala')
    omega.genKeyPair()
    assert alpha_key1.serialized_privateKey == alpha_key2.serialized_privateKey #equal seeds, equal keys
    assert alpha_key1.serialized_privateKey != omega.serialized_privateKey

def test_serialization_deserialization():
    alpha = Keypair('Good Train House Koala')
    alpha.genKeyPair()
    assert alpha.privateKey == alpha.deserialize(alpha.serialized_privateKey)

def test_signing():
    pen = Signature()
    message = b'Yin & Yang'
    sk = 'keys/private.txt'
    vk = 'keys/public.txt'
    signature = pen.signData(sk,message)
    assert pen.verifySignature(signature,vk,message) == True
    assert pen.verifySignature(signature,'keys/alternate_public.txt',message) == False