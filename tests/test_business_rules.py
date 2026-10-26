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


def test_bean_cost():
    assert round(calculate_bean_cost(14.00, 10), 2) == 140.00

def test_bulk_discount_below_20():
    assert get_bulk_discount(19) == 0.0

def test_bulk_discount_at_20():
    assert get_bulk_discount(20) == 0.09

def test_large_discount_below_80():
    assert get_bulk_discount(79) == 0.09

def test_large_discount_at_80():
    assert get_bulk_discount(80) == 0.14

def test_partner_discount_changes_result():
    assert round(get_bulk_discount(20, True), 2) == 0.13
    assert get_bulk_discount(20, False) == 0.09

def test_shipment_total_with_shipping_fee():
    assert round(calculate_shipment_total(10.00, 10), 2) == 135.00

def test_shipping_fee_below_250():
    assert round(calculate_shipment_total(249.99, 1), 2) == 284.99

def test_no_shipping_fee_at_250():
    assert round(calculate_shipment_total(250.00, 1), 2) == 250.00

def test_shipment_total_with_bulk_discount():
    assert round(calculate_shipment_total(10.00, 20), 2) == 217.00

def test_prepayment_below_1500():
    assert requires_prepayment(1499.99) is False

def test_prepayment_at_1500():
    assert requires_prepayment(1500.00) is True


def test_pallet_at_60_bags():
    assert needs_pallet(60, 800.00) is False

def test_pallet_above_60_bags():
    assert needs_pallet(61, 800.00) is True

def test_pallet_at_700_total():
    assert needs_pallet(61, 700.00) is False

def test_pallet_above_700_total():
    assert needs_pallet(61, 700.01) is True


def test_total_shipped_with_two_shipments():
    shipments = [
        {"buyer": "A", "bag_price": 10.00, "bags": 10, "partner": False},
        {"buyer": "B", "bag_price": 10.00, "bags": 20, "partner": False},
    ]
    assert round(total_shipped(shipments), 2) == 352.00

def test_total_shipped_empty_list():
    assert round(total_shipped([]), 2) == 0.00

def test_largest_shipment_with_two_buyers():
    shipments = [
        {"buyer": "A", "bag_price": 10.00, "bags": 10, "partner": False},
        {"buyer": "B", "bag_price": 10.00, "bags": 20, "partner": False},
    ]
    assert largest_shipment(shipments) == "B"

def test_largest_shipment_tie():
    shipments = [
        {"buyer": "A", "bag_price": 10.00, "bags": 20, "partner": False},
        {"buyer": "B", "bag_price": 10.00, "bags": 20, "partner": False},
    ]
    assert largest_shipment(shipments) == "A"

def test_largest_shipment_empty_list():
    assert largest_shipment([]) == ""

def test_format_shipment_line_no_flags():
    assert format_shipment_line("Uptown Bakery", 175.00, False, False) == (
        "Uptown Bakery: $175.00 | prepayment: no | pallet: no"
    )

def test_format_shipment_line_both_flags():
    assert format_shipment_line("Zenith Grocers", 1892.00, True, True) == (
        "Zenith Grocers: $1892.00 | prepayment: yes | pallet: yes"
    )

def test_format_shipment_line_one_flag():
    assert format_shipment_line("Vine Cafe", 222.50, True, False) == (
        "Vine Cafe: $222.50 | prepayment: yes | pallet: no"
    )