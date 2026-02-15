from app import Calculator

def test_add():
    calc = Calculator()
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0
    assert calc.add(0, 0) == 0
    print("✓ test_add pasado")

def test_subtract():
    calc = Calculator()
    assert calc.subtract(5, 3) == 2
    assert calc.subtract(0, 5) == -5
    print("✓ test_subtract pasado")

def test_multiply():
    calc = Calculator()
    assert calc.multiply(3, 4) == 12
    assert calc.multiply(5, 0) == 0
    print("✓ test_multiply pasado")

def test_divide():
    calc = Calculator()
    assert calc.divide(10, 2) == 5
    assert calc.divide(7, 2) == 3.5
    assert calc.divide(10, 0) == "Error: División por cero"
    print("✓ test_divide pasado")

def test_history():
    calc = Calculator()
    calc.add(2, 3)
    calc.multiply(4, 5)
    
    history = calc.get_history()
    assert len(history) == 2
    assert "2 + 3 = 5" in history[0]
    print("✓ test_history pasado")

if __name__ == "__main__":
    print("Ejecutando tests...\n")
    test_add()
    test_subtract()
    test_multiply()
    test_divide()
    test_history()
    print("\n✅ Todos los tests pasaron!")
