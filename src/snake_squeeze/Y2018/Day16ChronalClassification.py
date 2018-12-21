import re
from enum import Enum

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


class OpCodeExecute:
    def __init__(self, op_code_method):
        self.op_code_method = op_code_method


    def execute(self, capture):
        result = self.op_code_method.calculate(capture)
        is_matching = False
        # only if a result is defined, validate
        if result and capture.after:
            is_matching = True
            for i, j in zip(capture.after, result):
                if i != j:
                    is_matching = False
                    break
        return is_matching, result


    def __repr__(self):
        return self.op_code_method.op_code.name


class OpCodeFunctions:
    def __init__(self, op_code, register_method, evaluate):
        self.op_code = op_code
        self.register_method = register_method
        self.evaluate = evaluate


    def calculate(self, capture):
        return self.register_method(capture, self.evaluate)


    @classmethod
    def _create_register(cls, capture, new_register_value):
        register = []
        for i in range(4):
            if i == capture.instruction[3]:
                register.append(new_register_value)
            else:
                register.append(capture.before[i])
        return register


    @classmethod
    def with_register_a_and_b(cls, capture, evaluate):
        if not capture.supports_register():
            return None
        register_a_value = capture.before[capture.instruction[1]]
        register_b_value = capture.before[capture.instruction[2]]
        return cls._create_register(capture, evaluate(register_a_value, register_b_value))


    @classmethod
    def with_register_a_and_value_b(cls, capture, evaluate):
        if capture.instruction[1] > 3:
            return None
        register_a_value = capture.before[capture.instruction[1]]
        value_b = capture.instruction[2]
        return cls._create_register(capture, evaluate(register_a_value, value_b))


    @classmethod
    def with_value_a_and_register_b(cls, capture, evaluate):
        if capture.instruction[2] > 3:
            return None
        value_a = capture.instruction[1]
        register_b_value = capture.before[capture.instruction[2]]
        return cls._create_register(capture, evaluate(value_a, register_b_value))


    @classmethod
    def sum(cls, value_a, value_b):
        return value_a + value_b


    @classmethod
    def mul(cls, value_a, value_b):
        return value_a * value_b


    @classmethod
    def bit_and(cls, value_a, value_b):
        return value_a & value_b


    @classmethod
    def bit_or(cls, value_a, value_b):
        return value_a | value_b


    @classmethod
    def set(cls, value_a, _):
        return value_a


    @classmethod
    def gt(cls, value_a, value_b):
        return 1 if value_a > value_b else 0


    @classmethod
    def eq(cls, value_a, value_b):
        return 1 if value_a == value_b else 0


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


class OpCodes(Enum):
    addr = "addr"
    addi = "addi"
    mulr = "mulr"
    muli = "muli"
    banr = "banr"
    bani = "bani"
    borr = "borr"
    bori = "bori"
    setr = "setr"
    seti = "seti"
    gtir = "gtir"
    gtri = "gtri"
    gtrr = "gtrr"
    eqir = "eqir"
    eqri = "eqri"
    eqrr = "eqrr"
