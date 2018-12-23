from enum import Enum


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
