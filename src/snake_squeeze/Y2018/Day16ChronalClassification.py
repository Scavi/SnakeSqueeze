import re

from snake_squeeze.Y2018.DayHelper import OpCodeFunctions, OpCodes, OpCodeExecute
from snake_squeeze.Y2018.Helper import Graph


class Day16ChronalClassification:

    def __init__(self):
        self.op_code_executors = list()
        self.op_code_executors.append(OpCodeExecute(OpCodeFunctions(
            OpCodes.addr,
            OpCodeFunctions.with_register_a_and_b,
            OpCodeFunctions.sum)))
        self.op_code_executors.append(OpCodeExecute(OpCodeFunctions(
            OpCodes.addi,
            OpCodeFunctions.with_register_a_and_value_b,
            OpCodeFunctions.sum)))
        self.op_code_executors.append(OpCodeExecute(OpCodeFunctions(
            OpCodes.mulr,
            OpCodeFunctions.with_register_a_and_b,
            OpCodeFunctions.mul)))
        self.op_code_executors.append(OpCodeExecute(OpCodeFunctions(
            OpCodes.muli,
            OpCodeFunctions.with_register_a_and_value_b,
            OpCodeFunctions.mul)))
        self.op_code_executors.append(OpCodeExecute(OpCodeFunctions(
            OpCodes.banr,
            OpCodeFunctions.with_register_a_and_b,
            OpCodeFunctions.bit_and)))
        self.op_code_executors.append(OpCodeExecute(OpCodeFunctions(
            OpCodes.bani,
            OpCodeFunctions.with_register_a_and_value_b,
            OpCodeFunctions.bit_and)))
        self.op_code_executors.append(OpCodeExecute(OpCodeFunctions(
            OpCodes.borr,
            OpCodeFunctions.with_register_a_and_b,
            OpCodeFunctions.bit_or)))
        self.op_code_executors.append(OpCodeExecute(OpCodeFunctions(
            OpCodes.bori,
            OpCodeFunctions.with_register_a_and_value_b,
            OpCodeFunctions.bit_or)))
        self.op_code_executors.append(OpCodeExecute(OpCodeFunctions(
            OpCodes.setr,
            OpCodeFunctions.with_register_a_and_b,
            OpCodeFunctions.set)))
        self.op_code_executors.append(OpCodeExecute(OpCodeFunctions(
            OpCodes.seti,
            OpCodeFunctions.with_value_a_and_register_b,
            OpCodeFunctions.set)))
        self.op_code_executors.append(OpCodeExecute(OpCodeFunctions(
            OpCodes.gtir,
            OpCodeFunctions.with_value_a_and_register_b,
            OpCodeFunctions.gt)))
        self.op_code_executors.append(OpCodeExecute(OpCodeFunctions(
            OpCodes.gtri,
            OpCodeFunctions.with_register_a_and_value_b,
            OpCodeFunctions.gt)))
        self.op_code_executors.append(OpCodeExecute(OpCodeFunctions(
            OpCodes.gtrr,
            OpCodeFunctions.with_register_a_and_b,
            OpCodeFunctions.gt)))
        self.op_code_executors.append(OpCodeExecute(OpCodeFunctions(
            OpCodes.eqir,
            OpCodeFunctions.with_value_a_and_register_b,
            OpCodeFunctions.eq)))
        self.op_code_executors.append(OpCodeExecute(OpCodeFunctions(
            OpCodes.eqri,
            OpCodeFunctions.with_register_a_and_value_b,
            OpCodeFunctions.eq)))
        self.op_code_executors.append(OpCodeExecute(OpCodeFunctions(
            OpCodes.eqrr,
            OpCodeFunctions.with_register_a_and_b,
            OpCodeFunctions.eq)))


    def solve_1(self, instructions):
        high_matches = 0
        i = 0
        op_code_correlations = Graph()
        while i < len(instructions):
            if len(instructions[i].strip()) > 0:
                capture, i = self._create_capture_validation(instructions, i)
                match_count = 0
                # iterate through all op code function to determine what capture correlates to which op code
                for j in range(len(self.op_code_executors)):
                    is_match, _ = self.op_code_executors[j].execute(capture)
                    if is_match:
                        match_count += 1
                        op_code_correlations.add_edge(capture.instruction[0], j)

                if match_count > 2:
                    high_matches += 1
            i += 1
        return high_matches, op_code_correlations


    def solve_2(self, instructions, op_code_correlations):
        op_codes = self._determine_op_code_order(op_code_correlations)
        registers = [0] * 4
        for instruction in instructions:
            capture = Capture(instruction=[int(n) for n in instruction.split(" ")], before=registers)
            op_executor = op_codes[capture.instruction[0]]
            _, registers = op_executor.execute(capture)
        return registers[0]


    def _determine_op_code_order(self, op_code_correlations):
        known_instructions = set()
        op_code_order = [None] * len(op_code_correlations.graph)
        while len(known_instructions) < len(op_code_correlations.graph):
            distinct_instruction = None
            for instruction, correlations in op_code_correlations.graph.items():
                if len(correlations) == 1:
                    distinct_instruction = correlations.pop()
                    known_instructions.add(distinct_instruction)
                    op_code_order[instruction] = self.op_code_executors[distinct_instruction]
                    break

            for _, correlations in op_code_correlations.graph.items():
                if distinct_instruction in correlations:
                    correlations.remove(distinct_instruction)
        return op_code_order


    @staticmethod
    def _create_capture_validation(instructions, i):
        instruction = instructions[i + 1]
        before_line = re.search("(?<=(Before:\\s\\[))[^\\]]*", instructions[i]).group(0)
        after_line = re.search("(?<=(After:\\s\\s\\[))[^\\]]*", instructions[i + 2]).group(0)
        capture = Capture(
            instruction=[int(n) for n in instruction.split(" ")],
            before=[int(n) for n in before_line.split(",")],
            after=[int(n) for n in after_line.split(",")],
        )
        return capture, i + 2


class Capture:
    def __init__(self, instruction, before, after=None):
        self.instruction = instruction
        self.before = before
        self.after = after


    def supports_register(self):
        for i in range(1, len(self.instruction)):
            if self.instruction[i] > 3:
                return False
        return True
