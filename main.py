from __future__ import print_function
from MutantGenerator import MutantGenerator
import sys
import os


def main():

    print("No Command Line Arguments, Using Default Input file: calculator.py")
    mutant = MutantGenerator("calculator.py")
    os.system("python CalculatorUnitTest.py")


if __name__ == "__main__":
    main()
