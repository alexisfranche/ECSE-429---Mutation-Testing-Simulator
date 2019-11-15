from __future__ import print_function
from MutantGenerator import MutantGenerator
import sys


def main():

    if len(sys.argv) <= 1:
        print("No Command Line Arguments, Using Default Input file: calculator.py")
        mutant = MutantGenerator("calculator.py")
    elif len(sys.argv) == 2:
        print(f"Using input file: {0}".format(str(sys.argv[1])))
        mutant = MutantGenerator(str(sys.argv[1]))
    elif len(sys.argv) > 2:
        print("ERROR: too many command line arguments")
        return


if __name__ == "__main__":
    main()
