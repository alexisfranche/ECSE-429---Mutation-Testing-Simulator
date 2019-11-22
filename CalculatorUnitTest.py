import importlib.util
import os.path
import random
import unittest

from concurrencytest import ConcurrentTestSuite, fork_for_tests
l = []

class TestSequence(unittest.TestCase):
    pass


def setup(test_list):
    originalpath = os.path.join(os.getcwd(), "calculator.py")
    path, dirs, files = next(os.walk("Mutant_files"))

    originalspec = importlib.util.spec_from_file_location("calculator.py", originalpath)
    original = importlib.util.module_from_spec(originalspec)
    originalspec.loader.exec_module(original)

    for file in files:
        spec = importlib.util.spec_from_file_location(file, path + "/" + file)
        mutant = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mutant)
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        num3 = random.randint(1, 10)
        num4 = random.randint(1, 10)
        l.append([num1, num2, num3, num4])
        test_list.append([file, mutant.Calculator.use_calculator(mutant.Calculator, num1, num2, num3, num4),
                          original.Calculator.use_calculator(original.Calculator, num1, num2, num3, num4)])


def test_generator(a, b):
    def test(self):
        self.assertEqual(a, b)

    return test


def execute():
    test_list = []
    setup(test_list)
    runner = unittest.TextTestRunner()
    for t in test_list:
        test_name = 'test_%s' % t[0]
        test = test_generator(t[1], t[2])
        setattr(TestSequence, test_name, test)

    fast = unittest.makeSuite(TestSequence, 'test')
    print('\nRun mutant tests across 3 processes:')
    concurrent_suite = ConcurrentTestSuite(fast, fork_for_tests(3))
    runner.run(concurrent_suite)
    print(l)
