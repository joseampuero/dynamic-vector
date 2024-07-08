import unittest
from enums.unitStorage import UnitStorageEnum
from cacheLine import CacheLine
from enums.cacheLineState import CacheLineState
from cache import Cache

class TestCache(unittest.TestCase):
    def setUp(self):
        self.cache = Cache(32, UnitStorageEnum.KB, 64)

    def test_numberOfLines(self):
        # Test the number of lines calculation
        expected_lines = (32 * 1024) // 64
        self.assertEqual(self.cache.numberLines, expected_lines)

    def test_read_miss(self):
        # Test reading an address that is not in cache (miss)
        data = self.cache.read(0x0000)
        self.assertIsNone(data)
        self.assertEqual(self.cache.misses, 1)
        self.assertEqual(self.cache.hits, 0)

    def test_read_hit(self):
        # Test reading an address that is in cache (hit)
        self.cache.write(0x0000, 'data')
        data = self.cache.read(0x0000)
        self.assertEqual(data, 'data')
        self.assertEqual(self.cache.hits, 1)
        self.assertEqual(self.cache.misses, 1)

    def test_write_miss(self):
        # Test writing to an address that is not in cache (miss)
        self.cache.write(0x0000, 'data')
        self.assertEqual(self.cache.misses, 1)
        self.assertEqual(self.cache.hits, 0)
        data = self.cache.read(0x0000)
        self.assertEqual(data, 'data')

    def test_write_hit(self):
        # Test writing to an address that is in cache (hit)
        self.cache.write(0x0000, 'data')
        self.cache.write(0x0000, 'new_data')
        self.assertEqual(self.cache.hits, 1)
        self.assertEqual(self.cache.misses, 1)
        data = self.cache.read(0x0000)
        self.assertEqual(data, 'new_data')

    def test_invalidateOtherCaches(self):
        # Test invalidateOtherCaches function
        # Implementing a basic test for invalidateOtherCaches function
        self.cache.invalidateOtherCaches(0x0000)
        # This function is currently a placeholder, so we can't assert any changes.
        pass

    def test_cache_eviction(self):
        # Test the eviction policy when the cache is full
        for i in range(self.cache.numberLines + 1):
            self.cache.write(i * 64, f'data_{i}')
        self.assertEqual(self.cache.misses, self.cache.numberLines + 1)
        self.assertEqual(len(self.cache.cache), self.cache.numberLines)
        self.cache.write(0, 'new_data')
        self.assertNotIn((self.cache.numberLines * 64) // self.cache.lineSize, self.cache.cache)
        self.assertEqual(self.cache.misses, self.cache.numberLines + 1 + 1)
        self.assertEqual(self.cache.hits, 0)

    def test_getStats(self):
        # Test the getStats function
        self.cache.write(0x0000, 'data')
        self.cache.read(0x0000)
        hits, misses = self.cache.getStats()
        self.assertEqual(hits, 1)
        self.assertEqual(misses, 1)

if __name__ == '__main__':
    unittest.main()
