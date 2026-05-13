# test_sourcegraphcody.py
"""
Tests for SourcegraphCody module.
"""

import unittest
from sourcegraphcody import SourcegraphCody

class TestSourcegraphCody(unittest.TestCase):
    """Test cases for SourcegraphCody class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SourcegraphCody()
        self.assertIsInstance(instance, SourcegraphCody)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SourcegraphCody()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
