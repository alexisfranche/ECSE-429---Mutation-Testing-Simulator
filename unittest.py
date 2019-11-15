

import unittest
import os.path


class Test(unittest.TestCase):
    path, dirs, files = next(os.walk("./Mutant_files"))
    file_count = len(files) - 1
    print(file_count)
    current_index = 1

    @classmethod
    def setUpClass(cls):
        global current_index
        currentMutant = f"Mutant{current_index}"

    @classmethod
    def evaluateMutant(cls):

