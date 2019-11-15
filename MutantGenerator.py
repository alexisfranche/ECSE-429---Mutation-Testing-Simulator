from __future__ import print_function
import os

#Team

class MutantGenerator:

    def __init__(self, filename):
        print("Mutation in progress...")
        self.file = filename
        self.content = []
        self.output = []
        self.mutations = ['*', '/', '+', '-']
        self.mut_dict = {'*': 0, '/': 0, '+': 0, '-': 0}
        self.getInput(filename)
        self.buildOutputTextFile()
        self.appendTotals()
        self.writeOutputTextFile()
        self.genMutatedSourceFiles()
        print("Mutation Completed...")
        print("Mutant_Stats and Mutant source files generated in folder 'Mutant_files'.")

    def getInput(self, filename):
        with open(filename) as file:
            self.content = file.readlines()

    def getMutants(self, cur_op):
        mut_list = []
        for mutant in self.mutations:
            if cur_op != mutant:
                mut_list.append(mutant)
        return mut_list

    def getAllOperators(self, line):
        i = 1
        mutants_inline = []
        for op in line:
            if str(op) is '*' or str(op) is '/' or str(op) is '+' or str(op) is '-':
                index = line.find(str(op))
                mutants_inline.append((str(op), i, index))
                i = i + 1
        return mutants_inline

    def createClassName(self, mut_file, i):
        z = 0
        for line in mut_file:
            if "Calculator" in line:
                newClass = line.replace("Calculator", "Mutant" + str(i), 1)
                return (newClass, z)
            z = z + 1



    def genMutatedSourceFiles(self):
        i = 1
        line_num = 0
        for line in self.content:
            for operator in self.getAllOperators(line):
                mutant_list = self.getMutants(operator[0])
                for item in mutant_list:
                    mutated_file = self.content.copy()
                    newLine = mutated_file[line_num]
                    mutant_loc = operator[2]
                    newLine = newLine[:mutant_loc] + item + newLine[mutant_loc+1:]
                    newLine = newLine.rstrip() + "  # Mutant inserted here, original mutant '{0}' \n".format(operator[0])
                    mutated_file[line_num] = newLine
                    classTup = self.createClassName(mutated_file, i)
                    mutated_file[classTup[1]] = classTup[0]
                    self.writeMutantSourceFile(mutated_file, i)
                    i = i + 1
            line_num = line_num + 1

    def writeMutantSourceFile(self, mut_file, num):
        dir = os.path.join(os.getcwd(), "Mutant_files")
        if not os.path.exists(dir):
            os.mkdir(dir)

        with open(os.path.join(dir, "Mutant" + str(num) + ".py"), 'w') as f:
            for line in mut_file:
                f.write(line)
        return

    def buildOutputTextFile(self):
        line_num = 1
        for line in self.content:
            for operator in self.getAllOperators(line):
                mutant_list = self.getMutants(operator[0])
                for item in mutant_list:
                    output_msg = """Mutant insertion on line: {0}\nOriginal arithmetic operator: '{1}'""".format(line_num, operator[0])
                    output_msg = output_msg + """\nOperator number {0} on this line\nType of mutant inserted: {1}
                                """.format(operator[1], item)
                    self.output.append(output_msg)
                    self.mut_dict[item] = int(self.mut_dict.get(item)) + 1

            line_num = line_num + 1

    def appendTotals(self):
        msg = """Total * mutants: {0}\nTotal / mutants: {1}\nTotal + mutants: {2}\nTotal - mutants: {3}
        """.format(self.mut_dict.get('*'), self.mut_dict.get('/'), self.mut_dict.get('+'), self.mut_dict.get('-'))
        self.output.append(msg)
        return

    def writeOutputTextFile(self):

        with open("Mutant_Stats.txt", 'w') as f:
            for item in self.output:
                f.write("%s\n" % item)
        return
