# test_paydrift.py
"""
Tests for PayDrift module.
"""

import unittest
from paydrift import PayDrift

class TestPayDrift(unittest.TestCase):
    """Test cases for PayDrift class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PayDrift()
        self.assertIsInstance(instance, PayDrift)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PayDrift()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
