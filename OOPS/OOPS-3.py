# Python program to create a calculator class.
# Include methods for basic arithmetic operations.


class Calculator:
    def sum(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Error! Division by zero."

# Example usage:
Cal = Calculator()
print(f"Addition: {Cal.sum(13, 6)}")
print(f"Subtraction: {Cal.sub(13, 6)}")
print(f"Multiplication: {Cal.mul(13, 6)}")
print(f"Division: {Cal.divide(12, 0)}")
print(f"Division: {Cal.divide(12, 6)}")
