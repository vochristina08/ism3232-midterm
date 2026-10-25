from business_rules import calculate_bean_cost, get_bulk_discount


def test_calculate_bean_cost():
    assert round(calculate_bean_cost(14.00, 10), 2) == 140.00

def test_get_bulk_discount():
    assert get_bulk_discount(19) == 0.0
    assert get_bulk_discount(20) == 0.09
    assert get_bulk_discount(79) == 0.09
    assert get_bulk_discount(80) == 0.14
    assert get_bulk_discount(20, True) == 0.13
    assert round(get_bulk_discount(80, True), 2) == 0.18
