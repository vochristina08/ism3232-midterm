from business_rules import calculate_bean_cost


def test_calculate_bean_cost():
    assert round(calculate_bean_cost(14.00, 10), 2) == 140.00
