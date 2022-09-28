import json
from block_chain.account import Account
from block_chain.block import Block
from block_chain.blockchain import Blockchain
from block_chain.hash import Hash
from block_chain.keypair import Keypair
from block_chain.operation import Operation
from block_chain.signature import Signature
from block_chain.transaction import Transaction
from persistence.explorer import Explorer

explorer = Explorer()
user = Account()
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
    assert pen.verifySignature(signature,'keys/alternate_public.txt',message) == False #Using different key pair to verify signature
    
    
def test_signing_from_object():
    pen = Signature()
    message = b'Yin & Yang'
    keys = Keypair('Bad Train House Koala')
    keys.genKeyPair()
    signature = pen.signData(keys.privateKey,message)
    assert pen.verifySignature(signature,keys.publicKey,message) == True

def test_accountID_generation():
    user_1 = Account()
    user_1.genAccount('Hello Good People Holla')
    user_2 = Account()
    user_2.genAccount('Hello Good People Holla')
    user_3 = Account()
    user_3.genAccount('A big bang Started!')
    print(user_1.accountID)
    print(user_2.accountID)
    print(user_3.accountID)
    assert user_1.accountID==user_2.accountID
    assert user_1.accountID!=user_3.accountID

def test_blockSize():
    transaction = {
        'operations':'operation',
        'transactionID':'self.transactionID',
        'Signature':'Account.signData(self.transactionID,0)'
    }
    block = Block(transaction)
    print(block.block)

def test_getBlock(): #Get genesis block
    block = json.loads(Explorer.getBlock(0)[0])
    blockSize = Explorer.getBlock(0)[1]
    genesisBlock = {
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
    }
    
    assert genesisBlock == block
    # assert genesisBlock['blockSize'] == blockSize == 224

def test_blockToDict():
    block = explorer.blockToDict(Explorer.getBlock(0)[0])
    assert float(block['transactions']['operations']['amount']) == 0
