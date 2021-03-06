# imports
from hashlib import sha256 as sha
from binascii import hexlify, unhexlify
from time import time
from struct import pack

# hash function
# takes in a string
# returns a SHA-256 encoded hex-string


def hashSHA(string):
    return hexlify(sha(string.encode()).digest()).decode()

# create block
# takes in hash of previous block
# returns a dictionary object with:
# hash of previous block, data field, and the newly created block's hash


def createBlock(data, prevHash):
    blockHash = hashSHA(prevHash + data)
    return {
        'prevHash': prevHash,
        'data': data,
        'blockHash': blockHash
    }

# is valid
# takes in two blocks
# checks to see if the second block's previous hash field
# is equivalent to the first block's hash field


def isValid(blockA, blockB):
    return blockB['prevHash'] == blockA['blockHash']

# blockchain class
# contains the actual list of blocks and
# corresponding operations


class Blockchain:

    def __init__(self):
        self.chain = []

    # add block
    # takes in a block
    # adds it to the end of the chain
    def addBlock(self, block):
        self.chain.append(block)

    # top
    # returns the last block in the chain
    def top(self):
        return self.chain[-1]

    # height
    # returns the height (length) of the chain
    def height(self):
        return len(self.chain)

# genesis
# creates a block, but uses a null hash as the previous hash


def genesis():
    prevHash = "0"*64
    data = "genesis"
    return createBlock(data, prevHash)

# to integer
# takes in a byte string as an argument
# returns an integer with big endian byte order


def toInt(bytestring):
    return int.from_bytes(unhexlify(bytestring), byteorder='big')

# proof of work
# takes in data, a previous hash, and a target
# works to calculate a hash integer value less than the target
# does this by "incremental guessing"
# timestamp and nonce update each time we "swing the pick axe"
# once it's found, the output is like a traditional block
# but with the new fields as well


def createBlockPoW(data, prevHash, target):
    nonce = 0
    timestamp = int(time())
    blockHash = hashSHA(prevHash + data + str(timestamp) +
                        str(target) + str(nonce))
    while not toInt(blockHash) < target:
        nonce += 1
        timestamp = int(time())
        blockHash = hashSHA(prevHash + data + str(timestamp) +
                            str(target) + str(nonce))
    return {
        'prevHash': prevHash,
        'data': data,
        'timestamp': timestamp,
        'target': target,
        'nonce': nonce,
        'blockHash': blockHash
    }

############################################################################
############################ NEW CODE BELOW HERE ###########################
############################################################################

def hash_SHA(byte_string): 
    return hexlify(sha(byte_string).digest())
    


def int_to_bytes(val):
    """
    Given an integer i, return it in byte form, as an unsiged int 
    Will only work for positive ints. 
    Max value accepted is 2^32 - 1 or 4,294,967,295
    Basically any valid positive 32 bit int will work 
    
    :param val: integer i 
    :return: integer i in byte form as unsigned int.
    """
    return pack('I', val)

def short_to_bytes(val):
    """
    Given an short i, return it in byte form, as an unsiged short 
    Will only work for positive shorts. 
    Max value accepted is 2^8 - 1 or 65535
    Basically any valid positive 8 bit int will work 
    
    :param val: short i 
    :return: short i in byte form as unsigned short.
    """
    return pack('H', val)

def long_to_bytes(val):
    """
    Given an long i, return it in byte form, as an unsiged long 
    Will only work for positive longs. 
    Max value accepted is 2^32 - 1 or 4,294,967,295
    Basically any valid positive 8 bit int will work 
    
    :param val: long i 
    :return: long i in byte form as unsigned long.
    """
    return pack('L', val)
 
