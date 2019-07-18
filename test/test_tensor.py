import unittest
from tensor.tensor import *

class TestTensorMethods(unittest.TestCase):

    def setUp(self):
        self.tensor1 = Tensor(2, [2,2], [1,2,3,4])
        self.tensor2 = Tensor(2, [2,2], [2,2,3,4])

    def tearDown(self):
        pass

    def test_ndims(self):
        self.assertEqual(self.tensor1.ndims, 2)

    def test_shape(self):
        self.assertEqual(self.tensor1.shape, [2,2])

    def test_elements(self):
        self.assertEqual(self.tensor1.elements, [1, 2, 3, 4])

    def test_add(self):
        tensor3 = self.tensor1 + self.tensor2
        self.assertEqual(tensor3.elements, [3, 4, 6, 8]) 

    def test_getter(self):
        self.assertEqual(self.tensor1[1], 2)

    def test_setter(self):
        self.tensor1[0] = 5
        self.assertEqual(self.tensor1.elements, [5, 2, 3, 4])

if __name__ == '__main__':
    unittest.main()
