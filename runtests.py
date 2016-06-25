import unittest
import tests

if __name__ == '__main__':
    testsuite = unittest.TestLoader().loadTestsFromModule(tests)
    unittest.TextTestRunner().run(testsuite)