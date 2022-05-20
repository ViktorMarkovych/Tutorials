from tutorials import iteration_recursion

def test_smoke() -> None:
    assert iteration_recursion.fibonacci(0) == 0, "Smoke test error"

def test_negative_element() -> None:
    assert iteration_recursion.fibonacci(-1) == -1, "Negative element test error"

def test_first_element() -> None:
    assert iteration_recursion.fibonacci(1) == 1, "First element test error"

def test_second_element() -> None:
    assert iteration_recursion.fibonacci(2) == 1, "Second element test error"

def test_third_element() -> None:
    assert iteration_recursion.fibonacci(3) == 2, "Third element test error"

def test_5_element() -> None:
    assert iteration_recursion.fibonacci(5) == 5, "Fifth element test error"

def test_10_element() -> None:
    assert iteration_recursion.fibonacci(10) == 55, "Tenth element test error"