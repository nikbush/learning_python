import task3.app as app


def test_func_is_odd_or_even_positive_values():
    assert app.is_odd_or_even(2) == "Even"
    assert app.is_odd_or_even(5) == "Odd"


def test_func_is_odd_or_even_zero_value():
    assert app.is_odd_or_even(0) == "Even"


def test_func_is_odd_or_even_nagative_values():
    assert app.is_odd_or_even(-7) == "Odd"
    assert app.is_odd_or_even(-100) == "Even"
