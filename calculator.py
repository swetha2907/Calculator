class Calculator:
    def add(self, *args):
        return sum(args)

    def subtract(self, *args):
        result = args[0]
        for num in args[1:]:
            result -= num
        return result

    def multiply(self, *args):
        result = 1
        for num in args:
            result *= num
        return result

    def divide(self, *args):
        if 0 in args[1:]:
            raise ValueError("Division by zero is invalid")
        result = args[0]
        for num in args[1:]:
            result //= num
        return result

    def modulo(self, *args):
        return args[0] % args[1]

calc = Calculator()
print("Addition:", calc.add(10, 5))
print("Subtraction:", calc.subtract(10, 5, 2))
print("Multiplication:", calc.multiply(10, 5, 2))
print("Division:", calc.divide(10, 5, 2))
print("Modulo:", calc.modulo(10, 3))