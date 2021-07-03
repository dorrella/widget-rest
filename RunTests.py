#!/usr/bin/env python3

import unittest
import os

# delete old log for sanity
log_file = "test_log.txt"
if os.path.exists(log_file):
    os.remove(log_file)

root_dir = "tests"
test_loader = unittest.TestLoader()
test_suite = test_loader.discover(root_dir, pattern="*_test.py")

unittest.TextTestRunner().run(test_suite)
