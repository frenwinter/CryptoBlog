# test_cryptoblog.py
"""
Tests for CryptoBlog module.
"""

import unittest
from cryptoblog import CryptoBlog

class TestCryptoBlog(unittest.TestCase):
    """Test cases for CryptoBlog class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CryptoBlog()
        self.assertIsInstance(instance, CryptoBlog)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CryptoBlog()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
