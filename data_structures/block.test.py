# imports
import unittest
from block import *
import time
from struct import unpack

# unit test class


class TestBlock(unittest.TestCase):

    # test hash function

    def testHashSHA(self):
        # testHashSHA part 1:
        # take two different strings
        # check to see if hashes are different
        a = "apple"
        b = "orange"
        hashA = hashSHA(a)
        hashB = hashSHA(b)
        self.assertNotEqual(hashA, hashB)

        # testHashSHA part 2:
        # take two long strings with a single letter changed
        # check to see if hashes are different
        s1 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
        s2 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minin veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
        hashS1 = hashSHA(s1)
        hashS2 = hashSHA(s2)
        self.assertNotEqual(hashS1, hashS2)

        # testHashSHA part 3:
        # take two of the same strings
        # hash them separately
        # check to see if the hashes are equivalent
        c = "melon"
        d = "melon"
        hashC = hashSHA(c)
        hashD = hashSHA(d)
        self.assertEqual(hashC, hashD)

    # test is valid
    # check to see if a block points backwards to a previous block
    def testIsValid(self):
        blockA = createBlock('this is block a', '000')
        blockB = createBlock('this is block b', blockA['blockHash'])
        self.assertTrue(isValid(blockA, blockB))

    # test add block
    # check to see if when adding a block it is contained in the chain
    def testAddBlock(self):
        bc = Blockchain()
        testBlock = createBlock('this is a test', '123456789')
        bc.addBlock(testBlock)
        self.assertEqual(bc.chain[0], testBlock)

    # test top
    # check to see if calling top returns the last block in the chain

    def testTop(self):
        bc = Blockchain()
        testBlock = createBlock('this is a test', '123456789')
        bc.addBlock(testBlock)
        self.assertEqual(bc.top(), testBlock)

    # test height
    # check to see if height returns the length of the chain
    def testHeight(self):
        bc = Blockchain()
        testBlock = createBlock('this is a test', '123456789')
        bc.addBlock(testBlock)
        bc.addBlock(testBlock)
        bc.addBlock(testBlock)
        bc.addBlock(testBlock)
        self.assertEqual(4, bc.height())

    # test proof of work
    # check to see if a proof of work mined block
    # contains a hash that's less than the target
    # check also how much time it takes to mine a block
    def testPoW(self):
        data = 'testPoW'
        prevHash = '000000'
        # play around with this exponent (stick to the 60-100 range)
        target = 10**75
        print("Mining...")
        a = int(time.time())
        b = createBlockPoW(data, prevHash, target)
        print("Block found!")
        c = int(time.time())
        print("Time it took: {} seconds".format((c-a)))
        self.assertLessEqual(toInt(b['blockHash']), target)

    def test_Hash_SHA(self):
        data = "SIG Blockchain"
        actual = hash_SHA(data.encode())
        self.assertIsInstance(actual, bytes)

    def test_int_to_bytes(self):
        """
        Tests out values for the int_to_bytes function. Tests out max values as well
        """
        byte1 = int_to_bytes(1) 
        #if we unpack the bytes as a unsigned integer, we should get the same value
        self.assertEqual(unpack('I', byte1)[0], 1)
        #test out 0
        byte0 = int_to_bytes(0) 
        self.assertEqual(unpack('I', byte0)[0], 0)
        #test out max signed 32 bit int
        byte_max_32 = int_to_bytes(2**31 -1)
        self.assertEqual(unpack('I', byte_max_32)[0], 2**31 -1)
        #test out max unsigned 32 bit int 
        byte_max_u32 = int_to_bytes(2**32 -1)
        self.assertEqual(unpack('I', byte_max_u32)[0], 2**32 -1)
     
    def test_short_to_bytes(self):
        """
        Tests out values for the short_to_bytes function. Tests out max values as well
        """
        byte1 = short_to_bytes(1) 
        #if we unpack the bytes as a unsigned integer, we should get the same value
        self.assertEqual(unpack('H', byte1)[0], 1)
        #test out 0
        byte0 = short_to_bytes(0) 
        self.assertEqual(unpack('H', byte0)[0], 0)
        #test out max unsigned 32 bit int 
        byte_max_short = short_to_bytes(2**8 -1)
        self.assertEqual(unpack('H', byte_max_short)[0], 2**8 -1)
       
    def test_long_to_bytes(self):
        """
        Tests out values for the long_to_bytes function. Tests out max values as well
        """
        byte1 = long_to_bytes(1) 
        #if we unpack the bytes as a unsigned integer, we should get the same value
        self.assertEqual(unpack('L', byte1)[0], 1)
        #test out 0
        byte0 = long_to_bytes(0) 
        self.assertEqual(unpack('L', byte0)[0], 0)
        #test out max unsigned 32 bit int 
        byte_max_long = long_to_bytes(2**32 -1)
        self.assertEqual(unpack('L', byte_max_long)[0], 2**32 -1)

if __name__ == '__main__':
    unittest.main()
