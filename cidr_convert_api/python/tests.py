import unittest
from convert import CidrMaskConvert

class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.convert = CidrMaskConvert()

    def test_valid_cidr_to_mask(self):
        self.assertEqual('128.0.0.0', self.convert.cidr_to_mask('1'))
        self.assertEqual('255.255.0.0', self.convert.cidr_to_mask('16'))
        self.assertEqual('255.255.248.0', self.convert.cidr_to_mask('21'))
        self.assertEqual('255.255.255.255', self.convert.cidr_to_mask('32'))


    def test_valid_mask_to_cidr(self):
        self.assertEqual('1', self.convert.mask_to_cidr('128.0.0.0'))
        self.assertEqual('16', self.convert.mask_to_cidr('255.255.0.0'))
        self.assertEqual('21', self.convert.mask_to_cidr('255.255.248.0'))
        self.assertEqual('32', self.convert.mask_to_cidr('255.255.255.255'))


    def test_invalid_cidr_to_mask(self):
        self.assertEqual('Invalid', self.convert.cidr_to_mask('0'))
        self.assertEqual('Invalid', self.convert.cidr_to_mask(-1))
        self.assertEqual('Invalid', self.convert.cidr_to_mask(33))


    def test_invalid_mask_to_cidr(self):
        self.assertEqual('Invalid', self.convert.mask_to_cidr('0.0.0.0'))
        self.assertEqual('Invalid', self.convert.mask_to_cidr('0.0.0.0.0'))
        self.assertEqual('Invalid', self.convert.mask_to_cidr('255.255.255'))
        self.assertEqual('Invalid', self.convert.mask_to_cidr('11.0.0.0'))


if __name__ == '__main__':
    unittest.main()
