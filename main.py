from __future__ import print_function
from MutantGenerator import MutantGenerator
import CalculatorUnitTest


def main():
    print("No Command Line Arguments, Using Default Input file: calculator.py")
    MutantGenerator("calculator.py")
    CalculatorUnitTest.execute()


if __name__ == "__main__":
    main()
