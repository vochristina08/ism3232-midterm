from business_rules import (
    calculate_bean_cost,
    calculate_shipment_total,
    get_bulk_discount,
    requires_prepayment,
)


def test_calculate_bean_cost():
    assert round(calculate_bean_cost(14.00, 10), 2) == 140.00

def test_get_bulk_discount():
    assert get_bulk_discount(19) == 0.0
    assert get_bulk_discount(20) == 0.09
    assert get_bulk_discount(79) == 0.09
    assert get_bulk_discount(80) == 0.14
    assert get_bulk_discount(20, True) == 0.13
    assert round(get_bulk_discount(80, True), 2) == 0.18

def test_calculate_shipment_total():
    assert calculate_shipment_total(10.00, 10) == 135.00
    assert calculate_shipment_total(10.00, 20) == 217.00
    assert calculate_shipment_total(10.00, 30) == 273.00

def test_requires_prepayment():
    assert requires_prepayment(1499.99) is False
    assert requires_prepayment(1500.00) is True
    assert requires_prepayment(2000.00) is True    