import unittest
import os.path
import importlib.util


class TestSequence(unittest.TestCase):
    pass


def setup(test_list,dir):
    path, dirs, files = next(os.walk("Mutant_files\\"+dir))

    for file in files:
        spec = importlib.util.spec_from_file_location(file, path + "/" + file)
        mutant = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mutant)
        test_list.append([file, mutant.Calculator.operation4(mutant.Calculator), 4])


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
