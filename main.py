from __future__ import print_function
from MutantGenerator import MutantGenerator
import CalculatorUnitTest
import os
import shutil
import threading


def partition():
    path, dirs, files = next(os.walk("./Mutant_files"))

    set_size = int(len(files) / 3)

    dir = os.path.join(os.getcwd(), "Mutant_files")
    for i in range(3):
        dir2 = os.path.join(dir, "Set" + str(i))
        if not os.path.exists(dir2):
            os.mkdir(dir2)

    for z in range(3):
        if z == 0:
            for file in files[:set_size]:
                shutil.copy(os.path.join(dir, file), os.path.join(dir, "Set0"))
        if z == 1:
            for file in files[set_size:2 * set_size]:
                shutil.copy(os.path.join(dir, file), os.path.join(dir, "Set1"))
        else:
            for file in files[2 * set_size:]:
                shutil.copy(os.path.join(dir, file), os.path.join(dir, "Set2"))


def main():
    print("No Command Line Arguments, Using Default Input file: calculator.py")
    MutantGenerator("calculator.py")
    partition()

    t1 = threading.Thread(target=CalculatorUnitTest.execute, args=["set0"])
    t2 = threading.Thread(target=CalculatorUnitTest.execute, args=["set1"])
    t3 = threading.Thread(target=CalculatorUnitTest.execute, args=["set2"])
    t1.start()
    t2.start()
    t3.start()


if __name__ == "__main__":
    main()
