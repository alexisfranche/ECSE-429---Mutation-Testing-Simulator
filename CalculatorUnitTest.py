import unittest
import os.path
import importlib.util
import random


class TestSequence(unittest.TestCase):
    pass


def setup(test_list,dir):
    originalpath = os.path.join(os.getcwd(), "calculator.py")
    path, dirs, files = next(os.walk(os.path.join("Mutant_files", dir)))

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
        num5 = random.randint(1, 10)
        test_list.append([file, mutant.Calculator.use_calculator(mutant.Calculator, num1, num2, num3, num4, num5),
                          original.Calculator.use_calculator(original.Calculator, num1, num2, num3, num4, num5)])


def test_generator(a, b):
    def test(self):
        self.assertEqual(a, b)

    return test


def execute(directory):
    test_list = []
    setup(test_list, directory)
    for t in test_list:
        test_name = 'test_%s' % t[0]
        test = test_generator(t[1], t[2])
        setattr(TestSequence, test_name, test)
    unittest.main(module=__name__)
