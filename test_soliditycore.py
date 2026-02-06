# test_soliditycore.py
"""
Tests for solidityCore module.
"""

import unittest
from soliditycore import solidityCore

class TestsolidityCore(unittest.TestCase):
    """Test cases for solidityCore class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = solidityCore()
        self.assertIsInstance(instance, solidityCore)
        
    def test_run_method(self):
        """Test the run method."""
        instance = solidityCore()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
