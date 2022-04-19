import os
import pytest

import sys
# sys.path.append("..")
sys.path.insert(0, '../src/')

from src.logger import setup_logger

# content of test_class.py
class TestClass:
    def log_directory_is_created(self):
        path = "logs"
        l = setup_logger('testing')
        assert path 
        