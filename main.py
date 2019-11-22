from __future__ import print_function

import CalculatorUnitTest
from MutantGenerator import MutantGenerator


def main():
    print("No Command Line Arguments, Using Default Input file: calculator.py")
    MutantGenerator("calculator.py")
    CalculatorUnitTest.execute()


if __name__ == "__main__":
    main()
