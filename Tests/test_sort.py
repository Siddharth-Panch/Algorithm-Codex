import unittest,random

class SortTest(unittest.TestCase):
    def test(self,fn):
        pop=[i for i in range(10**8)]
        for _ in range(100):
            length=random.randint(0,10**6)
            z=random.choices(pop,k=length)
            """
                filler code
            """
            self.assertEqual(z,z.sort())

if __name__ == '__main__':
    unittest.main()
