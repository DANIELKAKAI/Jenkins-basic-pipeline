import unittest
from convert import CidrMaskConvert
from api import app


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


class ApiTestCase(unittest.TestCase):
    """This class represents the api endpoint test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = app
        self.app.config["TESTING"] = True
        self.client = self.app.test_client

    def test_root_endpoint(self):
        res = self.client().get('/')
        self.assertEqual(res.status_code, 200)
        self.assertIn('OK', str(res.data))

    def test_health_endpoint(self):
        res = self.client().get('/_health')
        self.assertEqual(res.status_code, 200)
        self.assertIn('OK', str(res.data))

    def test_mask_to_cidr_endpoint(self):
        res = self.client().get('/mask-to-cidr?value={}'.format('255.255.0.0'))
        json_data = res.get_json()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(json_data, {
            "function": "maskToCidr",
            "input": "255.255.0.0",
            "output": "16"
        })

    def test_cidr_to_mask_endpoint(self):
        res = self.client().get('/cidr-to-mask?value={}'.format('24'))
        json_data = res.get_json()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(json_data, {
            "function": "cidrToMask",
            "input": "24",
            "output": "255.255.255.0"
        })


if __name__ == '__main__':
    unittest.main()
