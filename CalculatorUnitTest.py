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
    for t in test_list:
        test_name = 'test_%s' % t[0]
        test = test_generator(t[1], t[2])
        setattr(TestSequence, test_name, test)

    fast = unittest.makeSuite(TestSequence, 'test')
    print('\nRun mutant tests across 3 processes:')

    with open("output.log", 'w') as f:
        runner = unittest.TextTestRunner(f)
        concurrent_suite = ConcurrentTestSuite(fast, fork_for_tests(3))
        output = runner.run(concurrent_suite)

    with open("output.log", 'r') as f:
        lines = f.readlines()
        i = 1
        with open("results.txt", 'w') as w:
            for c in lines[0].strip():
                if c == '.':
                    w.write(f"\nMutant #{i} was not killed")
                    print(f"Mutant #{i} was not killed")
                else:
                    w.write(f"\nMutant #{i} was killed")
                    print(f"Mutant #{i} was killed")

                w.write(f"\nvector is {l[i - 1]}\n")
                print(f"vector is {l[i - 1]}\n")
                i = i + 1

    tot_tests = output.testsRun
    tot_fail = len(output.failures)
    mut_cov = (tot_fail / tot_tests) * 100

    with open("results.txt", "a") as w:
        w.write("\nMutant Coverage: %{0:.2f}".format(mut_cov))
    print("Mutant Coverage: %{0:.2f}".format(mut_cov))
