import unittest
from tlb import TLB

class TestTLB(unittest.TestCase):
    def test_ifValueIsFoundThenLookupSuccessful(self):
        tlb = TLB(size=16)
        
        tlb.update(0, 100, modified=False)
        tlb.update(1, 200, modified=False)
        
        self.assertEqual(tlb.lookup(0).physical_address, 100)
        self.assertIsNone(tlb.lookup(2))


    def test_ifValueIsNotFoundThenLookupFail(self):
        tlb = TLB(size=16)
        
        tlb.update(0, 100, modified=False)
        tlb.update(1, 200, modified=False)
        
        self.assertIsNone(tlb.lookup(2))

    def test_updateAppliesReplacementPolicies(self):
        tlb = TLB(size=2)
        
        tlb.update(0, 100, modified=False)
        tlb.update(1, 200, modified=False)
        
        tlb.update(2, 300, modified=False)
        
        self.assertIsNone(tlb.lookup(0))
        self.assertEqual(tlb.lookup(1).physical_address, 200)
        self.assertEqual(tlb.lookup(2).physical_address, 300)

if __name__ == '__main__':
    unittest.main()