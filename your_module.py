# your_module.py
def safe_divide(a: float, b: float) -> float:
    """
    Divides a by b, handling division by zero.
    Returns 'inf' if b == 0.
    """
    try:
        return a / b
    except ZeroDivisionError:
        return float('inf')

def advanced_calculator(a: float, b: float, op: str) -> float:
    """
    Performs add, subtract, multiply, divide operations.
    Handles errors and unsupported ops.
    """
    if op == "add":
        return a + b
    elif op == "sub":
        return a - b
    elif op == "mul":
        return a * b
    elif op == "div":
        return safe_divide(a, b)
    else:
        raise ValueError("Unsupported operation")
