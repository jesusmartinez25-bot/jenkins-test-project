class Calculator:
    def __init__(self):
        self.history = []
    
    def add(self, a, b):
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a, b):
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a, b):
        result = a * b
        self.history.append(f"{a} × {b} = {result}")
        return result
    
    def divide(self, a, b):
        if b == 0:
            return "Error: División por cero"
        result = a / b
        self.history.append(f"{a} ÷ {b} = {result}")
        return result
    
    def get_history(self):
        return self.history
    
    def clear_history(self):
        self.history = []


if __name__ == "__main__":
    calc = Calculator()
    
    print("=== Calculadora Simple ===\n")
    
    print("Operaciones:")
    print(f"10 + 5 = {calc.add(10, 5)}")
    print(f"20 - 8 = {calc.subtract(20, 8)}")
    print(f"6 × 7 = {calc.multiply(6, 7)}")
    print(f"100 ÷ 4 = {calc.divide(100, 4)}")
    print(f"10 ÷ 0 = {calc.divide(10, 0)}")
    
    print("\nHistorial de operaciones:")
    for operation in calc.get_history():
        print(f"  - {operation}")
