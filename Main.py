from block_chain.account import Account
from block_chain.operation import Operation
from block_chain.blockchain import Blockchain
from persistence.explorer import Explorer

try:
    open('persistence/db.bc')
except:
    Blockchain.initBlockchain()

"""
alice: 9ecde9c3174dc7d65a9c35d3c67e8a9f3f5046e52095ce451ebb41fb444dd814
bob: 5e4babf14f5ff937b8d1e4e1e25bf69eeea65d907ed0e7022419feebb1d7579f
charlie: b6f5e3b7122eab572cc2b9fb6ab2da998708cdd669ea2959b2eb580d5b9da196
"""
user = Account()
explorer = Explorer()
menu = ['Create transaction','Add account','List accounts','Verify transaction','View balance','quit']
print('Welcome to the Audit Blockchain System(ABS)')
while 1:
    choice = input('Login/Recover Wallet:\n\t1.) Login\n\t2.) Recover with mnemonic\n\t3.) Explore blockchain database\n')
    if choice == '3': # Explore Database
        print('Database hash:',Explorer.getChainState())
        print('Number of Blocks: ',Explorer.getChainHeight())
        print('Blocks')
        cursor = 0
        for i in range(0,Explorer.getChainHeight()):
            block =  Explorer.getBlock(cursor)[0]
            block = explorer.blockToDict(block)
            print(block['transactions'])
            cursor+=Explorer.getBlock(cursor)[1]
    if choice=='2':
        user.genAccount(input('Enter the 4 words to recover wallet:\n'))
        print(f"Account recoverd succesfully accountID : {user.accountID}")
        for c, i in enumerate(menu):
            print(f"\t{c+1}: {i}")
        choice = input('What would you want to do:\n')
        if int(choice)==len(menu):
            break
        if choice=='1':
            sender = input('Enter sender address/ID\n')
            receiver = input('Enter receiver address/ID\n')
            amount = float(input('Enter amount to be sent\n'))
            Operation(sender,receiver,amount)
        if choice=='2':
            print()
        if choice=='3':
            for i in user.wallet:
                for keys in i:
                    print(f"Address : {i[keys]}")