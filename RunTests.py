#!/usr/bin/env python3

import unittest

root_dir = "tests"
unit_dir = f"{root_dir}/unit"

test_suite = unittest.TestLoader().discover(root_dir, pattern="*_test.py")

unittest.TextTestRunner().run(test_suite)
