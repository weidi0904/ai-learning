def add(a: int | float, b: int | float) -> int | float:
    if not isinstance(a, int | float) or not isinstance(b, int | float):
        raise TypeError("add() only supports int or float values")

    return a + b
