import unittest
import os.path
import importlib.util

l = []
path, dirs, files = next(os.walk("./Mutant_files"))

for file in files:
    spec = importlib.util.spec_from_file_location(file, path+"/"+file)
    mutant = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mutant)
    l.append([file, mutant.Calculator.operation4(mutant.Calculator),  4])


class TestSequense(unittest.TestCase):
    pass


def test_generator(a, b):
    def test(self):
        self.assertEqual(a,b)
    return test


if __name__ == '__main__':

    for t in l:
        test_name = 'test_%s' % t[0]
        test = test_generator(t[1], t[2])
        setattr(TestSequense, test_name, test)
    unittest.main()
