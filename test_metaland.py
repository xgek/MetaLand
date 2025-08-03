# test_metaland.py
"""
Tests for MetaLand module.
"""

import unittest
from metaland import MetaLand

class TestMetaLand(unittest.TestCase):
    """Test cases for MetaLand class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MetaLand()
        self.assertIsInstance(instance, MetaLand)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MetaLand()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
