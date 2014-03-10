"""
Test suite loader
"""

import unittest
import doctest
import tstore.pgtablestorage as pgtablestorage
import tstore.tstore as tstore


def suite():
    tests = unittest.TestSuite()
    tests.addTests(doctest.DocTestSuite(pgtablestorage))
    tests.addTests(doctest.DocTestSuite(tstore))
    return tests

