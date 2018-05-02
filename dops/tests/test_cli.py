#!/usr/bin/env python3
# coding=utf-8

"""
@version: 0.1
@author: ysicing
@file: dops/test_cli.py 
@time: Apr 27, 14:37
"""

import pexpect
import unittest


class CliTest(unittest.TestCase):

    def test_run_cli(self):
        self.cli = None
        self.step_run_cli()

    def step_run_cli(self):
        self.cli = pexpect.spawnu('dops')


if __name__ == "__main__":
    unittest.main()