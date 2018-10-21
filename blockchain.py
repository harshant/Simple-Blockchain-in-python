#!/usr/bin/python

#importing libraries
import hashlib
import datetime as dt 

comp_hash = 0 # Defining global variable to stored the hash when creating the block

#making Block class
class Block():
    # These data should be hashed and should not be tempered 
    block_number=1
    data = None
    previous_hash = 0
    timestamp = dt.datetime.now()
    nonce = 0
    next = None
    # hash could not be hashed :)
    hash = None

    # Defining constructor function
    def __init__(self,data):
        self.data = data


    # Defining hash function to hash the data
    def hash(self,nonce_value):
        self.nonce = nonce_value
        h = hashlib.sha256()
        h.update(
        str(self.data)+str(self.nonce)+str(self.previous_hash)+str(self.block_number)
        +str(self.timestamp)
        )
        return h.hexdigest()

    # Function to print block data
    def __str__(self):
        print "block_number:"+ str(self.block_number) + "\n data:" + self.data + "\n previous hash:" + str(int(self.previous_hash))  + "\n nonce :" + str(self.nonce) + "\n next block:" + "\n ========================================================="

# Defining BlockChain class 
class BlockChain():
    
    diff = 20 # Defining deficulty for mining
    maxNonce = 2**26 # Manixum nonce value to mine
    threeshold = 2**(256-diff) # Resulted hash should be shaller than threeshold value
    
    # Initializing first block called the genesis block
    block = Block("genesis")
    head = block

    def add_node(self):
        new_block = Block("new node")
        new_block.previous_hash = comp_hash
        print str(new_block.previous_hash) + "\n " 
        new_block.block_number = self.block.block_number + 1
        self.block.hash = comp_hash
        self.block.next = new_block
        self.block.__str__()
        self.block = new_block


    def miner(self,data):
        for n in range(self.maxNonce):
            self.block.data = str(data) + " is the block number -1 and the nonce is : " + str(n)
            comp_hash = self.block.hash(n) 
            if int(comp_hash,16) <= self.threeshold :
                print "working add_node"
                self.add_node()
                break


blockchain = BlockChain()

for m in range(10):
    blockchain.miner(m)
    print "blockchain object is working" + str(m)


