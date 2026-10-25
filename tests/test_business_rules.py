from business_rules import (
    calculate_bean_cost,
    calculate_shipment_total,
    format_shipment_line,
    get_bulk_discount,
    largest_shipment,
    needs_pallet,
    requires_prepayment,
    total_shipped,
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

def test_needs_pallet():
    assert needs_pallet(60, 800) is False
    assert needs_pallet(61, 700) is False
    assert needs_pallet(61, 700.01) is True
    assert needs_pallet(80, 1000) is True

def test_total_shipped():
    shipments = [
        {"buyer": "A", "bag_price": 10.00, "bags": 10, "partner": False},
        {"buyer": "B", "bag_price": 10.00, "bags": 20, "partner": False},
    ]
    assert total_shipped(shipments) == 352.00
    assert total_shipped([]) == 0.0

def test_largest_shipment():
    shipments = [
        {"buyer": "A", "bag_price": 10.00, "bags": 10, "partner": False},
        {"buyer": "B", "bag_price": 10.00, "bags": 20, "partner": False},
        {"buyer": "C", "bag_price": 10.00, "bags": 20, "partner": False},
    ]
    assert largest_shipment(shipments) == "B"
    assert largest_shipment([]) == ""

def test_format_shipment_line():
    assert format_shipment_line("Uptown Bakery", 175.00, False, False) == (
        "Uptown Bakery: $175.00 | prepayment: no | pallet: no"
    )
    assert format_shipment_line("Zenith Grocers", 1892.00, True, True) == (
        "Zenith Grocers: $1892.00 | prepayment: yes | pallet: yes"
    )