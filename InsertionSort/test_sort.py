from copy import deepcopy
import unittest,random
from Insertion_Sort import insertion_sort

class SortTest(unittest.TestCase):
    def test(self,fn=insertion_sort):
        pop=[i for i in range(10**6)]
        for _ in range(100):
            length=random.randint(0,10**4)
            z=random.choices(pop,k=length)
            y=deepcopy(z)
            fn(y,0,length-1)
            self.assertEqual(sorted(z),y)

if __name__ == '__main__':
    unittest.main()
