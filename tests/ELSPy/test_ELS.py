# pylint: disable-all
import unittest
from ELSPy.ELS import ELS

class TestELSPy(unittest.TestCase):

  _wsdl = 'http://localhost:8080'

  def setUp(self):
    self.c = ELS(self._wsdl, 'username', 'password')

  def test_init(self):
    resp = self.c
    self.assertEqual(resp.wsdl, self._wsdl)
    self.assertEqual(resp.loginguid, None)