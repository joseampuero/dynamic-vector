import unittest
from tlb import TLB
import constants

class TestTLB(unittest.TestCase):
    def test_ifValueIsFoundThenLookupSuccessful(self):
        tlb = TLB(size=16, replacement_policy=constants.FIFO)
        
        tlb.update(0, 100)
        tlb.update(1, 200)
        
        self.assertEqual(tlb.lookup(0), 100)
        self.assertIsNone(tlb.lookup(2))

    def test_ifValueIsNotFoundThenLookupFail(self):
        tlb = TLB(size=16, replacement_policy=constants.FIFO)
        
        tlb.update(0, 100)
        tlb.update(1, 200)
        
        self.assertIsNone(tlb.lookup(2))    

    def test_updateAppliesReplacementPolicies(self):
        tlb = TLB(size=2, replacement_policy=constants.FIFO)
        
        tlb.update(0, 100)
        tlb.update(1, 200)
        
        tlb.update(2, 300)
        
        self.assertIsNone(tlb.lookup(0))
        self.assertEqual(tlb.lookup(1), 200)
        self.assertEqual(tlb.lookup(2), 300)

if __name__ == '__main__':
    unittest.main()