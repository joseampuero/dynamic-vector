import unittest
import ctypesAdapter

class TestMemorySimulator(unittest.TestCase):
    def test_valuesAreStoredCorrectly(self):
        helper = ctypesAdapter.CDLL('./helper.so')
        helper.memorySimulator.argtypes = [ctypesAdapter.c_int, ctypesAdapter.c_float]
        helper.memorySimulator.restype = ctypesAdapter.POINTER(ctypesAdapter.c_float)

        size = 5
        startValue = 900

        ptrArray = helper.memorySimulator(size, startValue)
        
        self.assertIsNotNone(ptrArray)
        for index, value in zip(range(size), range(startValue, startValue+size)):
            self.assertEqual(ptrArray[index], value)

        self.assertNotEqual(ptrArray[size], startValue+size)

if __name__ == '__main__':
    unittest.main()